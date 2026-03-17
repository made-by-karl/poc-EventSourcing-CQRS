"""Slide 09 — Reconstitute: State = Fold over Events"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Current state is just the sum of all past events")

    code(slide,
         "CoffeeMachine machine = CoffeeMachine.reconstitute(events);\n"
         "// replays: MachineRegistered → CoffeeProduced → BeansRefilled → ...\n"
         "// result:  beans = 60 - 10 + 20 - 5 = 65  →  capped at MAX_BEANS",
         0.5, 1.05, 12.3, 1.75, sz=14)

    # Arrow label
    txt(slide, "events  →  fold  →  current state",
        0, 3.05, SW, 0.68,
        sz=24, col=ACCENT, bold=True, align=PP_ALIGN.CENTER)

    # Step cards
    steps = [
        ("1  Start",        "Initialise empty state\n(no DB read needed)"),
        ("2  Apply events", "Mutate in-memory aggregate\nfor each event in order"),
        ("3  Return",       "Aggregate ready for\ncommand handling"),
    ]
    for i, (title, body) in enumerate(steps):
        l = 0.4 + i * 4.265
        card(slide, l, 3.9, 4.0, 2.3, title, body, tsz=15, bsz=13)

    notes(slide,
          "Walk through the fold mentally: start at 60, subtract 10 for espresso, "
          "add 20 for refill. This is literally CoffeeMachine.reconstitute() in the demo. "
          "Open the source after the talk — the method is ~15 lines.")
    return slide
