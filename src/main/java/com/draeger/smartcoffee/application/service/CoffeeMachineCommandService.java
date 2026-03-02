package com.draeger.smartcoffee.application.service;

import com.draeger.smartcoffee.application.command.ProduceCoffeeCommand;
import com.draeger.smartcoffee.application.command.RefillBeansCommand;
import com.draeger.smartcoffee.application.command.RegisterMachineCommand;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineCommandUseCase;
import com.draeger.smartcoffee.application.port.out.CoffeeMachineRepository;
import com.draeger.smartcoffee.application.port.out.EventStore;
import com.draeger.smartcoffee.application.port.out.SnapshotStore;
import com.draeger.smartcoffee.domain.event.BeansRefilled;
import com.draeger.smartcoffee.domain.event.CoffeeProduced;
import com.draeger.smartcoffee.domain.event.MachineRegistered;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.util.UUID;

@Service
public class CoffeeMachineCommandService implements CoffeeMachineCommandUseCase {

    private final EventStore eventStore;
    private final CoffeeMachineRepository repository;
    private final SnapshotStore snapshotStore;

    public CoffeeMachineCommandService(EventStore eventStore, CoffeeMachineRepository repository,
                                       SnapshotStore snapshotStore) {
        this.eventStore = eventStore;
        this.repository = repository;
        this.snapshotStore = snapshotStore;
    }

    @Override
    public UUID registerMachine(RegisterMachineCommand command) {
        UUID machineId = UUID.randomUUID();
        MachineRegistered event = new MachineRegistered(
            machineId, command.name(), command.initialBeans(), Instant.now()
        );
        eventStore.append(machineId, event);
        CoffeeMachine machine = repository.load(machineId);
        snapshotStore.maybeSnapshot(machineId, machine);
        return machineId;
    }

    @Override
    public void produceCoffee(ProduceCoffeeCommand command) {
        CoffeeMachine machine = repository.load(command.machineId());
        CoffeeProduced event = machine.handle(command);
        eventStore.append(command.machineId(), event);
        snapshotStore.maybeSnapshot(command.machineId(), machine);
    }

    @Override
    public void refillBeans(RefillBeansCommand command) {
        CoffeeMachine machine = repository.load(command.machineId());
        BeansRefilled event = machine.handle(command);
        eventStore.append(command.machineId(), event);
        snapshotStore.maybeSnapshot(command.machineId(), machine);
    }
}
