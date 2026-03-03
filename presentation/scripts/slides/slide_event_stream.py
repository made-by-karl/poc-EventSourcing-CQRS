"""Slide 08 — The Event Stream"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Each aggregate owns an ordered stream of events")

    # Lane label
    txt(slide, "OR Machine 1  —  event stream",
        0.5, 1.0, 12.3, 0.48,
        sz=15, col=MUTED, bold=True)

    # Timeline rail
    rect(slide, 0.6, 1.82, 12.1, 0.06, fill=BORDER)

    # Events
    events = [
        ("seq 0", "MachineRegistered", "60 beans initial"),
        ("seq 1", "CoffeeProduced",    "ESPRESSO / Dr. Smith"),
        ("seq 2", "BeansRefilled",     "+20 beans"),
        ("seq 3", "CoffeeProduced",    "AMERICANO / Dr. Lee"),
    ]
    for i, (seq, etype, detail) in enumerate(events):
        l = 0.6 + i * 3.1
        # Dot on timeline
        rect(slide, l + 1.2, 1.6, 0.45, 0.45, fill=ACCENT, line=ACCENT)
        # Card below timeline
        rect(slide, l, 2.1, 2.9, 2.1, fill=PANEL, line=BORDER)
        txt(slide, seq,   l + 0.1, 2.16, 2.7, 0.38, sz=12, col=MUTED)
        txt(slide, etype, l + 0.1, 2.55, 2.7, 0.45, sz=14, col=ACCENT, bold=True)
        txt(slide, detail, l + 0.1, 3.02, 2.7, 0.95, sz=12, col=TEXT)

    # Arrow label
    txt(slide, "events  →  fold  →  current state",
        0, 4.4, SW, 0.68,
        sz=24, col=ACCENT, bold=True, align=PP_ALIGN.CENTER)
        
    # Bean calculation
    rect(slide, 1.5, 5.0, 10.3, 0.78, fill=PANEL, line=BORDER)
    txt(slide,
        "beans = 60 (registered) − 10 (espresso) + 20 (refill) − 5 (americano) = 65",
        1.7, 5.07, 9.9, 0.62,
        sz=15, col=TEXT, align=PP_ALIGN.CENTER)

    footer(slide, "Sequence numbers are monotonic and immutable.")
    notes(slide,
          "'Aggregate' just means 'the thing that owns the stream'. "
          "One coffee machine = one aggregate = one ordered event stream. "
          "Sequence numbers are the backbone of optimistic concurrency — "
          "we'll see that in demo 3.")
    return slide
