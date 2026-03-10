"""Slide 27 — Getting Started"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "You don't need a framework to start")

    tiers = [
        ("1  DIY (this demo)",
         "domain_events table\n"
         "Spring JdbcTemplate\n"
         "~500 lines of infrastructure\n\n"
         "Perfect starting point.\n"
         "Everything on one screen."),
        ("2  Framework",
         "Axon Framework (Java)\n"
         "EventSourcing.NET (C#)\n\n"
         "Handles projections,\nsagas, snapshots."),
        ("3  Dedicated store",
         "EventStoreDB\n"
         "Kafka + consumer groups\n"
         "AWS EventBridge\n\n"
         "For large-scale,\ndistributed systems."),
    ]
    for i, (title, body) in enumerate(tiers):
        l = 0.5 + i * 4.3
        rect(slide, l, 1.05, 4.0, 5.55, fill=PANEL, line=BORDER)
        txt(slide, title, l + 0.1, 1.15, 3.8, 0.52,
            sz=16, bold=True, col=ACCENT)
        rect(slide, l + 0.1, 1.77, 3.8, 0.06, fill=BORDER)
        txt(slide, body, l + 0.1, 1.92, 3.8, 4.5,
            sz=13, col=TEXT, wrap=True)

    footer(slide,
           "Start with the plain JDBC approach. Add infrastructure when the pain justifies it.")
    notes(slide,
          "The demo repo is the tier-1 implementation — everything fits on a handful of screens. "
          "You can understand the entire infrastructure in an afternoon. "
          "Move to a framework when the boilerplate exceeds the learning benefit.")
    return slide
