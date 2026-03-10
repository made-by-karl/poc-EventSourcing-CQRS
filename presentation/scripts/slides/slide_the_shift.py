"""Slide 28 — Closing: The Shift"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, '"What is the state?" → "What happened?"')

    outcomes = [
        ("Auditability",
         "Every change is a named,\ntimestamped, immutable fact.\n\n"
         "Compliance comes for free."),
        ("Scalability",
         "Reads and writes scale\nindependently.\n\n"
         "Aggregates partition naturally."),
        ("Temporal power",
         "Time travel, replay,\nretroactive projections.\n\n"
         "History is first-class."),
    ]
    for i, (title, body) in enumerate(outcomes):
        l = 0.5 + i * 4.3
        rect(slide, l, 1.05, 4.0, 4.55, fill=PANEL, line=ACCENT, lw=Pt(2))
        txt(slide, title, l + 0.1, 1.18, 3.8, 0.52,
            sz=18, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)
        rect(slide, l + 0.3, 1.8, 3.4, 0.07, fill=BORDER)
        txt(slide, body, l + 0.1, 1.95, 3.8, 3.5,
            sz=14, col=TEXT, wrap=True, align=PP_ALIGN.CENTER)

    # Tagline
    rect(slide, 0.5, 5.78, 12.3, 0.08, fill=ACCENT)
    txt(slide,
        "Event Sourcing doesn't add history. It stops throwing it away.",
        0, 5.95, SW, 0.75,
        sz=22, bold=True, col=TEXT, align=PP_ALIGN.CENTER)

    notes(slide,
          "It's the takeaway. "
          "We didn't add a feature called 'history'. "
          "We changed the storage model so that history is preserved by default. "
          "That single shift unlocks auditability, scalability, and temporal queries.")
    return slide
