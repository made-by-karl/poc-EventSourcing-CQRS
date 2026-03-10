-- Periodic snapshots of aggregate state to avoid full event replay.
-- version = sequence_number of the last domain_event included in this snapshot.
-- Delta loading: SELECT ... WHERE sequence_number > snapshot.version
CREATE TABLE aggregate_snapshots (
    id             BIGSERIAL    PRIMARY KEY,
    aggregate_id   UUID         NOT NULL,
    aggregate_type VARCHAR(255) NOT NULL,
    version        BIGINT       NOT NULL,
    payload        JSONB        NOT NULL,
    taken_at       TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_snapshot_aggregate_version UNIQUE (aggregate_id, version)
);
CREATE INDEX idx_snapshots_aggregate_id ON aggregate_snapshots (aggregate_id, version DESC);
