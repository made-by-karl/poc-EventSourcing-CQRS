"""Slide 03 — The Traditional Approach: UPDATE in Place"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "The Traditional Approach")

    # Left column label
    txt(slide, "You do this:", 0.4, 1.05, 5.8, 0.42,
        sz=16, col=MUTED, bold=True)
    code(slide,
         "UPDATE machines\nSET beans_available = 45\nWHERE id = 'abc';",
         0.4, 1.52, 5.8, 1.55, sz=15)

    # Arrow
    txt(slide, "→", 6.2, 2.1, 0.9, 0.8,
        sz=36, col=ACCENT, align=PP_ALIGN.CENTER)

    # Right column label
    txt(slide, "The database remembers only this:", 7.13, 1.05, 5.7, 0.42,
        sz=16, col=MUTED, bold=True)
    code(slide,
         "id  | beans_available\nabc |      45",
         7.13, 1.52, 5.7, 1.55, sz=15)

    # "History is gone" panel
    rect(slide, 0.8, 3.35, 11.7, 1.85, fill=PANEL, line=BORDER)
    txt(slide, "Previous values:", 1.1, 3.48, 4.0, 0.42,
        sz=14, col=MUTED, bold=True)
    txt(slide, "beans_available = 60  →  50  →  30  →  45",
        1.1, 3.93, 11.0, 0.55,
        sz=16, col=MUTED, italic=True)
    txt(slide, "✗  History is gone. Every UPDATE destroys the previous value.",
        1.1, 4.52, 11.0, 0.55,
        sz=15, col=DANGER)

    notes(slide,
          "This is perfectly reasonable for most apps. The UPDATE is fast, simple, atomic. "
          "The problem shows up later — when an auditor asks 'who changed this and when?' "
          "The answer is: we don't know. We only know where it ended up.")
    return slide
