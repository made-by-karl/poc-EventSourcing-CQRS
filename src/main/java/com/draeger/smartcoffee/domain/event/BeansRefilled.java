package com.draeger.smartcoffee.domain.event;

import java.time.Instant;
import java.util.UUID;

public class BeansRefilled extends DomainEvent {

    private final String user;
    private final int beansAdded;
    private final int beansAvailableAfter;

    public BeansRefilled(UUID machineId, String user, int beansAdded, int beansAvailableAfter, Instant occurredAt) {
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
