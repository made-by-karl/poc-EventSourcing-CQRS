"""Divider — Event Sourcing"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)

    # Section number
    txt(slide, "Part I", 0, 2.0, SW, 0.7,
        sz=18, col=MUTED, align=PP_ALIGN.CENTER)

    # Section title
    txt(slide, "Event Sourcing", 0, 2.7, SW, 1.2,
        sz=44, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)

    # Accent underline
    rect(slide, 4.5, 3.95, 4.33, 0.08, fill=ACCENT)

    # Subtitle
    txt(slide, "Store what happened, not what is.", 0, 4.3, SW, 0.7,
        sz=20, col=TEXT, italic=True, align=PP_ALIGN.CENTER)

    return slide
