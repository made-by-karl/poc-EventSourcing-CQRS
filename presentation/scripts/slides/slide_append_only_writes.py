"""Slide — Append-only writes: no locks, no contention"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Append-only writes — no locks, no contention")

    # ── Left card: CRUD UPDATE in place (DANGER border) ──────────────────────
    rect(slide, 0.4, 1.05, 5.8, 3.0, fill=PANEL, line=DANGER, lw=Pt(2))
    txt(slide, "CRUD: UPDATE in place", 0.65, 1.15, 5.3, 0.45,
        sz=16, bold=True, col=DANGER)
    crud_items = [
        "Row lock held until COMMIT",
        "Contention on same rows",
        "Random I/O (seek to row)",
        "Dead tuples → VACUUM pressure",
    ]
    for i, item in enumerate(crud_items):
        txt(slide, f"  ✗  {item}", 0.65, 1.72 + i * 0.52, 5.3, 0.45,
            sz=14, col=TEXT)

    # ── Right card: ES INSERT only (SUCCESS border) ──────────────────────────
    rect(slide, 7.13, 1.05, 5.8, 3.0, fill=PANEL, line=SUCCESS, lw=Pt(2))
    txt(slide, "ES: INSERT only", 7.38, 1.15, 5.3, 0.45,
        sz=16, bold=True, col=SUCCESS)
    es_items = [
        "No row locks — append to end",
        "Different aggregates = different rows",
        "Sequential I/O (append to end of table)",
        "No dead tuples → minimal VACUUM",
    ]
    for i, item in enumerate(es_items):
        txt(slide, f"  ✓  {item}", 7.38, 1.72 + i * 0.52, 5.3, 0.45,
            sz=14, col=TEXT)

    # ── Bottom callout ────────────────────────────────────────────────────────
    txt(slide, "Zero dead tuples, almost no VACUUM overhead.",
        0.4, 4.5, 12.53, 0.5, sz=14, bold=True, col=ACCENT)

    footer(slide, "No UPDATEs on the event store. Ever.")

    notes(slide,
          "Compare CRUD row-level locks with ES sequential INSERTs. "
          "Different machines never touch the same rows → zero cross-aggregate contention. "
          "Same-machine races caught by UNIQUE constraint (optimistic lock: retry, don't block). "
          "No UPDATEs also means no dead tuples, so autovacuum is nearly free.")
    return slide
