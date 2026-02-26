package com.draeger.smartcoffee.domain.event;

import com.draeger.smartcoffee.domain.model.CoffeeType;

import java.time.Instant;
import java.util.UUID;

public class CoffeeProduced extends DomainEvent {

    private final CoffeeType coffeeType;
    private final String user;
    private final int beansConsumed;
    private final int beansAvailableAfter;

    public CoffeeProduced(UUID machineId, CoffeeType coffeeType, String user,
                          int beansConsumed, int beansAvailableAfter, Instant occurredAt) {
        super(machineId, occurredAt);
        this.coffeeType = coffeeType;
        this.user = user;
        this.beansConsumed = beansConsumed;
        this.beansAvailableAfter = beansAvailableAfter;
    }

    public CoffeeType getCoffeeType() {
        return coffeeType;
    }

    public String getUser() {
        return user;
    }

    public int getBeansConsumed() {
        return beansConsumed;
    }

    public int getBeansAvailableAfter() {
        return beansAvailableAfter;
    }
}
