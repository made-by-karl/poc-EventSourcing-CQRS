package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.domain.event.BeansRefilled;
import com.draeger.smartcoffee.domain.event.CoffeeProduced;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.event.MachineRegistered;
import com.draeger.smartcoffee.domain.model.CoffeeType;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.event.TransactionPhase;
import org.springframework.transaction.event.TransactionalEventListener;

import java.sql.Timestamp;

@Component
public class ProjectionUpdater {

    private final JdbcTemplate jdbc;

    public ProjectionUpdater(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    @TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void on(DomainEventPublishedEvent wrapper) {
        apply(wrapper.getDomainEvent());
    }

    /** Package-private — also called by ProjectionRebuildService during replay. */
    void apply(DomainEvent event) {
        switch (event) {
            case MachineRegistered e -> jdbc.update(
                "INSERT INTO projection_machine_state (machine_id, name, beans_available, cups_produced) VALUES (?, ?, ?, 0) " +
                "ON CONFLICT (machine_id) DO UPDATE SET name = EXCLUDED.name, beans_available = EXCLUDED.beans_available",
                e.getMachineId(), e.getName(), e.getInitialBeans());
            case CoffeeProduced e -> {
                jdbc.update(
                    "UPDATE projection_machine_state SET beans_available = ?, cups_produced = cups_produced + 1 WHERE machine_id = ?",
                    e.getBeansAvailableAfter(), e.getMachineId());
                jdbc.update(
                    "INSERT INTO projection_user_stats (username, coffee_type, cup_count) VALUES (?, ?, 1) ON CONFLICT (username, coffee_type) DO UPDATE SET cup_count = projection_user_stats.cup_count + 1",
                    e.getUser(), e.getCoffeeType().name());
                if (e.getCoffeeType() == CoffeeType.DOUBLE_ESPRESSO) {
                    jdbc.update(
                        "INSERT INTO projection_double_espresso_log (username, occurred_at) VALUES (?, ?)",
                        e.getUser(), Timestamp.from(e.getOccurredAt()));
                }
            }
            case BeansRefilled e -> jdbc.update(
                "UPDATE projection_machine_state SET beans_available = ? WHERE machine_id = ?",
                e.getBeansAvailableAfter(), e.getMachineId());
            case null, default -> {
            }
        }
    }
}
