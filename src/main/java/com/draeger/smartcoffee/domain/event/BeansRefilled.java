package com.draeger.smartcoffee.domain.event;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.time.Instant;
import java.util.UUID;

public class BeansRefilled extends DomainEvent {

    private final String user;
    private final int beansAdded;

    @JsonCreator
    public BeansRefilled(
            @JsonProperty("aggregateId") UUID aggregateId,
            @JsonProperty("user")        String user,
            @JsonProperty("beansAdded")  int beansAdded,
            @JsonProperty("occurredAt")  Instant occurredAt) {
        super(aggregateId, AggregateTypes.COFFEE_MACHINE, occurredAt);
        this.user = user;
        this.beansAdded = beansAdded;
    }

    public String getUser() {
        return user;
    }

    public int getBeansAdded() {
        return beansAdded;
    }
}
