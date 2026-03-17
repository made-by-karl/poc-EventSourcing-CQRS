package com.draeger.smartcoffee.application.port.in;

import java.time.Instant;
import java.util.UUID;

public record MachineStateAtDto(
    UUID machineId,
    String name,
    int beansAvailable,
    Instant lastMaintenance,
    Instant asOf,
    int eventsReplayed
) {}
