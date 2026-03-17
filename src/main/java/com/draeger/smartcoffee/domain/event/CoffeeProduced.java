package com.draeger.smartcoffee.domain.event;

import com.draeger.smartcoffee.domain.model.CoffeeType;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.time.Instant;
import java.util.UUID;

public class CoffeeProduced extends DomainEvent {

    private final CoffeeType coffeeType;
    private final String user;
    private final int beansConsumed;

    @JsonCreator
    public CoffeeProduced(
            @JsonProperty("machineId")     UUID machineId,
            @JsonProperty("coffeeType")    CoffeeType coffeeType,
            @JsonProperty("user")          String user,
            @JsonProperty("beansConsumed") int beansConsumed,
            @JsonProperty("occurredAt")    Instant occurredAt) {
        super(machineId, occurredAt);
        this.coffeeType = coffeeType;
        this.user = user;
        this.beansConsumed = beansConsumed;
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
}
