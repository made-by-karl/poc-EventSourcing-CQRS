package com.draeger.smartcoffee;

import com.draeger.smartcoffee.application.command.RegisterMachineCommand;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineCommandUseCase;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class DataInitializer implements ApplicationRunner {

    private final CoffeeMachineCommandUseCase commandService;

    public DataInitializer(CoffeeMachineCommandUseCase commandService) {
        this.commandService = commandService;
    }

    @Override
    public void run(ApplicationArguments args) {
        commandService.registerMachine(new RegisterMachineCommand("OR Machine 1", 60));
        commandService.registerMachine(new RegisterMachineCommand("OR Machine 2", 60));
        commandService.registerMachine(new RegisterMachineCommand("Doctors' Lounge", 40));
    }
}
