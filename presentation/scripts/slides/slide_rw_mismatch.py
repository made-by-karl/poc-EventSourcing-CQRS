"""Slide 10 — The Read/Write Mismatch"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Write model and read model have opposite shapes")

    # Write side
    rect(slide, 0.4, 1.05, 5.9, 3.9, fill=PANEL, line=BORDER)
    txt(slide, "Write model — behaviour-first", 0.65, 1.15, 5.4, 0.48,
        sz=18, col=ACCENT, bold=True)
    write_needs = [
        "Rich aggregate enforces business rules",
        '"Beans must stay \u2265 0" — checked in domain code',
        "Consistency within one aggregate boundary",
        "Versioned for optimistic concurrency",
    ]
    for i, item in enumerate(write_needs):
        txt(slide, f"  \u2713  {item}", 0.65, 1.75 + i * 0.68, 5.4, 0.58,
            sz=15, col=TEXT)

    # vs label
    txt(slide, "vs", 6.2, 2.7, 0.93, 0.8,
        sz=32, col=MUTED, align=PP_ALIGN.CENTER)

    # Read side
    rect(slide, 7.13, 1.05, 5.9, 3.9, fill=PANEL, line=BORDER)
    txt(slide, "Read model — data-first", 7.38, 1.15, 5.4, 0.48,
        sz=18, col=ACCENT, bold=True)
    read_needs = [
        "Flat, denormalised struct",
        "Joins & aggregations pre-computed",
        "Fast dashboard & report queries",
        "No behaviour \u2014 just data",
    ]
    for i, item in enumerate(read_needs):
        txt(slide, f"  \u2713  {item}", 7.38, 1.75 + i * 0.68, 5.4, 0.58,
            sz=15, col=TEXT)

    # Conflict callout
    rect(slide, 1.0, 5.2, 11.3, 1.35, fill=BORDER, line=ACCENT, lw=Pt(2))
    txt(slide,
        "A domain aggregate is too rich to query efficiently.\n"
        "A flat projection is too thin to enforce business rules.\n"
        "Force one model to serve both \u2014 it ends up mediocre at each.",
        1.2, 5.25, 10.9, 1.25,
        sz=15, col=DANGER, align=PP_ALIGN.CENTER)

    notes(slide,
          "The write model is a behavioural object — it knows the rules. "
          "The read model is a structural snapshot — it knows the shape of the data. "
          "They pull in opposite directions. "
          "CQRS is just the name we give to accepting that and using two separate models.")
    return slide
