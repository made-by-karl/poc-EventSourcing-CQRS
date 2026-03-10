package com.draeger.smartcoffee.adapter.in.web;

import com.draeger.smartcoffee.application.command.ProduceCoffeeCommand;
import com.draeger.smartcoffee.application.command.RefillBeansCommand;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineCommandUseCase;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineQueryUseCase;
import com.draeger.smartcoffee.application.port.in.MachineDto;
import com.draeger.smartcoffee.domain.exception.InsufficientBeansException;
import com.draeger.smartcoffee.domain.exception.OptimisticLockException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/machines")
public class OperationsController {

    private final CoffeeMachineCommandUseCase commandService;
    private final CoffeeMachineQueryUseCase queryService;

    public OperationsController(CoffeeMachineCommandUseCase commandService,
                                CoffeeMachineQueryUseCase queryService) {
        this.commandService = commandService;
        this.queryService = queryService;
    }

    @GetMapping
    public ResponseEntity<List<MachineDto>> getAllMachines() {
        return ResponseEntity.ok(queryService.getAllMachines());
    }

    @PostMapping("/{id}/produce-coffee")
    public ResponseEntity<?> produceCoffee(@PathVariable UUID id,
                                           @RequestBody ProduceCoffeeRequest request) {
        try {
            commandService.produceCoffee(new ProduceCoffeeCommand(id, request.coffeeType(), request.user()));
            return ResponseEntity.ok().build();
        } catch (InsufficientBeansException e) {
            return ResponseEntity.status(409).body(Map.of("error", e.getMessage()));
        } catch (OptimisticLockException e) {
            return ResponseEntity.status(409).body(Map.of("error", e.getMessage(), "hint", "Retry the command"));
        }
    }

    @PostMapping("/{id}/refill")
    public ResponseEntity<?> refillBeans(@PathVariable UUID id,
                                         @RequestBody RefillRequest request) {
        commandService.refillBeans(new RefillBeansCommand(id, request.beansToAdd(), request.user()));
        return ResponseEntity.ok().build();
    }
}
