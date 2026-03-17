"""Slide 06 — The Core Insight: Don't store what IS, store what HAPPENED"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Don't store what IS. Store what HAPPENED.")

    # Large contrast panel
    rect(slide, 1.2, 1.2, 10.9, 3.6, fill=PANEL, line=BORDER, lw=Pt(2))

    # Row 1 — gold event fact
    txt(slide,
        "CoffeeProduced  —  DOUBLE_ESPRESSO  —  Dr. Smith  —  09:14:32",
        1.7, 1.55, 9.9, 1.1,
        sz=23, col=ACCENT, bold=True, align=PP_ALIGN.CENTER)

    # Strikethrough overlay line
    rect(slide, 2.5, 2.42, 8.3, 0.07, fill=MUTED)

    # Row 2 — new property value
    txt(slide, "beansConsumed = 20",
        1.7, 2.67, 9.9, 0.9,
        sz=30, col=MUTED, italic=True, align=PP_ALIGN.CENTER)

    # Sub-label
    rect(slide, 3.5, 3.68, 6.3, 0.08, fill=ACCENT)
    txt(slide, "Facts are immutable.  State is derived.",
        0, 3.85, SW, 0.72,
        sz=26, col=TEXT, bold=True, align=PP_ALIGN.CENTER)

    # Tagline
    txt(slide, "This is the entire talk in one slide.",
        0, 5.1, SW, 0.6,
        sz=18, col=MUTED, italic=True, align=PP_ALIGN.CENTER)

    notes(slide,
          "Everything else in this talk is elaborating "
          "on these two sentences. State is ephemeral. Facts are permanent. "
          "ES is making history part of your application domain. "
          "If you remember one thing from today, it's this slide.")
    return slide
