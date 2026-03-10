package com.draeger.smartcoffee.application.port.out;

import java.util.UUID;

public record SnapshotRecord(
    UUID aggregateId,
    String aggregateType,
    long version,
    String payload        // JSON string
) {}
