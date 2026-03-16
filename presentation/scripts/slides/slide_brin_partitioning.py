"""Slide — Keeping the event store fast at scale (BRIN + partitioning)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Keeping the event store fast at scale")

    # ── Left card: BRIN index (ACCENT border) ──────────────────────────────
    rect(slide, 0.4, 1.05, 5.8, 2.8, fill=PANEL, line=ACCENT, lw=Pt(2))
    txt(slide, "BRIN index", 0.65, 1.15, 5.3, 0.45,
        sz=16, bold=True, col=ACCENT)
    brin_items = [
        "Stores min/max per block range, not per row",
        "~100× smaller than B-tree",
        "Perfect fit: occurred_at is monotonic on disk",
    ]
    for i, item in enumerate(brin_items):
        txt(slide, f"  •  {item}", 0.65, 1.72 + i * 0.52, 5.3, 0.45,
            sz=14, col=TEXT)

    # ── Right card: Partition by month (ACCENT border) ─────────────────────
    rect(slide, 7.13, 1.05, 5.8, 2.8, fill=PANEL, line=ACCENT, lw=Pt(2))
    txt(slide, "Partition by month", 7.38, 1.15, 5.3, 0.45,
        sz=16, bold=True, col=ACCENT)
    part_items = [
        "Old months = cold data, new partition in cache",
        "Partition pruning skips irrelevant months",
        "Smaller per-partition indexes stay in memory",
    ]
    for i, item in enumerate(part_items):
        txt(slide, f"  •  {item}", 7.38, 1.72 + i * 0.52, 5.3, 0.45,
            sz=14, col=TEXT)


    footer(slide, "Append-only tables are the best case for PostgreSQL storage.")

    notes(slide,
          "BRIN works because append-only tables have perfect physical-to-logical "
          "correlation — occurred_at increases monotonically, new rows land at the "
          "end of the table, so block ranges map directly to time ranges. B-tree "
          "inserts for monotonic keys always go to the rightmost leaf (no random "
          "page splits), but BRIN is ~100× smaller in index footprint. "
          "For partitioning: partition pruning skips entire months at query time. "
          "Cold partitions are still fully queryable — they're just skipped when "
          "the WHERE clause doesn't need them.")
    return slide
