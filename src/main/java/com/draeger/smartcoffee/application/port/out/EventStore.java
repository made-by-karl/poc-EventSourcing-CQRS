package com.draeger.smartcoffee.application.port.out;

import com.draeger.smartcoffee.domain.event.DomainEvent;

import java.util.List;
import java.util.UUID;

public interface EventStore {

    void append(DomainEvent event);

    List<DomainEvent> loadEvents(UUID aggregateId);

    List<DomainEvent> loadAllEvents();

    List<UUID> getAllAggregateIds();
}
