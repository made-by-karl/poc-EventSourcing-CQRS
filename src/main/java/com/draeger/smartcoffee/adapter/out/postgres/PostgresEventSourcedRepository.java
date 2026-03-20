package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.application.port.out.CoffeeMachineRepository;
import com.draeger.smartcoffee.application.port.out.EventStore;
import com.draeger.smartcoffee.application.port.out.SnapshotRecord;
import com.draeger.smartcoffee.application.port.out.SnapshotStore;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.event.MachineRegistered;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Primary;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;
import tools.jackson.databind.DeserializationFeature;
import tools.jackson.databind.ObjectMapper;
import tools.jackson.databind.json.JsonMapper;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Primary
@Repository
public class PostgresEventSourcedRepository implements CoffeeMachineRepository {

    private static final Logger log = LoggerFactory.getLogger(PostgresEventSourcedRepository.class);

    private static final ObjectMapper MAPPER = JsonMapper.builder()
        .disable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES)
        .build();

    private final EventStore eventStore;
    private final SnapshotStore snapshotStore;
    private final JdbcTemplate jdbc;

    public PostgresEventSourcedRepository(EventStore eventStore, SnapshotStore snapshotStore, JdbcTemplate jdbc) {
        this.eventStore = eventStore;
        this.snapshotStore = snapshotStore;
        this.jdbc = jdbc;
    }

    @Override
    public CoffeeMachine create(MachineRegistered event) {
        eventStore.append(event);
        CoffeeMachine machine = CoffeeMachine.reconstitute(List.of(event));
        return machine;
    }

    @Override
    public CoffeeMachine load(UUID aggregateId) {
        Optional<SnapshotRecord> snap = snapshotStore.findLatest(aggregateId);
        if (snap.isPresent()) {
            List<DomainEvent> deltaEvents = jdbc.query(
                "SELECT event_type, payload FROM domain_events " +
                "WHERE aggregate_id = ? AND sequence_number > ? ORDER BY sequence_number",
                (rs, n) -> EventSerializer.deserialize(rs.getString("payload"), rs.getString("event_type")),
                aggregateId, snap.get().version());

            try {
                CoffeeMachinePayload p = MAPPER.readValue(snap.get().payload(), CoffeeMachinePayload.class);
                CoffeeMachine machine = CoffeeMachine.fromSnapshot(
                    snap.get().aggregateId(),
                    p.name(),
                    p.beansAvailable(),
                    p.lastMaintenance(),
                    deltaEvents);
                log.info("Loaded machine {} from snapshot@v={}, replayed {} delta events",
                    aggregateId, snap.get().version(), deltaEvents.size());
                return machine;
            } catch (Exception e) {
                throw new EventSerializationException("Failed to deserialize snapshot payload for machine: " + aggregateId, e);
            }
        } else {
            List<DomainEvent> all = eventStore.loadEvents(aggregateId);
            log.info("Loaded machine {} by full replay of {} events", aggregateId, all.size());
            return CoffeeMachine.reconstitute(all);
        }
    }

    @Override
    public boolean exists(UUID aggregateId) {
        Integer count = jdbc.queryForObject(
            "SELECT COUNT(1) FROM domain_events WHERE aggregate_id = ?",
            Integer.class,
            aggregateId);
        return count != null && count > 0;
    }

    @Override
    public void update(CoffeeMachine machine, DomainEvent event) {
        eventStore.append(event);
        snapshotStore.maybeSnapshot(machine);
    }
}
