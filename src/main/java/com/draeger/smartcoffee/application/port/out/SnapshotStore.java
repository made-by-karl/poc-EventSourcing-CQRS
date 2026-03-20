package com.draeger.smartcoffee.application.port.out;

import com.draeger.smartcoffee.domain.model.CoffeeMachine;

import java.util.Optional;
import java.util.UUID;

public interface SnapshotStore {

    Optional<SnapshotRecord> findLatest(UUID aggregateId);

    void save(SnapshotRecord snapshot);

    /** Checks if delta since last snapshot meets the threshold; saves if so. */
    void maybeSnapshot(CoffeeMachine machine);
}
