"""Slide 07a — What is an Aggregate?"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "The Aggregate \u2014 Transactional Boundary")

    # Concrete example callout
    rect(slide, 0.4, 1.05, 10.3, 1.65, fill=PANEL, line=ACCENT, lw=Pt(2))
    txt(slide, "CoffeeMachine aggregate",
        0.6, 1.12, 5.0, 0.42,
        sz=15, bold=True, col=ACCENT)
    txt(slide,
        "Fields:   id  \u00b7  name  \u00b7  beansAvailable\n"
        "Invariant:   0 \u2264 beansAvailable \u2264 MAX_CAPACITY (100)\n"
        "Violation \u2192 InsufficientBeansException  (no event produced)",
        0.6, 1.58, 9.9, 1.0,
        sz=13, col=TEXT, fn=MONO)

    # Three concept cards
    cards = [
        ("Contains entities",
         "An aggregate root can own child\n"
         "entities and value objects.\n\n"
         "The root controls all access \u2014\n"
         "outside code never reaches in."),
        ("Guarantees validity",
         "Every command is validated before\n"
         "an event is produced.\n\n"
         "The aggregate rejects anything that\n"
         "would leave it in an invalid state."),
        ("Transactional scope",
         "All changes within an aggregate are\n"
         "committed atomically.\n\n"
         "One command \u2192 one event \u2192 one\n"
         "transaction. No partial updates."),
    ]
    for i, (title, body) in enumerate(cards):
        l = 0.4 + i * 4.2
        card(slide, l, 2.9, 3.95, 3.2, title, body, tsz=15, bsz=12)

    footer(slide, "One aggregate instance = one consistency boundary.")

    notes(slide,
          "An aggregate is a DDD concept: a cluster of objects treated as a unit "
          "for data changes. In our codebase, CoffeeMachine is the aggregate root.")
    return slide
