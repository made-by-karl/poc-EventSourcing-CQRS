"""Slide 21 — The domain_events Table"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "One append-only table. Everything else is derived.")

    code(slide,
         "CREATE TABLE domain_events (\n"
         "    id              BIGSERIAL    PRIMARY KEY,\n"
         "    machine_id      UUID         NOT NULL,\n"
         "    sequence_number BIGINT       NOT NULL,\n"
         "    event_type      VARCHAR(100) NOT NULL,\n"
         "    payload         JSONB        NOT NULL,\n"
         "    occurred_at     TIMESTAMPTZ  NOT NULL,\n"
         "    CONSTRAINT uq_machine_sequence\n"
         "        UNIQUE (machine_id, sequence_number)\n"
         ");",
         0.5, 1.05, 12.3, 4.5, sz=14)

    # Callout
    rect(slide, 1.5, 5.75, 10.3, 0.85, fill=BORDER, line=ACCENT, lw=Pt(2))
    txt(slide,
        "UNIQUE(machine_id, sequence_number)  —  the optimistic lock",
        1.7, 5.8, 9.9, 0.75,
        sz=16, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)

    footer(slide, "All events from all types of aggregate go into this table. ")
    notes(slide,
          "This is the entire write model. Everything else — projections, snapshots — "
          "is derived from these rows. "
          "The UNIQUE constraint on (machine_id, sequence_number) "
          "is what prevents concurrent writes from corrupting the stream.")
    return slide
