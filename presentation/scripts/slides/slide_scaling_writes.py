"""Slide — Scaling the write side"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Scaling the write side")

    # ── Three stacked tiers ──────────────────────────────────────────────────
    tiers = [
        ("Tier 1",
         "Multiple handler instances",
         "Stateless command handlers behind a load balancer.\n"
         "Route by aggregate ID → consistent hashing;\n"
         "optimistic concurrency catches collisions."),
        ("Tier 2",
         "Shard the event store",
         "Partition event store by aggregate ID across databases.\n"
         "Each shard handles a subset of aggregates;\n"
         "no cross-shard transactions needed."),
        ("Tier 3",
         "Event bus as backbone",
         "Kafka / EventStoreDB as primary append log.\n"
         "Ordered partitions per aggregate;\n"
         "consumers project into any read store."),
    ]
    for i, (tier, title, body) in enumerate(tiers):
        y = 1.05 + i * 1.35
        # Tier label
        txt(slide, tier, 0.4, y + 0.18, 1.4, 0.45,
            sz=14, bold=True, col=MUTED)
        # Content card
        rect(slide, 1.9, y, 11.03, 1.15, fill=PANEL, line=ACCENT, lw=Pt(2))
        txt(slide, title, 2.1, y + 0.05, 10.6, 0.4,
            sz=15, bold=True, col=ACCENT)
        txt(slide, body, 2.1, y + 0.45, 10.6, 0.65,
            sz=12, col=TEXT)

    # ── Bottom panel: When / Price ───────────────────────────────────────────
    panel_y = 5.2
    # Left card — When?
    rect(slide, 0.4, panel_y, 6.0, 1.35, fill=PANEL, line=BORDER)
    txt(slide, "When?", 0.6, panel_y + 0.08, 5.6, 0.35,
        sz=14, bold=True, col=ACCENT)
    txt(slide, "Single PostgreSQL handles millions of events/day.\n"
              "You probably don't need sharding yet.",
        0.6, panel_y + 0.48, 5.6, 0.8, sz=12, col=TEXT)

    # Right card — Price
    rect(slide, 6.93, panel_y, 6.0, 1.35, fill=PANEL, line=BORDER)
    txt(slide, "Price", 7.13, panel_y + 0.08, 5.6, 0.35,
        sz=14, bold=True, col=ACCENT)
    txt(slide, "Each tier adds operational complexity.\n"
              "Start with tier 1 — it's often enough.",
        7.13, panel_y + 0.48, 5.6, 0.8, sz=12, col=TEXT)

    footer(slide,
           "Aggregates don't share state — that's what makes this work.")

    notes(slide,
          "Tier 1 is where most teams stay. Stateless command handlers are "
          "trivial to scale — spin up more instances, put a load balancer in "
          "front. Consistent hashing by aggregate ID avoids two instances "
          "handling the same aggregate simultaneously, but if it happens, the "
          "UNIQUE sequence constraint rejects the slower writer (optimistic "
          "concurrency). Tier 2 is rare — you're sharding when a single "
          "Postgres can't keep up with write throughput, which is millions of "
          "events/day. Shard key = aggregate ID, so each aggregate's stream "
          "lives entirely on one shard. No cross-shard joins needed because "
          "you never query across aggregates on the write side. Tier 3 is for "
          "teams that need guaranteed ordering at extreme scale — Kafka "
          "partitions give you per-key ordering with horizontal throughput. "
          "EventStoreDB is purpose-built for this. The honest answer: most "
          "teams never leave tier 1.")
    return slide
