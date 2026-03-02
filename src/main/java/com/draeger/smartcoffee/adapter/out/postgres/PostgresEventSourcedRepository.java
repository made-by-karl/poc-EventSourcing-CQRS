package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.application.port.out.CoffeeMachineRepository;
import com.draeger.smartcoffee.application.port.out.EventStore;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Primary
@Repository
public class PostgresEventSourcedRepository implements CoffeeMachineRepository {

    private final EventStore eventStore;

    public PostgresEventSourcedRepository(EventStore eventStore) {
        this.eventStore = eventStore;
    }

    @Override
    public CoffeeMachine load(UUID machineId) {
        List<DomainEvent> events = eventStore.loadEvents(machineId);
        return CoffeeMachine.reconstitute(events);
    }

    @Override
    public boolean exists(UUID machineId) {
        return !eventStore.loadEvents(machineId).isEmpty();
    }
}
