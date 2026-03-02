package com.draeger.smartcoffee.domain.event;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.time.Instant;
import java.util.UUID;

public class BeansRefilled extends DomainEvent {

    private final String user;
    private final int beansAdded;
    private final int beansAvailableAfter;

    @JsonCreator
    public BeansRefilled(
            @JsonProperty("machineId")           UUID machineId,
            @JsonProperty("user")                String user,
            @JsonProperty("beansAdded")          int beansAdded,
            @JsonProperty("beansAvailableAfter") int beansAvailableAfter,
            @JsonProperty("occurredAt")          Instant occurredAt) {
        super(machineId, occurredAt);
        this.user = user;
        this.beansAdded = beansAdded;
        this.beansAvailableAfter = beansAvailableAfter;
    }

    public String getUser() {
        return user;
    }

    public int getBeansAdded() {
        return beansAdded;
    }

    public int getBeansAvailableAfter() {
        return beansAvailableAfter;
    }
}
