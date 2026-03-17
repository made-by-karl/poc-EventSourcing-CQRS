package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.application.port.in.BeanLevelDto;
import com.draeger.smartcoffee.application.port.in.CaffeineAlertDto;
import com.draeger.smartcoffee.application.port.in.CoffeeMachineQueryUseCase;
import com.draeger.smartcoffee.application.port.in.MachineDto;
import com.draeger.smartcoffee.application.port.in.MachineStateAtDto;
import com.draeger.smartcoffee.application.port.in.UserStatsDto;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.exception.MachineNotFoundException;
import com.draeger.smartcoffee.domain.model.CoffeeMachine;
import org.springframework.context.annotation.Primary;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.time.Instant;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

@Primary
@Service
public class PostgresQueryService implements CoffeeMachineQueryUseCase {

    private final JdbcTemplate jdbc;

    public PostgresQueryService(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    @Override
    public List<MachineDto> getAllMachines() {
        return jdbc.query(
            "SELECT machine_id, name, beans_available FROM projection_machine_state ORDER BY name",
            (rs, rowNum) -> new MachineDto(
                UUID.fromString(rs.getString("machine_id")),
                rs.getString("name"),
                rs.getInt("beans_available")));
    }

    @Override
    public List<BeanLevelDto> getBeanLevels() {
        return jdbc.query(
            "SELECT machine_id, name, beans_available, cups_produced, last_maintenance FROM projection_machine_state ORDER BY name",
            (rs, rowNum) -> {
                Timestamp ts = rs.getTimestamp("last_maintenance");
                return new BeanLevelDto(
                    UUID.fromString(rs.getString("machine_id")),
                    rs.getString("name"),
                    rs.getInt("beans_available"),
                    rs.getInt("cups_produced"),
                    ts != null ? ts.toInstant() : null);
            });
    }

    @Override
    public List<UserStatsDto> getUserStats() {
        List<Map<String, Object>> rows = jdbc.queryForList(
            "SELECT username, coffee_type, cup_count FROM projection_user_stats ORDER BY username, coffee_type");

        Map<String, Map<String, Integer>> statsMap = new HashMap<>();
        for (Map<String, Object> row : rows) {
            String user = (String) row.get("username");
            String type = (String) row.get("coffee_type");
            int count = ((Number) row.get("cup_count")).intValue();
            statsMap.computeIfAbsent(user, k -> new HashMap<>()).put(type, count);
        }

        return statsMap.entrySet().stream()
            .map(entry -> {
                int total = entry.getValue().values().stream().mapToInt(Integer::intValue).sum();
                return new UserStatsDto(entry.getKey(), total, entry.getValue());
            })
            .toList();
    }

    @Override
    public List<CaffeineAlertDto> getCaffeineAlerts() {
        return jdbc.query(
            "SELECT username, COUNT(*) AS cnt FROM projection_double_espresso_log " +
            "WHERE occurred_at > NOW() - INTERVAL '2 hours' " +
            "GROUP BY username HAVING COUNT(*) >= 3",
            (rs, rowNum) -> new CaffeineAlertDto(
                rs.getString("username"),
                rs.getInt("cnt")));
    }

    @Override
    public MachineStateAtDto getMachineStateAt(UUID machineId, Instant asOf) {
        List<DomainEvent> events = jdbc.query(
            "SELECT event_type, payload FROM domain_events " +
            "WHERE machine_id = ? AND occurred_at <= ? ORDER BY sequence_number",
            (rs, n) -> EventSerializer.deserialize(rs.getString("payload"), rs.getString("event_type")),
            machineId, Timestamp.from(asOf));
        if (events.isEmpty()) {
            throw new MachineNotFoundException(machineId, asOf);
        }
        CoffeeMachine machine = CoffeeMachine.reconstitute(events);
        return new MachineStateAtDto(machineId, machine.getName(), machine.getBeansAvailable(), machine.getLastMaintenance(), asOf, events.size());
    }
}
