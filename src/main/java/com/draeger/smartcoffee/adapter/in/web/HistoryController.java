package com.draeger.smartcoffee.adapter.in.web;

import com.draeger.smartcoffee.application.port.in.CoffeeMachineQueryUseCase;
import com.draeger.smartcoffee.application.port.in.MachineStateAtDto;
import com.draeger.smartcoffee.domain.exception.MachineNotFoundException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.Instant;
import java.time.format.DateTimeParseException;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/machines")
public class HistoryController {

    private final CoffeeMachineQueryUseCase queryService;

    public HistoryController(CoffeeMachineQueryUseCase queryService) {
        this.queryService = queryService;
    }

    @GetMapping("/{id}/history")
    public ResponseEntity<?> getMachineStateAt(@PathVariable UUID id,
                                               @RequestParam("at") String at) {
        Instant asOf;
        try {
            asOf = Instant.parse(at);
        } catch (DateTimeParseException e) {
            return ResponseEntity.badRequest()
                .body(Map.of("error", "Invalid timestamp format. Use ISO-8601, e.g. 2025-03-01T14:00:00Z"));
        }
        try {
            MachineStateAtDto result = queryService.getMachineStateAt(id, asOf);
            return ResponseEntity.ok(result);
        } catch (MachineNotFoundException e) {
            return ResponseEntity.status(404).body(Map.of("error", e.getMessage()));
        }
    }
}
