package com.draeger.smartcoffee.domain.exception;

import java.util.UUID;

public class OptimisticLockException extends RuntimeException {
    public OptimisticLockException(UUID machineId, long conflictingVersion) {
        super("Concurrent modification detected for machine " + machineId
            + " at version " + conflictingVersion + ". Retry the command.");
    }
}
