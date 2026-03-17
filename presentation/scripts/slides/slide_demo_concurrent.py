"""Slide 18 — Demo 3: Optimistic Concurrency"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Demo 3 — Optimistic Concurrency")

    # Race condition diagram
    rect(slide, 0.4, 1.05, 12.5, 2.55, fill=PANEL, line=BORDER)
    txt(slide, "Thread A:", 0.65, 1.15, 2.5, 0.45, sz=15, bold=True, col=TEXT)
    txt(slide, "Thread B:", 0.65, 2.15, 2.5, 0.45, sz=15, bold=True, col=TEXT)
    code(slide,
         "SELECT MAX(seq) = 4   →   INSERT seq=5   →   ✓  200 OK",
         3.1, 1.08, 9.5, 0.72, sz=13)
    code(slide,
         "SELECT MAX(seq) = 4   →   INSERT seq=5   →   ✗  UNIQUE violation",
         3.1, 2.08, 9.5, 0.72, sz=13)

    # Result boxes
    rect(slide, 0.4, 3.85, 6.07, 1.35, fill=PANEL, line=SUCCESS, lw=Pt(2))
    txt(slide, "✓  200 OK",
        0.65, 3.95, 5.57, 0.52, sz=20, bold=True, col=SUCCESS)
    txt(slide, "Write succeeded — event appended",
        0.65, 4.52, 5.57, 0.55, sz=14, col=TEXT)

    rect(slide, 6.87, 3.85, 6.07, 1.35, fill=PANEL, line=DANGER, lw=Pt(2))
    txt(slide, "✗  409 Conflict",
        7.12, 3.95, 5.57, 0.52, sz=20, bold=True, col=DANGER)
    txt(slide, "Concurrent modification at version 5. Retry.",
        7.12, 4.52, 5.57, 0.55, sz=14, col=TEXT)

    footer(slide,
           "UNIQUE(machine_id, sequence_number) IS the lock. No explicit locking code.")
    notes(slide,
          "[DEMO] Click 'Fire Concurrent Writes'. One box goes green, one red. "
          "Refresh domain_events to confirm only one row was inserted. "
          "The UNIQUE constraint does the work — no SELECT FOR UPDATE, no distributed lock.")
    return slide
