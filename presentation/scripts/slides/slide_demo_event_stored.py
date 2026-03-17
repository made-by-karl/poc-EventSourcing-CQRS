"""Slide 16 — Demo 1: Dispense Coffee → Event Stored"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Demo 1 — Commands produce events")

    # Left panel — simulated UI
    rect(slide, 0.4, 1.05, 6.07, 5.3, fill=PANEL, line=BORDER)
    txt(slide, "operations.html — Dispense Panel",
        0.65, 1.15, 5.3, 0.42, sz=12, col=MUTED)
    # Simulated form
    rect(slide, 0.65, 1.68, 5.3, 2.55, fill=BG, line=BORDER)
    txt(slide, "Machine:   OR Machine 1",
        0.85, 1.82, 4.9, 0.42, sz=13, col=TEXT)
    txt(slide, "Type:       DOUBLE_ESPRESSO  ▼",
        0.85, 2.26, 4.9, 0.42, sz=13, col=TEXT)
    txt(slide, "User:        Dr. Smith",
        0.85, 2.7, 4.9, 0.42, sz=13, col=TEXT)
    # Dispense button
    rect(slide, 1.35, 3.25, 3.6, 0.72, fill=ACCENT, line=ACCENT)
    txt(slide, "Dispense Coffee",
        1.35, 3.3, 3.6, 0.62,
        sz=16, bold=True, col=BG, align=PP_ALIGN.CENTER)
    txt(slide, "✓  HTTP 200 — CoffeeProduced",
        0.85, 4.1, 5.0, 0.5, sz=13, col=SUCCESS)

    # Right panel — SQL result
    code(slide,
         "domain_events table\n"
         "─────────────────────────────────────────\n"
         "seq | event_type      | payload (excerpt)\n"
         "────┼─────────────────┼──────────────────\n"
         " 0  | MachineReg...   | { name: OR Machine 1,\n"
         "    |                 |   initialBeans: 60 }\n"
         " 1  | CoffeeProdu...  | { coffeeType: DOUBLE_ESPRESSO,\n"
         "    |                 |   user: Dr.Smith, ... }",
         6.87, 1.05, 6.07, 5.3, sz=11)

    footer(slide, "Every button click = one row appended. Nothing updated. Nothing deleted.")
    notes(slide,
          "[DEMO] Open pgweb at :8081. Dispense a coffee. Refresh domain_events. "
          "Show the appended row. Point out: seq increments, event_type is past tense, "
          "payload is JSONB. The existing row is untouched.")
    return slide
