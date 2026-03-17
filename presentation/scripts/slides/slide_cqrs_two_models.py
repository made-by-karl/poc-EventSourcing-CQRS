"""Slide — CQRS: Two Models (visual overview)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *

DB_PNG = os.path.join(os.path.dirname(__file__), "database.png")


def _db_image(slide, cx, top, w=2.4, h=2.6):
    """Place the database.png image centred at cx, starting at top."""
    l = cx - w / 2
    slide.shapes.add_picture(DB_PNG, Inches(l), Inches(top), Inches(w), Inches(h))


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Command Query Responsibility Segregation")

    # ── Write-side DB ─────────────────────────────────────────────────────────
    write_cx = 3.0
    _db_image(slide, write_cx, 1.3)
    txt(slide, "Write Model", write_cx - 1.5, 4.1, 3.0, 0.5,
        sz=22, col=ACCENT, bold=True, align=PP_ALIGN.CENTER)

    write_props = [
        "Normalised",
        "ACID transactions",
        "Append-only events",
    ]
    for i, prop in enumerate(write_props):
        txt(slide, prop, write_cx - 1.5, 4.7 + i * 0.45, 3.0, 0.4,
            sz=14, col=TEXT, align=PP_ALIGN.CENTER)

    # ── Arrow: write → read ───────────────────────────────────────────────────
    arrow_y = 2.5
    txt(slide, "─────────────▶", 4.8, arrow_y, 3.7, 0.6,
        sz=28, col=ACCENT, align=PP_ALIGN.CENTER, fn=MONO)
    txt(slide, "\u2699\ufe0f", 5.4, arrow_y - 0.55, 0.5, 0.5,
        sz=16, col=MUTED, align=PP_ALIGN.RIGHT)
    txt(slide, "project data", 5.9, arrow_y - 0.55, 2.0, 0.5,
        sz=16, col=MUTED, italic=True)

    # ── Read-side DB ──────────────────────────────────────────────────────────
    read_cx = 10.33
    _db_image(slide, read_cx, 1.3)
    txt(slide, "Read Model", read_cx - 1.5, 4.1, 3.0, 0.5,
        sz=22, col=ACCENT, bold=True, align=PP_ALIGN.CENTER)

    read_props = [
        "Denormalised",
        "Eventually consistent",
        "Query-optimised views",
    ]
    for i, prop in enumerate(read_props):
        txt(slide, prop, read_cx - 1.5, 4.7 + i * 0.45, 3.0, 0.4,
            sz=14, col=TEXT, align=PP_ALIGN.CENTER)

    footer(slide, "Projecting into the read model is not part of the write transaction.")
    notes(slide,
          "CQS (the principle) says: a method either changes state OR returns data, never both. "
          "CQRS lifts that to the architectural level — separate models for writes and reads. "
          "The arrow is the projection step: we derive read-optimised views from the write-side events. "
          "Two models, each optimised for its job.")
    return slide
