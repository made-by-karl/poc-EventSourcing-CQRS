package com.draeger.smartcoffee.adapter.out.memory;

import com.draeger.smartcoffee.application.port.in.BeanLevelDto;
import com.draeger.smartcoffee.application.port.in.CaffeineAlertDto;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineQueryUseCase;
import com.draeger.smartcoffee.application.port.in.MachineDto;
import com.draeger.smartcoffee.application.port.in.MachineStateAtDto;
import com.draeger.smartcoffee.application.port.in.UserStatsDto;
import com.draeger.smartcoffee.application.port.out.CoffeeMachineRepository;
import com.draeger.smartcoffee.application.port.out.EventStore;
import com.draeger.smartcoffee.domain.event.CoffeeProduced;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.exception.MachineNotFoundException;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;
import com.draeger.smartcoffee.domain.model.CoffeeType;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class InMemoryCoffeeMachineQueryService implements CoffeeMachineQueryUseCase {

    private final EventStore eventStore;
    private final CoffeeMachineRepository repository;

    public InMemoryCoffeeMachineQueryService(EventStore eventStore, CoffeeMachineRepository repository) {
        this.eventStore = eventStore;
        this.repository = repository;
    }

    @Override
    public List<MachineDto> getAllMachines() {
        return eventStore.getAllMachineIds().stream()
            .map(id -> {
                CoffeeMachine machine = repository.load(id);
                return new MachineDto(id, machine.getName(), machine.getBeansAvailable());
            })
            .toList();
    }

    @Override
    public List<BeanLevelDto> getBeanLevels() {
        return eventStore.getAllMachineIds().stream()
            .map(id -> {
                List<DomainEvent> events = eventStore.loadEvents(id);
                CoffeeMachine machine = CoffeeMachine.reconstitute(events);
                int cupsProduced = (int) events.stream()
                    .filter(e -> e instanceof CoffeeProduced)
                    .count();
                return new BeanLevelDto(id, machine.getName(), machine.getBeansAvailable(), cupsProduced);
            })
            .toList();
    }

    @Override
    public List<UserStatsDto> getUserStats() {
        List<DomainEvent> allEvents = eventStore.loadAllEvents();
        Map<String, Map<String, Integer>> statsMap = new HashMap<>();

        for (DomainEvent event : allEvents) {
            if (event instanceof CoffeeProduced e) {
                Map<String, Integer> byType = statsMap.computeIfAbsent(e.getUser(), k -> new HashMap<>());
                byType.merge(e.getCoffeeType().name(), 1, Integer::sum);
            }
        }

        return statsMap.entrySet().stream()
            .map(entry -> {
                Map<String, Integer> byType = entry.getValue();
                int total = byType.values().stream().mapToInt(Integer::intValue).sum();
                return new UserStatsDto(entry.getKey(), total, byType);
            })
            .toList();
    }

    @Override
    public List<CaffeineAlertDto> getCaffeineAlerts() {
        Instant twoHoursAgo = Instant.now().minus(2, ChronoUnit.HOURS);

        Map<String, Long> counts = eventStore.loadAllEvents().stream()
            .filter(e -> e instanceof CoffeeProduced cp
                && cp.getCoffeeType() == CoffeeType.DOUBLE_ESPRESSO
                && cp.getOccurredAt().isAfter(twoHoursAgo))
            .map(e -> ((CoffeeProduced) e).getUser())
            .collect(Collectors.groupingBy(u -> u, Collectors.counting()));

        return counts.entrySet().stream()
            .filter(entry -> entry.getValue() >= 3)
            .map(entry -> new CaffeineAlertDto(entry.getKey(), entry.getValue().intValue()))
            .toList();
    }

    @Override
    public MachineStateAtDto getMachineStateAt(UUID machineId, Instant asOf) {
        List<DomainEvent> events = eventStore.loadEvents(machineId).stream()
            .filter(e -> !e.getOccurredAt().isAfter(asOf))
            .toList();
        if (events.isEmpty()) {
            throw new MachineNotFoundException(machineId, asOf);
        }
        CoffeeMachine machine = CoffeeMachine.reconstitute(events);
        return new MachineStateAtDto(machineId, machine.getName(), machine.getBeansAvailable(), asOf, events.size());
    }
}
