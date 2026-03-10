package com.draeger.smartcoffee.application.command;

import com.draeger.smartcoffee.domain.model.CoffeeType;

import java.util.UUID;

public record ProduceCoffeeCommand(UUID machineId, CoffeeType coffeeType, String user) {
}
