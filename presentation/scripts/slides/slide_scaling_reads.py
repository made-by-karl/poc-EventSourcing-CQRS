"""Slide — Scaling the read side"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Scaling the read side")

    # ── Left card: Scale out projections (SUCCESS border) ────────────────────
    rect(slide, 0.4, 1.05, 6.0, 3.0, fill=PANEL, line=SUCCESS, lw=Pt(2))
    txt(slide, "Scale out projections", 0.65, 1.15, 5.5, 0.45,
        sz=16, bold=True, col=SUCCESS)
    scale_items = [
        "Read replicas (PostgreSQL streaming replication)",
        "Independent projection instances consuming events",
        "Each projection scales separately from commands",
    ]
    for i, item in enumerate(scale_items):
        txt(slide, f"  •  {item}", 0.65, 1.72 + i * 0.55, 5.5, 0.45,
            sz=14, col=TEXT)

    # ── Right card: Right store for the job (SUCCESS border) ─────────────────
    rect(slide, 6.93, 1.05, 6.0, 3.0, fill=PANEL, line=SUCCESS, lw=Pt(2))
    txt(slide, "Right store for the job", 7.18, 1.15, 5.5, 0.45,
        sz=16, bold=True, col=SUCCESS)
    store_items = [
        "Redis — sub-millisecond dashboards",
        "Elasticsearch — full-text search over events",
        "ClickHouse / TimescaleDB — analytics & time series",
    ]
    for i, item in enumerate(store_items):
        txt(slide, f"  •  {item}", 7.18, 1.72 + i * 0.55, 5.5, 0.45,
            sz=14, col=TEXT)

    # ── Bottom panel: When / Price ───────────────────────────────────────────
    panel_y = 4.35
    # Left card — When?
    rect(slide, 0.4, panel_y, 6.0, 1.65, fill=PANEL, line=BORDER)
    txt(slide, "When?", 0.6, panel_y + 0.08, 5.6, 0.35,
        sz=14, bold=True, col=ACCENT)
    txt(slide, "Read load typically 10–100× write load.\n"
              "Scale reads first — it gives the most\n"
              "performance improvement.",
        0.6, panel_y + 0.48, 5.6, 1.05, sz=12, col=TEXT)

    # Right card — Price
    rect(slide, 6.93, panel_y, 6.0, 1.65, fill=PANEL, line=BORDER)
    txt(slide, "Price", 7.13, panel_y + 0.08, 5.6, 0.35,
        sz=14, bold=True, col=ACCENT)
    txt(slide, "Eventual consistency window grows with\n"
              "more stores. Each new technology =\n"
              "another thing to operate.",
        7.13, panel_y + 0.48, 5.6, 1.05, sz=12, col=TEXT)

    footer(slide,
           "CQRS means reads and writes scale independently")

    notes(slide,
          "The CQRS split is what makes read-side scaling so natural. Each "
          "projection is just a consumer of the event log — you can run "
          "multiple instances, each building a different read model. "
          "PostgreSQL read replicas are the simplest first step: streaming "
          "replication gives you near-zero-lag copies for read queries. "
          "Beyond that, project into the right technology per use case — "
          "Redis for real-time dashboards, Elasticsearch for search, "
          "ClickHouse for analytics. Each projection store can scale "
          "independently. The trade-off: every additional store increases "
          "the eventual consistency window and adds operational burden. "
          "Start with PostgreSQL projections (like our demo), add "
          "specialized stores only when you have a concrete performance "
          "need.")
    return slide
