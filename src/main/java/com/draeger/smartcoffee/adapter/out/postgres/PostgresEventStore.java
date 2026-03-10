package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.application.port.out.EventStore;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.exception.OptimisticLockException;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.context.annotation.Primary;
import org.springframework.dao.DuplicateKeyException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.sql.Timestamp;
import java.util.List;
import java.util.UUID;

@Primary
@Repository
public class PostgresEventStore implements EventStore {

    private final JdbcTemplate jdbc;
    private final ApplicationEventPublisher publisher;

    public PostgresEventStore(JdbcTemplate jdbc, ApplicationEventPublisher publisher) {
        this.jdbc = jdbc;
        this.publisher = publisher;
    }

    @Override
    @Transactional
    public void append(UUID machineId, DomainEvent event) {
        // SELECT MAX + 1 is the optimistic version number.
        // The UNIQUE (machine_id, sequence_number) constraint is the actual lock:
        // if two writers race for the same aggregate, only one INSERT succeeds;
        // the other gets a constraint violation which we surface as OptimisticLockException.
        // Different aggregates (machine IDs) never contend — each is its own partition.
        Long nextSeq = jdbc.queryForObject(
            "SELECT COALESCE(MAX(sequence_number), -1) + 1 FROM domain_events WHERE machine_id = ?",
            Long.class, machineId);
        try {
            jdbc.update(
                "INSERT INTO domain_events (machine_id, sequence_number, event_type, payload, occurred_at) VALUES (?, ?, ?, ?::jsonb, ?)",
                machineId, nextSeq, event.getEventType(),
                EventSerializer.serialize(event),
                Timestamp.from(event.getOccurredAt()));
        } catch (DuplicateKeyException e) {
            throw new OptimisticLockException(machineId, nextSeq);
        }
        publisher.publishEvent(new EventStoreUpdatedEvent(this, event));
    }

    @Override
    public List<DomainEvent> loadEvents(UUID machineId) {
        return jdbc.query(
            "SELECT event_type, payload FROM domain_events WHERE machine_id = ? ORDER BY sequence_number",
            (rs, rowNum) -> EventSerializer.deserialize(rs.getString("payload"), rs.getString("event_type")),
            machineId);
    }

    @Override
    public List<UUID> getAllMachineIds() {
        return jdbc.query(
            "SELECT machine_id FROM domain_events GROUP BY machine_id ORDER BY MIN(id)",
            (rs, rowNum) -> UUID.fromString(rs.getString("machine_id")));
    }

    @Override
    public List<DomainEvent> loadAllEvents() {
        return jdbc.query(
            "SELECT event_type, payload FROM domain_events ORDER BY id",
            (rs, rowNum) -> EventSerializer.deserialize(rs.getString("payload"), rs.getString("event_type")));
    }
}
