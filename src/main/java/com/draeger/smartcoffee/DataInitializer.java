package com.draeger.smartcoffee;

import com.draeger.smartcoffee.application.command.RegisterMachineCommand;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineCommandUseCase;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;

@Component
public class DataInitializer implements ApplicationRunner {

    private final CoffeeMachineCommandUseCase commandService;
    private final JdbcTemplate jdbc;

    public DataInitializer(CoffeeMachineCommandUseCase commandService, JdbcTemplate jdbc) {
        this.commandService = commandService;
        this.jdbc = jdbc;
    }

    @Override
    public void run(ApplicationArguments args) {
        Integer count = jdbc.queryForObject(
            "SELECT COUNT(*) FROM domain_events WHERE event_type = 'MachineRegistered'", Integer.class);
        if (count != null && count > 0) {
            return;
        }
        commandService.registerMachine(new RegisterMachineCommand("OR Machine 1", 60));
        commandService.registerMachine(new RegisterMachineCommand("OR Machine 2", 60));
        commandService.registerMachine(new RegisterMachineCommand("Doctors' Lounge", 40));
    }
}
