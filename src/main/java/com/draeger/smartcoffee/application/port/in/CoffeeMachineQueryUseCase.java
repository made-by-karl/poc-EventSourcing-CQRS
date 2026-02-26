package com.draeger.smartcoffee.application.port.in;

import java.util.List;

public interface CoffeeMachineQueryUseCase {

    List<MachineDto> getAllMachines();

    List<BeanLevelDto> getBeanLevels();

    List<UserStatsDto> getUserStats();

    List<CaffeineAlertDto> getCaffeineAlerts();
}
