package com.draeger.smartcoffee.application.service;

import com.draeger.smartcoffee.application.command.ProduceCoffeeCommand;
import com.draeger.smartcoffee.application.command.RefillBeansCommand;
import com.draeger.smartcoffee.application.command.RegisterMachineCommand;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineCommandUseCase;
import com.draeger.smartcoffee.application.port.out.CoffeeMachineRepository;
import com.draeger.smartcoffee.domain.event.BeansRefilled;
import com.draeger.smartcoffee.domain.event.CoffeeProduced;
import com.draeger.smartcoffee.domain.event.MachineRegistered;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.util.UUID;

@Service
public class CoffeeMachineCommandService implements CoffeeMachineCommandUseCase {

    private final CoffeeMachineRepository repository;

    public CoffeeMachineCommandService(CoffeeMachineRepository repository) {
        this.repository = repository;
    }

    @Override
    public UUID registerMachine(RegisterMachineCommand command) {
        UUID machineId = UUID.randomUUID();
        MachineRegistered event = new MachineRegistered(
            machineId, command.name(), command.initialBeans(), Instant.now()
        );

        CoffeeMachine machine = repository.create(event);
        return machine.getId();
    }

    @Override
    public void produceCoffee(ProduceCoffeeCommand command) {
        CoffeeMachine machine = repository.load(command.machineId());
        CoffeeProduced event = machine.handle(command);
        repository.update(machine, event);
    }

    @Override
    public void refillBeans(RefillBeansCommand command) {
        CoffeeMachine machine = repository.load(command.machineId());
        BeansRefilled event = machine.handle(command);
        repository.update(machine, event);
    }
}
