package com.draeger.smartcoffee.adapter.out;

import com.draeger.smartcoffee.application.port.out.CoffeeMachineRepository;
import com.draeger.smartcoffee.application.port.out.EventStore;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.UUID;

@Component
public class InMemoryEventSourcedRepository implements CoffeeMachineRepository {

    private final EventStore eventStore;

    public InMemoryEventSourcedRepository(EventStore eventStore) {
        this.eventStore = eventStore;
    }

    @Override
    public CoffeeMachine load(UUID machineId) {
        List<DomainEvent> events = eventStore.loadEvents(machineId);
        return CoffeeMachine.reconstitute(events);
    }

    @Override
    public boolean exists(UUID machineId) {
        return eventStore.getAllMachineIds().contains(machineId);
    }
}
