package com.draeger.smartcoffee.domain.model;

import com.draeger.smartcoffee.application.command.ProduceCoffeeCommand;
import com.draeger.smartcoffee.application.command.RefillBeansCommand;
import com.draeger.smartcoffee.domain.event.BeansRefilled;
import com.draeger.smartcoffee.domain.event.CoffeeProduced;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.event.MachineRegistered;
import com.draeger.smartcoffee.domain.exception.InsufficientBeansException;

import java.time.Instant;
import java.util.List;
import java.util.UUID;

public class CoffeeMachine {

    private static final int MAX_BEANS_CAPACITY = 60;

    private UUID id;
    private String name;
    private int beansAvailable;

    private CoffeeMachine() {
    }

    public static CoffeeMachine reconstitute(List<DomainEvent> events) {
        CoffeeMachine machine = new CoffeeMachine();
        for (DomainEvent event : events) {
            machine.apply(event);
        }
        return machine;
    }

    public CoffeeProduced handle(ProduceCoffeeCommand command) {
        int beansRequired = command.coffeeType().getBeansRequired();
        if (beansAvailable < beansRequired) {
            throw new InsufficientBeansException(
                "Not enough beans. Required: " + beansRequired + ", available: " + beansAvailable
            );
        }
        CoffeeProduced event = new CoffeeProduced(
            id,
            command.coffeeType(),
            command.user(),
            beansRequired,
            beansAvailable - beansRequired,
            Instant.now()
        );
        apply(event);
        return event;
    }

    public BeansRefilled handle(RefillBeansCommand command) {
        BeansRefilled event = new BeansRefilled(
            id,
            command.user(),
            command.beansToAdd(),
            Math.min(MAX_BEANS_CAPACITY, beansAvailable + command.beansToAdd()),
            Instant.now()
        );
        apply(event);
        return event;
    }

    private void apply(DomainEvent event) {
        if (event instanceof MachineRegistered e) {
            this.id = e.getMachineId();
            this.name = e.getName();
            this.beansAvailable = e.getInitialBeans();
        } else if (event instanceof CoffeeProduced e) {
            this.beansAvailable = e.getBeansAvailableAfter();
        } else if (event instanceof BeansRefilled e) {
            this.beansAvailable = e.getBeansAvailableAfter();
        }
    }

    public UUID getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getBeansAvailable() {
        return beansAvailable;
    }
}
