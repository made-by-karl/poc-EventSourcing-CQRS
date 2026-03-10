package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.application.port.in.RebuildResultDto;
import com.draeger.smartcoffee.application.port.out.EventStore;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class ProjectionRebuildService {

    private static final Logger log = LoggerFactory.getLogger(ProjectionRebuildService.class);

    private final JdbcTemplate jdbc;
    private final EventStore eventStore;
    private final ProjectionUpdater projectionUpdater;

    public ProjectionRebuildService(JdbcTemplate jdbc, EventStore eventStore,
                                    ProjectionUpdater projectionUpdater) {
        this.jdbc = jdbc;
        this.eventStore = eventStore;
        this.projectionUpdater = projectionUpdater;
    }

    @Transactional
    public RebuildResultDto rebuildAll() {
        long start = System.currentTimeMillis();
        jdbc.execute("TRUNCATE projection_machine_state, projection_user_stats, projection_double_espresso_log");
        List<DomainEvent> events = eventStore.loadAllEvents();
        events.forEach(projectionUpdater::apply);
        long elapsed = System.currentTimeMillis() - start;
        log.info("Projection rebuild: {} events in {}ms", events.size(), elapsed);
        return new RebuildResultDto(events.size(), elapsed);
    }
}
