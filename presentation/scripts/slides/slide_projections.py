"""Slide 12 — Projections"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "A projection is a tailored read model built from events")

    projections = [
        ("Bean Levels",
         "SELECT name,\n"
         "       beans_available,\n"
         "       cups_produced\n"
         "FROM projection_machine_state"),
        ("User Stats",
         "SELECT username,\n"
         "       coffee_type,\n"
         "       SUM(cup_count)\n"
         "FROM projection_user_stats"),
        ("Caffeine Alerts",
         "SELECT username, COUNT(*)\n"
         "FROM projection_double_espresso_log\n"
         "WHERE occurred_at > NOW()-'2h'\n"
         "GROUP BY username\n"
         "HAVING COUNT(*) >= 3"),
    ]
    for i, (title, sql) in enumerate(projections):
        l = 0.5 + i * 4.3
        rect(slide, l, 1.05, 4.0, 5.5, fill=PANEL, line=BORDER)
        txt(slide, title, l + 0.1, 1.15, 3.8, 0.48,
            sz=17, bold=True, col=ACCENT)
        code(slide, sql, l + 0.1, 1.75, 3.8, 4.62, sz=12)

    footer(slide, "Each projection is optimised for exactly one query. Rebuilt any time.")
    notes(slide,
          "You can have as many projections as you need. "
          "They're cheap to add because events never change. "
          "Add a new business requirement? Add a new projection. "
          "No schema migration on the event store.")
    return slide
