"""Slide 04 — What Gets Lost"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "State tells you what IS. Not what happened.")

    cards_data = [
        ("No history",
         "Previous values are overwritten forever. "
         "There is no 'undo' without extra infrastructure."),
        ("No audit",
         "'Who changed this?' requires a separate audit log — "
         "bolted on as an afterthought."),
        ("Temporal blindness",
         "'What did the system look like at 9 am?' is unanswerable "
         "from a current-state database."),
        ("One model for everything",
         "The schema is optimised for neither fast writes nor "
         "complex dashboard queries."),
    ]
    positions = [(0.4, 1.05), (6.95, 1.05), (0.4, 3.85), (6.95, 3.85)]
    for (l, t), (title, body) in zip(positions, cards_data):
        card(slide, l, t, 6.4, 2.55, title, body, tsz=17, bsz=13)

    notes(slide,
          "Teams fight these symptoms constantly: soft deletes, created_at/updated_at, "
          "separate audit_log tables. Each is a workaround for the same root cause: "
          "the data model discards history. "
          "Event Sourcing doesn't bolt on audit — audit IS the primary model.")
    return slide
