"""Slide 23 — Aggregates as Natural Partitions"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Scale-out is natural — aggregates don't share state")

    # Timeline lanes
    lane_data = [
        ("OR Machine 1",   [3.5, 5.2, 7.0]),
        ("OR Machine 2",   [4.0, 6.5]),
        ("Doctors Lounge", [3.8, 5.5, 7.2, 9.2]),
    ]
    row_ys = [1.2, 2.5, 3.8]
    for row_i, ((name, dot_xs), y) in enumerate(zip(lane_data, row_ys)):
        txt(slide, name, 0.5, y + 0.14, 2.5, 0.45, sz=13, col=MUTED, bold=True)
        # Lane line
        rect(slide, 3.1, y + 0.34, 9.7, 0.06, fill=BORDER)
        # Event dots
        for dx in dot_xs:
            rect(slide, dx, y + 0.17, 0.42, 0.42, fill=ACCENT, line=ACCENT)

    # Key point cards
    points = [
        ("No global lock",
         "Each machine's event stream is independent. "
         "Seq numbers are per-machine, not global."),
        ("Route by ID",
         "Hash aggregate ID → handler node. "
         "Zero cross-node coordination."),
        ("Linear scale-out",
         "Add more handler nodes to process more "
         "machines in parallel."),
    ]
    for i, (title, body) in enumerate(points):
        l = 0.4 + i * 4.3
        card(slide, l, 5.15, 4.0, 1.9, title, body, tsz=14, bsz=12)

    notes(slide,
          "This is the horizontal scaling story. "
          "Route by aggregate ID to a specific handler node, "
          "and you get linear scalability with zero cross-node coordination. "
          "The UNIQUE constraint enforces ordering *within* one machine, not globally.")
    return slide
