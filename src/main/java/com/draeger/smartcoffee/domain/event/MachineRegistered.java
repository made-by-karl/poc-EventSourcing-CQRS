package com.draeger.smartcoffee.domain.event;

import java.time.Instant;
import java.util.UUID;

public class MachineRegistered extends DomainEvent {

    private final String name;
    private final int initialBeans;

    public MachineRegistered(UUID machineId, String name, int initialBeans, Instant occurredAt) {
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
