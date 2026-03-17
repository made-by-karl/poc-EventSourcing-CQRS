package com.draeger.smartcoffee.application.port.out;

import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.event.MachineRegistered;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;

import java.util.UUID;

public interface CoffeeMachineRepository {

    CoffeeMachine create(MachineRegistered event);
    
    CoffeeMachine load(UUID machineId);

    boolean exists(UUID machineId);

    void update(CoffeeMachine machine, DomainEvent event);
}
