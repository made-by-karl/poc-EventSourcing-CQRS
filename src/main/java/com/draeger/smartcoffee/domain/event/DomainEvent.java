package com.draeger.smartcoffee.domain.event;

import java.time.Instant;
import java.util.UUID;

public abstract class DomainEvent {

    private final UUID machineId;
    private final Instant occurredAt;

    protected DomainEvent(UUID machineId, Instant occurredAt) {
        this.machineId = machineId;
        this.occurredAt = occurredAt;
    }

    public UUID getMachineId() {
        return machineId;
    }

    public Instant getOccurredAt() {
        return occurredAt;
    }

    public String getEventType() {
        return this.getClass().getSimpleName();
    }
}
