package com.draeger.smartcoffee.adapter.in.web;

import com.draeger.smartcoffee.application.port.in.BeanLevelDto;
import com.draeger.smartcoffee.application.port.in.CaffeineAlertDto;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineQueryUseCase;
import com.draeger.smartcoffee.application.port.in.UserStatsDto;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/projections")
public class ProjectionController {

    private final CoffeeMachineQueryUseCase queryService;

    public ProjectionController(CoffeeMachineQueryUseCase queryService) {
        this.queryService = queryService;
    }

    @GetMapping("/bean-levels")
    public ResponseEntity<List<BeanLevelDto>> getBeanLevels() {
        return ResponseEntity.ok(queryService.getBeanLevels());
    }

    @GetMapping("/user-stats")
    public ResponseEntity<List<UserStatsDto>> getUserStats() {
        return ResponseEntity.ok(queryService.getUserStats());
    }

    @GetMapping("/caffeine-alerts")
    public ResponseEntity<List<CaffeineAlertDto>> getCaffeineAlerts() {
        return ResponseEntity.ok(queryService.getCaffeineAlerts());
    }
}
