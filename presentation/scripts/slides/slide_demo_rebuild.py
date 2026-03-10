"""Slide 20 — Demo 5: Projection Rebuild"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Demo 5 — Projections are Disposable")

    steps = [
        ("1", "POST /api/admin/projections/rebuild", TEXT,   True),
        ("2", "TRUNCATE projection tables",           DANGER, False),
        ("3", "Replay all events in order",           MUTED,  False),
        ("4", '{ "eventsReplayed": 12, "elapsedMs": 48 }', SUCCESS, True),
    ]
    for i, (num, step, col, use_mono) in enumerate(steps):
        y = 1.15 + i * 1.22
        # Number badge
        rect(slide, 0.5, y, 0.75, 0.85, fill=BORDER, line=ACCENT)
        txt(slide, num, 0.5, y + 0.18, 0.75, 0.52,
            sz=22, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)
        # Step label
        rect(slide, 1.4, y, 11.4, 0.85, fill=PANEL, line=BORDER)
        font_name = MONO if use_mono else FONT
        txt(slide, step, 1.6, y + 0.2, 11.0, 0.55,
            fn=font_name, sz=16, col=col)

    # Key insight
    rect(slide, 1.5, 6.05, 10.3, 0.8, fill=BORDER, line=ACCENT, lw=Pt(2))
    txt(slide, "Events are the source of truth.  Projections are a cache.",
        1.7, 6.1, 9.9, 0.7,
        sz=20, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)

    notes(slide,
          "[DEMO] Hit Rebuild. The dashboard reappears with identical data. "
          "This proves the event log is the canonical state — projections can be thrown away "
          "and recreated at any time without data loss.")
    return slide
