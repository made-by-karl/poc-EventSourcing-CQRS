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
    public void append(DomainEvent event) {
        UUID aggregateId = event.getAggregateId();

        // SELECT MAX + 1 is the optimistic version number.
        // The UNIQUE (aggregate_id, sequence_number) constraint is the actual lock:
        // if two writers race for the same aggregate, only one INSERT succeeds;
        // the other gets a constraint violation which we surface as OptimisticLockException.
        // Different aggregates (machine IDs) never contend — each is its own partition.
        Long nextSeq = jdbc.queryForObject(
            "SELECT COALESCE(MAX(sequence_number), -1) + 1 FROM domain_events WHERE aggregate_id = ?",
            Long.class, aggregateId);
        try {
            jdbc.update(
                "INSERT INTO domain_events (aggregate_id, sequence_number, aggregate_type, event_type, payload, occurred_at) VALUES (?, ?, ?, ?, ?::jsonb, ?)",
                aggregateId, nextSeq, event.getAggregateType(), event.getEventType(),
                EventSerializer.serialize(event),
                Timestamp.from(event.getOccurredAt()));
        } catch (DuplicateKeyException e) {
            throw new OptimisticLockException(aggregateId, nextSeq);
        }
        publisher.publishEvent(new EventStoreUpdatedEvent(this, event));
    }

    @Override
    public List<DomainEvent> loadEvents(UUID aggregateId) {
        return jdbc.query(
            "SELECT event_type, payload FROM domain_events WHERE aggregate_id = ? ORDER BY sequence_number",
            (rs, rowNum) -> EventSerializer.deserialize(rs.getString("payload"), rs.getString("event_type")),
            aggregateId);
    }

    @Override
    public List<UUID> getAllAggregateIds() {
        return jdbc.query(
            "SELECT aggregate_id FROM domain_events GROUP BY aggregate_id ORDER BY MIN(id)",
            (rs, rowNum) -> UUID.fromString(rs.getString("aggregate_id")));
    }

    @Override
    public List<DomainEvent> loadAllEvents() {
        return jdbc.query(
            "SELECT event_type, payload FROM domain_events ORDER BY id",
            (rs, rowNum) -> EventSerializer.deserialize(rs.getString("payload"), rs.getString("event_type")));
    }
}
