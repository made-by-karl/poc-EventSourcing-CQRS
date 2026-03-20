package com.draeger.smartcoffee.domain.event;

import java.time.Instant;
import java.util.UUID;

public abstract class DomainEvent {

    private final UUID aggregateId;
    private final String aggregateType;
    private final Instant occurredAt;

    protected DomainEvent(UUID aggregateId, String aggregateType, Instant occurredAt) {
        this.aggregateId = aggregateId;
        this.aggregateType = aggregateType;
        this.occurredAt = occurredAt;
    }

    public UUID getAggregateId() {
        return aggregateId;
    }

    public String getAggregateType() {
        return aggregateType;
    }

    public Instant getOccurredAt() {
        return occurredAt;
    }

    public String getEventType() {
        return this.getClass().getSimpleName();
    }
}
