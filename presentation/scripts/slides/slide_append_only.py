"""Slide — Append-only event store: no locks, storage optimized by default"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Append-only — no locks, storage optimized by default")

    # ── Top-left card: CRUD UPDATE in place (DANGER border) ──────────────────
    rect(slide, 0.4, 1.05, 6.07, 2.5, fill=PANEL, line=DANGER, lw=Pt(2))
    txt(slide, "CRUD: UPDATE in place", 0.65, 1.15, 5.57, 0.45,
        sz=16, bold=True, col=DANGER)
    crud_items = [
        "Row locks held until COMMIT",
        "Contention on same rows",
        "Random I/O + dead tuples (VACUUM pressure)",
    ]
    for i, item in enumerate(crud_items):
        txt(slide, f"  \u2717  {item}", 0.65, 1.72 + i * 0.52, 5.57, 0.45,
            sz=14, col=TEXT)

    # ── Top-right card: ES INSERT only (SUCCESS border) ──────────────────────
    rect(slide, 6.87, 1.05, 6.07, 2.5, fill=PANEL, line=SUCCESS, lw=Pt(2))
    txt(slide, "Append-only: INSERT only", 7.12, 1.15, 5.57, 0.45,
        sz=16, bold=True, col=SUCCESS)
    es_items = [
        "No row locks \u2014 append to end",
        "Sequential I/O, no dead tuples",
        "Concurrent writes fail fast, never block",
    ]
    for i, item in enumerate(es_items):
        txt(slide, f"  \u2713  {item}", 7.12, 1.72 + i * 0.52, 5.57, 0.45,
            sz=14, col=TEXT)

    # ── Bottom strip: What append-only unlocks (ACCENT-bordered cards) ───────
    strip_top = 3.85
    card_h = 2.5
    card_w = 6.07
    gap = 0.4
    x0 = 0.4

    # Card 1: BRIN index
    rect(slide, x0, strip_top, card_w, card_h, fill=PANEL, line=ACCENT, lw=Pt(2))
    txt(slide, "BRIN index", x0 + 0.15, strip_top + 0.12, card_w - 0.3, 0.4,
        sz=15, bold=True, col=ACCENT)
    brin_items = [
        "Min/max per block range",
        "~100\u00d7 smaller than B-tree",
        "Timestamps monotonic on disk",
    ]
    for i, item in enumerate(brin_items):
        txt(slide, f"  \u2022  {item}", x0 + 0.15, strip_top + 0.6 + i * 0.45,
            card_w - 0.3, 0.4, sz=13, col=TEXT)

    # Card 2: Time partitioning
    x1 = x0 + card_w + gap
    rect(slide, x1, strip_top, card_w, card_h, fill=PANEL, line=ACCENT, lw=Pt(2))
    txt(slide, "Time partitioning", x1 + 0.15, strip_top + 0.12, card_w - 0.3, 0.4,
        sz=15, bold=True, col=ACCENT)
    part_items = [
        "Cold vs hot data separation",
        "Partition pruning at query time",
        "Smaller indexes stay in memory",
    ]
    for i, item in enumerate(part_items):
        txt(slide, f"  \u2022  {item}", x1 + 0.15, strip_top + 0.6 + i * 0.45,
            card_w - 0.3, 0.4, sz=13, col=TEXT)

    footer(slide, "Append-only is the best case for databases — optimized for both reads and writes.")

    notes(slide,
          "Compare CRUD row-level locks with ES sequential INSERTs. "
          "Different machines never touch the same rows \u2014 zero cross-aggregate contention. "
          "Same-machine races caught by UNIQUE constraint (optimistic lock: retry, don\u2019t block). "
          "No UPDATEs also means no dead tuples, so autovacuum is nearly free.\n\n"
          "BRIN works because append-only tables have perfect physical-to-logical "
          "correlation \u2014 occurred_at increases monotonically, new rows land at the "
          "end of the table, so block ranges map directly to time ranges. B-tree "
          "inserts for monotonic keys always go to the rightmost leaf, but BRIN is "
          "~100\u00d7 smaller in index footprint.\n\n"
          "For partitioning: partition pruning skips entire months at query time. "
          "Cold partitions are still fully queryable \u2014 they\u2019re just skipped when "
          "the WHERE clause doesn\u2019t need them.\n\n"
          "This is a general property of append-only logs. Kafka, Cassandra, "
          "DynamoDB streams all benefit similarly. PostgreSQL BRIN and partitioning "
          "are concrete examples of the broader principle.")
    return slide
