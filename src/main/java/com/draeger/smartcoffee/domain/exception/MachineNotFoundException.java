package com.draeger.smartcoffee.domain.exception;

import java.time.Instant;
import java.util.UUID;

public class MachineNotFoundException extends RuntimeException {

    public MachineNotFoundException(UUID machineId, Instant asOf) {
        super("No events found for machine " + machineId + " at or before " + asOf);
    }
}
