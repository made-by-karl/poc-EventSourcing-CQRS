"""Slide — Scaling the read side"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Scaling the read side")

    # ── Three stacked tiers ──────────────────────────────────────────────────
    tiers = [
        ("Tier 1",
         "Read replicas",
         "PostgreSQL streaming replication for near-zero-lag copies.\n"
         "Point read-heavy queries at replicas;\n"
         "projections stay on the primary.",
         "Read load is 10–100× write load — this is usually the first bottleneck."),
        ("Tier 2",
         "Independent projection instances",
         "Each projection is a separate event consumer.\n"
         "Scale, redeploy, or rebuild one\n"
         "without touching the others.",
         "When a single projection process can't keep up with the event stream."),
        ("Tier 3",
         "Specialized stores",
         "Redis for sub-ms dashboards, Elasticsearch for full-text search,\n"
         "ClickHouse / TimescaleDB for analytics.",
         "When PostgreSQL projections can't meet latency or query-shape requirements."),
    ]
    for i, (tier, title, body, when) in enumerate(tiers):
        y = 1.05 + i * 1.55
        # Tier label
        txt(slide, tier, 0.4, y + 0.25, 1.4, 0.45,
            sz=14, bold=True, col=MUTED)
        # Content card
        rect(slide, 1.9, y, 11.03, 1.4, fill=PANEL, line=ACCENT, lw=Pt(2))
        txt(slide, title, 2.1, y + 0.05, 10.6, 0.4,
            sz=15, bold=True, col=ACCENT)
        txt(slide, body, 2.1, y + 0.45, 10.6, 0.65,
            sz=12, col=TEXT)
        txt(slide, "↳ " + when, 2.1, y + 1.1, 10.6, 0.25,
            sz=11, italic=True, col=MUTED)

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
