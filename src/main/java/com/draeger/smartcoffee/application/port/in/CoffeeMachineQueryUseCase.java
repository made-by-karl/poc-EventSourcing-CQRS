package com.draeger.smartcoffee.application.port.in;

import java.time.Instant;
import java.util.List;
import java.util.UUID;

public interface CoffeeMachineQueryUseCase {

    List<MachineDto> getAllMachines();

    List<BeanLevelDto> getBeanLevels();

    List<UserStatsDto> getUserStats();

    List<CaffeineAlertDto> getCaffeineAlerts();

    MachineStateAtDto getMachineStateAt(UUID machineId, Instant asOf);
}
