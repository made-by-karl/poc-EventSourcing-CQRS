"""Slide 29 — Thank You / Q&A"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)

    # Large coffee icon
    txt(slide, "☕", 0, 0.9, SW, 2.1,
        sz=88, col=ACCENT, align=PP_ALIGN.CENTER)

    # Gold separator line
    rect(slide, 2.0, 3.1, 9.3, 0.08, fill=ACCENT)

    # Title
    txt(slide, "Facts over State", 0, 3.3, SW, 1.0,
        sz=44, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)

    # Repo link
    txt(slide, "github.com/made-by-karl/poc-EventSourcing-CQRS",
        0, 4.45, SW, 0.65,
        sz=20, col=MUTED, align=PP_ALIGN.CENTER)

    # Questions box
    rect(slide, 4.2, 5.45, 4.9, 0.92, fill=PANEL, line=ACCENT, lw=Pt(2))
    txt(slide, "Questions?", 4.2, 5.5, 4.9, 0.87,
        sz=28, bold=True, col=TEXT, align=PP_ALIGN.CENTER)

    notes(slide,
          "Leave 10–12 minutes for questions.\n\n"
          "Common questions:\n\n"
          "Q: How do you handle schema changes to events?\n"
          "A: Upcasters — functions that transform old event versions to the new schema on read.\n\n"
          "Q: What about deleting user data for GDPR?\n"
          "A: Tombstone events or crypto-shredding — encrypt the payload with a per-user key, "
          "then delete the key.\n\n"
          "Q: Isn't eventual consistency a problem?\n"
          "A: Depends on your SLA. For a coffee machine dashboard, millisecond lag is fine. "
          "For a payment system, you design the write side to be consistent "
          "and the read side to be fast.")
    return slide
