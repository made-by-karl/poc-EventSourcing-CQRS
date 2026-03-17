"""Slide 25 — The Costs / Trade-offs"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "ES+CQRS is not free")

    costs = [
        ("Eventual consistency",
         "Projections lag behind the event store — typically milliseconds, "
         "sometimes seconds. Your UI must tolerate this."),
        ("Schema evolution",
         "Old events are immutable. Adding fields requires upcasters — "
         "functions that upgrade old event versions on read."),
        ("Complexity",
         "More moving parts than a CRUD stack. "
         "Steeper learning curve. Team buy-in is required."),
        ("Debugging tooling",
         "You need a way to browse the event log. "
         "That's what pgweb is for in the demo. "
         "In production: dedicated event viewer or Kibana."),
    ]
    positions = [(0.4, 1.05), (6.73, 1.05), (0.4, 3.85), (6.73, 3.85)]
    for (l, t), (title, body) in zip(positions, costs):
        card(slide, l, t, 6.2, 2.55, title, body, tsz=16, bsz=12)

    notes(slide,
          "Be honest about this. ES+CQRS is not a universal solution. "
          "The trade-offs are real, and skipping this slide would be doing "
          "the audience a disservice.")
    return slide
