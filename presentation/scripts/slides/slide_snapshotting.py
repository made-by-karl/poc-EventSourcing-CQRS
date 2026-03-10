"""Slide 22 — Snapshotting"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Performance: Don't replay 10,000 events every time")

    # Without snapshot
    rect(slide, 0.4, 1.05, 5.8, 2.25, fill=PANEL, line=DANGER, lw=Pt(2))
    txt(slide, "Without snapshot:", 0.65, 1.15, 5.3, 0.45,
        sz=15, bold=True, col=DANGER)
    txt(slide,
        "Load 10,000 events\n→  replay all\n→  current state\n🐌  slow!",
        0.65, 1.65, 5.3, 1.55, sz=14, col=TEXT)

    # Arrow
    txt(slide, "→", 6.15, 1.9, 0.93, 0.8,
        sz=36, col=MUTED, align=PP_ALIGN.CENTER)

    # With snapshot
    rect(slide, 7.13, 1.05, 5.8, 2.25, fill=PANEL, line=SUCCESS, lw=Pt(2))
    txt(slide, "With snapshot:", 7.38, 1.15, 5.3, 0.45,
        sz=15, bold=True, col=SUCCESS)
    txt(slide,
        "Load snapshot @ v=9995\n→  replay 5 delta events\n→  current state\n⚡  fast!",
        7.38, 1.65, 5.3, 1.55, sz=14, col=TEXT)

    # Config callout
    rect(slide, 2.0, 3.52, 9.3, 0.65, fill=BORDER, line=ACCENT)
    txt(slide,
        "snapshot.threshold=5   →   snapshot every 5 events  (50–500 in production)",
        2.2, 3.57, 8.9, 0.55,
        fn=MONO, sz=13, col=ACCENT, align=PP_ALIGN.CENTER)

    # SQL
    code(slide,
         "SELECT version, payload\n"
         "FROM   aggregate_snapshots\n"
         "WHERE  aggregate_id = ?\n"
         "ORDER  BY version DESC\n"
         "LIMIT  1;\n"
         "\n"
         '-- payload → {"name": "OR Machine 1", "beansAvailable": 45}',
         1.5, 4.35, 10.3, 2.2, sz=13)

    notes(slide,
          "The threshold of 5 is low for demo purposes — you'd see the effect immediately. "
          "Production values of 50–500 are common depending on event size and replay frequency. "
          "Snapshotting is purely a performance optimisation — you can remove it without "
          "affecting correctness.")
    return slide
