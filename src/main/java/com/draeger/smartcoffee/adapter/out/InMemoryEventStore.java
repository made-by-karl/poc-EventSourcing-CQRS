package com.draeger.smartcoffee.adapter.out;
import com.draeger.smartcoffee.application.port.out.EventStore;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import tools.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import java.util.Collections;
import java.util.List;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;
@Component
public class InMemoryEventStore implements EventStore {
    private static final Logger log = LoggerFactory.getLogger(InMemoryEventStore.class);
    private final ConcurrentHashMap<UUID, List<DomainEvent>> eventsByMachine = new ConcurrentHashMap<>();
    private final List<DomainEvent> allEvents = new CopyOnWriteArrayList<>();
    private final ObjectMapper objectMapper = new ObjectMapper();

    public InMemoryEventStore() {
    }
    @Override
    public void append(UUID machineId, DomainEvent event) {
        eventsByMachine.computeIfAbsent(machineId, k -> new CopyOnWriteArrayList<>()).add(event);
        allEvents.add(event);
        try {
            String json = objectMapper.writeValueAsString(event);
            log.info("EVENT: {}", json);
        } catch (Exception e) {
            log.warn("Could not serialize event to JSON", e);
        }
    }
    @Override
    public List<DomainEvent> loadEvents(UUID machineId) {
        return Collections.unmodifiableList(
            eventsByMachine.getOrDefault(machineId, List.of())
        );
    }
    @Override
    public List<DomainEvent> loadAllEvents() {
        return Collections.unmodifiableList(allEvents);
    }
    @Override
    public List<UUID> getAllMachineIds() {
        return List.copyOf(eventsByMachine.keySet());
    }
}
