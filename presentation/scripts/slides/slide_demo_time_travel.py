"""Slide 17 — Demo 2: Temporal Queries / Time Travel"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Demo 2 — Temporal Queries")

    # Left — query panel
    rect(slide, 0.4, 1.05, 5.8, 5.3, fill=PANEL, line=BORDER)
    txt(slide, "Time Travel Query",
        0.65, 1.15, 5.3, 0.45, sz=15, bold=True, col=ACCENT)
    code(slide,
         "Machine: OR Machine 1\n"
         "At: 2026-03-02T08:00:00Z\n"
         "\n"
         "→  55 beans  (3 events replayed)",
         0.65, 1.72, 5.3, 2.3, sz=14)
    txt(slide, "GET /api/machines/{id}/history?at=...",
        0.65, 4.15, 5.3, 0.48, sz=12, col=MUTED)

    # Right — explanation
    rect(slide, 6.5, 1.05, 6.6, 5.3, fill=PANEL, line=BORDER)
    txt(slide, "How it works:",
        6.75, 1.15, 6.1, 0.45, sz=15, bold=True, col=ACCENT)
    steps = [
        "1.  Load all events for machine",
        "2.  Filter: occurred_at ≤ timestamp",
        "3.  Reconstitute aggregate from filtered list",
        "4.  Return state snapshot",
    ]
    for i, step in enumerate(steps):
        txt(slide, step, 6.75, 1.78 + i * 0.72, 6.1, 0.65, sz=14, col=TEXT)

    # Key insight strip
    rect(slide, 1.0, 6.55, 11.3, 0.5, fill=BORDER, line=ACCENT)
    txt(slide, "No special versioning infrastructure. The event log IS the audit trail.",
        1.2, 6.58, 10.9, 0.44,
        sz=13, col=ACCENT, bold=True, align=PP_ALIGN.CENTER)

    notes(slide,
          "[DEMO] Enter a timestamp from earlier in the session. "
          "Show that the state returned matches what we'd expect from the event history. "
          "No special versioning column needed — just filter by occurred_at.")
    return slide
