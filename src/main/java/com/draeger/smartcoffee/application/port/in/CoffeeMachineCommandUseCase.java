package com.draeger.smartcoffee.application.port.in;

import com.draeger.smartcoffee.application.command.ProduceCoffeeCommand;
import com.draeger.smartcoffee.application.command.RefillBeansCommand;
import com.draeger.smartcoffee.application.command.RegisterMachineCommand;

import java.util.UUID;

public interface CoffeeMachineCommandUseCase {

    UUID registerMachine(RegisterMachineCommand command);

    void produceCoffee(ProduceCoffeeCommand command);

    void refillBeans(RefillBeansCommand command);
}
