package com.draeger.smartcoffee.application.port.out;

import com.draeger.smartcoffee.domain.model.CoffeeMachine;

import java.util.UUID;

public interface CoffeeMachineRepository {

    CoffeeMachine load(UUID machineId);

    boolean exists(UUID machineId);
}
