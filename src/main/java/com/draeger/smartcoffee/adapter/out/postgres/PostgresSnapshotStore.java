package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.application.port.out.SnapshotRecord;
import com.draeger.smartcoffee.application.port.out.SnapshotStore;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;
import tools.jackson.databind.DeserializationFeature;
import tools.jackson.databind.ObjectMapper;
import tools.jackson.databind.json.JsonMapper;

import java.util.Optional;
import java.util.UUID;

@Repository
public class PostgresSnapshotStore implements SnapshotStore {

    private static final Logger log = LoggerFactory.getLogger(PostgresSnapshotStore.class);

    private static final ObjectMapper MAPPER = JsonMapper.builder()
        .disable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES)
        .build();

    private final JdbcTemplate jdbc;

    @Value("${snapshot.threshold:5}")
    private int threshold;

    public PostgresSnapshotStore(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    @Override
    public Optional<SnapshotRecord> findLatest(UUID aggregateId) {
        return jdbc.query(
            "SELECT aggregate_id, aggregate_type, version, payload::text FROM aggregate_snapshots " +
            "WHERE aggregate_id = ? ORDER BY version DESC LIMIT 1",
            (rs, rowNum) -> new SnapshotRecord(
                UUID.fromString(rs.getString("aggregate_id")),
                rs.getString("aggregate_type"),
                rs.getLong("version"),
                rs.getString("payload")),
            aggregateId
        ).stream().findFirst();
    }

    @Override
    public void save(SnapshotRecord snapshot) {
        jdbc.update(
            "INSERT INTO aggregate_snapshots (aggregate_id, aggregate_type, version, payload) " +
            "VALUES (?, ?, ?, ?::jsonb) ON CONFLICT (aggregate_id, version) DO NOTHING",
            snapshot.aggregateId(), snapshot.aggregateType(), snapshot.version(), snapshot.payload());
    }

    @Override
    public void maybeSnapshot(CoffeeMachine machine) {
        UUID machineId = machine.getId();

        long maxSeq = Optional.ofNullable(jdbc.queryForObject(
            "SELECT MAX(sequence_number) FROM domain_events WHERE machine_id = ?",
            Long.class, machineId
        )).orElse(0L);
        long snapVersion = findLatest(machineId).map(SnapshotRecord::version).orElse(0L);
        if (maxSeq - snapVersion >= threshold) {
            try {
                String json = MAPPER.writeValueAsString(
                    new CoffeeMachinePayload(machine.getName(), machine.getBeansAvailable()));
                save(new SnapshotRecord(machineId, "CoffeeMachine", maxSeq, json));
                log.info("Snapshot taken for machine {} at version={}", machineId, maxSeq);
            } catch (Exception e) {
                throw new EventSerializationException("Failed to serialize snapshot for machine: " + machineId, e);
            }
        }
    }
}
