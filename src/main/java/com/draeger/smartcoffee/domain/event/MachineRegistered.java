package com.draeger.smartcoffee.domain.event;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.time.Instant;
import java.util.UUID;

public class MachineRegistered extends DomainEvent {

    private final String name;
    private final int initialBeans;

    @JsonCreator
    public MachineRegistered(
            @JsonProperty("machineId")    UUID machineId,
            @JsonProperty("name")         String name,
            @JsonProperty("initialBeans") int initialBeans,
            @JsonProperty("occurredAt")   Instant occurredAt) {
        super(machineId, occurredAt);
        this.name = name;
        this.initialBeans = initialBeans;
    }

    public String getName() {
        return name;
    }

    public int getInitialBeans() {
        return initialBeans;
    }
}
