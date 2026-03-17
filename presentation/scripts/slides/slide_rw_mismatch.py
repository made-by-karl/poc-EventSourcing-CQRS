"""Slide 10 — The Read/Write Mismatch"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Write model and read model have opposite shapes")

    # Write side
    rect(slide, 0.4, 1.05, 6.07, 3.9, fill=PANEL, line=BORDER)
    txt(slide, "Write model — integrity-first", 0.65, 1.15, 5.57, 0.48,
        sz=18, col=ACCENT, bold=True)
    write_needs = [
        "Normalised — no duplicate data",
        "Referential integrity via foreign keys",
        "Transactional consistency (ACID)",
        "Optimised for single-row inserts & updates",
    ]
    for i, item in enumerate(write_needs):
        txt(slide, f"  \u2713  {item}", 0.65, 1.75 + i * 0.68, 5.57, 0.58,
            sz=15, col=TEXT)

    # vs label
    txt(slide, "vs", 6.27, 2.7, 0.8, 0.8,
        sz=32, col=MUTED, align=PP_ALIGN.CENTER)

    # Read side
    rect(slide, 6.87, 1.05, 6.07, 3.9, fill=PANEL, line=BORDER)
    txt(slide, "Read model — data-first", 7.12, 1.15, 5.57, 0.48,
        sz=18, col=ACCENT, bold=True)
    read_needs = [
        "Flat, denormalised struct",
        "Joins & aggregations pre-computed",
        "Eventually consistent — staleness is acceptable",
        "Fast dashboard & report queries",
    ]
    for i, item in enumerate(read_needs):
        txt(slide, f"  \u2713  {item}", 7.12, 1.75 + i * 0.68, 5.57, 0.58,
            sz=15, col=TEXT)

    # Conflict callout
    rect(slide, 1.0, 5.2, 11.3, 1.35, fill=BORDER, line=ACCENT, lw=Pt(2))
    txt(slide,
        "A normalised schema is too fragmented to query efficiently.\n"
        "A denormalised schema is too redundant to write safely.\n"
        "Force one model to serve both \u2014 it ends up mediocre at each.",
        1.2, 5.25, 10.9, 1.25,
        sz=15, col=DANGER, align=PP_ALIGN.CENTER)

    notes(slide,
          "CQRS comes from the insight that the read and write sides have fundamentally different needs. "
          "We can't maximize read performance while maintaining write integrity. "
          "They pull in opposite directions. "
          "CQRS solves this by giving them separate models, so each can be optimized for its own needs.")
    return slide
