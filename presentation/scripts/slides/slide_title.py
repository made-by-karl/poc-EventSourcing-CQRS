"""Slide 01 — Title: Facts over State"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)

    # Large coffee icon panel
    rect(slide, 5.5, 0.4, 2.3, 2.2, fill=PANEL, line=BORDER)
    txt(slide, "☕", 5.5, 0.45, 2.3, 1.9, sz=72, align=PP_ALIGN.CENTER, col=ACCENT)

    # Gold accent line beneath icon
    rect(slide, 1.5, 2.85, 10.3, 0.07, fill=ACCENT)

    # Main title
    txt(slide, "Facts over State", 0, 3.05, SW, 1.1,
        sz=52, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)

    # Subtitle
    txt(slide,
        "Designing Auditable, Scalable Systems\nwith Event Sourcing and Command Query Responsibility Segregation",
        1.0, 4.25, 11.33, 1.0,
        sz=22, col=TEXT, align=PP_ALIGN.CENTER)

    # Bottom strip — speaker / conference / date
    rect(slide, 0, 6.65, SW, 0.85, fill=PANEL)
    txt(slide, "[ Karl Rhenius ]   |   [ 7. Dräger Developer Day ]   |   [ 2026-03-18 ]",
        0.5, 6.72, SW - 1.0, 0.7,
        sz=14, col=MUTED, align=PP_ALIGN.CENTER)

    notes(slide,
          "Welcome everyone. I'm Karl. Today we have 45 minutes to explore "
          "Event Sourcing and Command Query Responsibility Segregation. "
          "We'll use a running demo app that models coffee machines in a "
          "hospital operating room.")
    return slide
