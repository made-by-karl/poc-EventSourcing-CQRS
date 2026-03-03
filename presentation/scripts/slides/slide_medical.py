"""Slide 05 — The Cost in a Medical Context"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "In regulated environments, audit is not optional")

    bullets = [
        ("Compliance",
         "Regulations require a complete, tamper-evident change log. "
         "An overwrite-in-place model cannot satisfy this."),
        ("Root-cause analysis",
         "'What state was the system in when the alert fired?' "
         "needs a temporal record, not just the current state."),
        ("Distributed debugging",
         "Without a timeline of events, diagnosing failures "
         "across services is pure guesswork."),
    ]
    for i, (title, body) in enumerate(bullets):
        y = 1.2 + i * 1.65
        rect(slide, 0.6, y, 12.1, 1.4, fill=PANEL, line=BORDER)
        txt(slide, title, 0.85, y + 0.1, 3.5, 0.48,
            sz=17, bold=True, col=ACCENT)
        txt(slide, body, 0.85, y + 0.6, 11.0, 0.72,
            sz=14, col=TEXT, wrap=True)

    notes(slide,
          "The coffee machine demo is deliberately low-stakes and relatable. "
          "But every principle here applies to an EHR system, a financial ledger, "
          "or a logistics platform. The audit requirement is a first-class constraint.")
    return slide
