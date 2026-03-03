"""Slide 13 — The Write–Read Loop"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "How an event flows from command to projection")

    steps = [
        ("1", "HTTP POST",                   "ProduceCoffeeCommand created from request body",          TEXT),
        ("2", "Load aggregate",              "Replay events (or snapshot + delta) to rebuild state",    TEXT),
        ("3", "Handle command",              "machine.handle(cmd)  →  CoffeeProduced event emitted",    TEXT),
        ("4", "EventStore.append()",         "Persists to domain_events  —  WRITE SIDE COMPLETE",       ACCENT),
        ("5", "EventStoreUpdatedEvent",      "Application event fired after DB commit",                 MUTED),
        ("6", "ProjectionUpdater.on()",      "Updates 3 projection tables  —  READ SIDE UPDATED",       SUCCESS),
    ]
    for i, (num, title, body, col) in enumerate(steps):
        y = 1.05 + i * 0.97
        # Number badge
        rect(slide, 0.4, y, 0.72, 0.78, fill=BORDER, line=ACCENT)
        txt(slide, num, 0.4, y + 0.14, 0.72, 0.52,
            sz=22, bold=True, col=ACCENT, align=PP_ALIGN.CENTER)
        # Step row
        rect(slide, 1.22, y, 11.7, 0.78, fill=PANEL, line=BORDER)
        txt(slide, title, 1.38, y + 0.06, 3.6, 0.32,
            sz=14, bold=True, col=col)
        txt(slide, body,  1.38, y + 0.42, 11.2, 0.34,
            sz=12, col=MUTED)

    notes(slide,
          "Steps 1–4 are the write side. Steps 5–6 are the read side. "
          "They're connected by a Spring application event in the demo, "
          "but in a distributed system you'd put a message queue here — "
          "Kafka, RabbitMQ, EventBridge. The architecture scales naturally.")
    return slide
