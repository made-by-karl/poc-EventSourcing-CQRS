"""Slide — Each projection is built for one job"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Each projection is built for one job")

    # ── Three projection cards across the top ────────────────────────────────
    cards = [
        ("Bean Levels",
         "projection_machine_state\nPK: machine_id (UUID)\nPoint lookup, zero JOINs"),
        ("User Stats",
         "projection_user_stats\nPK: (username, coffee_type)\nPre-aggregated, no GROUP BY"),
        ("Caffeine Alerts",
         "projection_double_espresso_log\nIDX: (username, occurred_at DESC)\nIndex-only sliding window scan"),
    ]
    for i, (title, body) in enumerate(cards):
        l = 0.4 + i * 4.2
        rect(slide, l, 1.05, 3.9, 2.35, fill=PANEL, line=ACCENT, lw=Pt(2))
        txt(slide, title, l + 0.15, 1.15, 3.6, 0.42,
            sz=15, bold=True, col=ACCENT)
        txt(slide, body, l + 0.15, 1.62, 3.6, 1.65,
            fn=MONO, sz=12, col=TEXT)

    # ── Bottom panel: CRUD alternative (DANGER border) ───────────────────────
    rect(slide, 0.4, 3.65, 12.53, 2.85, fill=PANEL, line=DANGER, lw=Pt(2))
    txt(slide, "CRUD alternative", 0.65, 3.75, 12.0, 0.4,
        sz=15, bold=True, col=DANGER)
    code(slide,
         "SELECT m.name, COUNT(o.id), ...\n"
         "FROM   machines m\n"
         "  JOIN orders o  ON o.machine_id = m.id\n"
         "  JOIN users u   ON u.id = o.user_id\n"
         "WHERE  o.created_at > NOW() - INTERVAL '2 hours'\n"
         "GROUP  BY m.name\n"
         "-- 3 JOINs, full scan, one schema for every question",
         0.65, 4.2, 11.9, 2.1, sz=12)

    footer(slide,
           "Normalized = one schema for every question.  "
           "Projections = one table per question.")

    notes(slide,
          "Each projection table is optimised for exactly one query pattern. "
          "Bean levels: point lookup by UUID. User stats: pre-aggregated counts, "
          "no GROUP BY at query time. Caffeine alerts: index-only scan on a time window. "
          "Compare with CRUD's normalised schema requiring JOINs across 3 tables. "
          "Projections aren't a luxury — they're why the read side is fast.")
    return slide
