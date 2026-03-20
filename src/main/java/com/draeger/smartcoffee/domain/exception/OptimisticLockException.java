package com.draeger.smartcoffee.domain.exception;

import java.util.UUID;

public class OptimisticLockException extends RuntimeException {
    public OptimisticLockException(UUID aggregateId, long conflictingVersion) {
        super("Concurrent modification detected for aggregate " + aggregateId
            + " at version " + conflictingVersion + ". Retry the command.");
    }
}
