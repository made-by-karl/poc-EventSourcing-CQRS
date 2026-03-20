-- Append-only event log with per-aggregate ordering + optimistic concurrency
CREATE TABLE domain_events (
    id              BIGSERIAL    PRIMARY KEY,
    aggregate_id    UUID         NOT NULL,
    sequence_number BIGINT       NOT NULL,
    aggregate_type  VARCHAR(100) NOT NULL,
    event_type      VARCHAR(100) NOT NULL,
    payload         JSONB        NOT NULL,
    occurred_at     TIMESTAMPTZ  NOT NULL,
    CONSTRAINT uq_aggregate_sequence UNIQUE (aggregate_id, sequence_number)
);
CREATE INDEX idx_domain_events_aggregate_id ON domain_events (aggregate_id, sequence_number);
CREATE INDEX idx_domain_events_occurred_at ON domain_events (occurred_at);

-- Current state per machine (bean level + cups produced)
CREATE TABLE projection_machine_state (
    machine_id      UUID         PRIMARY KEY,
    name            VARCHAR(255) NOT NULL,
    beans_available INT          NOT NULL DEFAULT 0,
    cups_produced   INT          NOT NULL DEFAULT 0
);

-- Cup counts per (user, coffee_type) — upserted on each CoffeeProduced
CREATE TABLE projection_user_stats (
    username    VARCHAR(255) NOT NULL,
    coffee_type VARCHAR(50)  NOT NULL,
    cup_count   INT          NOT NULL DEFAULT 0,
    PRIMARY KEY (username, coffee_type)
);

-- Log of DOUBLE_ESPRESSO events for sliding-window caffeine alerts
CREATE TABLE projection_double_espresso_log (
    id          BIGSERIAL    PRIMARY KEY,
    username    VARCHAR(255) NOT NULL,
    occurred_at TIMESTAMPTZ  NOT NULL
);
CREATE INDEX idx_desp_log_user_time ON projection_double_espresso_log (username, occurred_at DESC);
