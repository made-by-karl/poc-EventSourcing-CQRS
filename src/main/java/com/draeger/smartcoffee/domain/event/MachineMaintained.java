package com.draeger.smartcoffee.domain.event;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.time.Instant;
import java.util.UUID;

public class MachineMaintained extends DomainEvent {

    private final String user;
    private final Instant maintainedAt;
    private final int beansAfterMaintenance;

    @JsonCreator
    public MachineMaintained(
            @JsonProperty("aggregateId")            UUID aggregateId,
            @JsonProperty("user")                   String user,
            @JsonProperty("maintainedAt")           Instant maintainedAt,
            @JsonProperty("beansAfterMaintenance")  int beansAfterMaintenance,
            @JsonProperty("occurredAt")             Instant occurredAt) {
        super(aggregateId, AggregateTypes.COFFEE_MACHINE, occurredAt);
        this.user = user;
        this.maintainedAt = maintainedAt;
        this.beansAfterMaintenance = beansAfterMaintenance;
    }

    public String getUser() {
        return user;
    }

    public Instant getMaintainedAt() {
        return maintainedAt;
    }

    public int getBeansAfterMaintenance() {
        return beansAfterMaintenance;
    }
}
