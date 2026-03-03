"""Divider — Performance & Scaling"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)

    # Section number
    txt(slide, "Part III", 0, 2.0, SW, 0.7,
        sz=18, col=MUTED, align=PP_ALIGN.CENTER)

    # Section title
    txt(slide, "Performance & Scaling", 0, 2.7, SW, 1.2,
        sz=44, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)

    # Accent underline
    rect(slide, 4.5, 3.95, 4.33, 0.08, fill=ACCENT)

    # Subtitle
    txt(slide, "Making it fast and keeping it fast.", 0, 4.3, SW, 0.7,
        sz=20, col=TEXT, italic=True, align=PP_ALIGN.CENTER)

    notes(slide,
          "That was the 'CQRS' section. We saw how the read and write sides of our application have different data models, optimized for their specific workloads. "
          "CQRS gives us a lot of benefits — scalability, flexibility, separation of concerns, and more. "
          "But it also introduces new challenges around performance and consistency. "
          "So let's move on to 'Performance & Scaling'.")
    return slide
