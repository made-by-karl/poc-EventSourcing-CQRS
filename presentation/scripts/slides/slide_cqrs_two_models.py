"""Slide 11 — CQRS: Two Models"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Command Query Responsibility Segregation")

    # Write side panel
    rect(slide, 0.4, 1.05, 5.8, 5.35, fill=PANEL, line=BORDER)
    txt(slide, "COMMANDS (Write)", 0.65, 1.15, 5.3, 0.48,
        sz=17, col=ACCENT, bold=True)
    write_items = [
        ("ProduceCoffeeCommand", ACCENT, True),
        ("  ↓",                  MUTED,  False),
        ("CoffeeMachine.handle()", ACCENT, True),
        ("  ↓",                  MUTED,  False),
        ("CoffeeProduced (event)", ACCENT, True),
        ("  ↓",                  MUTED,  False),
        ("EventStore.append()",   ACCENT, True),
    ]
    for i, (label, col, bold) in enumerate(write_items):
        txt(slide, label, 0.65, 1.75 + i * 0.6, 5.3, 0.55,
            sz=14, col=col, bold=bold)

    # Connector
    txt(slide, "⇄", 6.1, 3.3, 1.1, 0.9,
        sz=36, col=BORDER, align=PP_ALIGN.CENTER)

    # Read side panel
    rect(slide, 7.13, 1.05, 5.8, 5.35, fill=PANEL, line=BORDER)
    txt(slide, "QUERIES (Read)", 7.38, 1.15, 5.3, 0.48,
        sz=17, col=ACCENT, bold=True)
    read_items = [
        ("EventStore (events)",        ACCENT, True),
        ("  ↓",                        MUTED,  False),
        ("ProjectionUpdater",           ACCENT, True),
        ("  ↓",                        MUTED,  False),
        ("projection_machine_state",   ACCENT, True),
        ("  ↓",                        MUTED,  False),
        ("REST API / Dashboard",       ACCENT, True),
    ]
    for i, (label, col, bold) in enumerate(read_items):
        txt(slide, label, 7.38, 1.75 + i * 0.6, 5.3, 0.55,
            sz=14, col=col, bold=bold)

    notes(slide,
          "CQS (the Principle) says: a method either changes state OR returns data, never both. "
          "CQRS lifts that to the architectural level: separate object models for commands and queries. "
          "In the demo they share one JVM, but the boundary is explicit and the models don't leak.")
    return slide
