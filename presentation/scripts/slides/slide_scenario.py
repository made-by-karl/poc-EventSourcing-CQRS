"""Slide 02 — Opening Scenario"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Monday morning. OR Machine 1 is empty.")

    questions = [
        "Who dispensed the last coffee — and when?",
        "Was the machine refilled last night, and by whom?",
        "At what point did the bean level drop below 10?",
    ]
    for i, q in enumerate(questions):
        y = 1.15 + i * 1.5
        rect(slide, 0.6, y, 12.1, 1.1, fill=PANEL, line=BORDER)
        txt(slide, f"  {i + 1}.  {q}",
            0.75, y + 0.13, 11.8, 0.84,
            sz=22, col=TEXT)

    # Footer callout
    rect(slide, 1.5, 5.75, 10.3, 0.78, fill=BORDER, line=ACCENT, lw=Pt(2))
    txt(slide, "With a traditional database, you can't answer these.",
        1.65, 5.8, 10.0, 0.68,
        sz=19, col=DANGER, bold=True, align=PP_ALIGN.CENTER)

    notes(slide,
          "We've all been in a production incident where the data "
          "has been overwritten and the audit trail is missing. "
          "This is the problem we're solving today.")
    return slide
