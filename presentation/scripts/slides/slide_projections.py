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
        rect(slide, l, 1.05, 4.0, 3.3, fill=PANEL, line=BORDER)
        txt(slide, title, l + 0.1, 1.15, 3.8, 0.48,
            sz=17, bold=True, col=ACCENT)
        code(slide, sql, l + 0.1, 1.75, 3.8, 2.5, sz=12)

    # ── Bottom panel: CRUD alternative (DANGER border) ───────────────────────
    rect(slide, 0.5, 4.6, 12.33, 2.1, fill=PANEL, line=DANGER, lw=Pt(2))
    txt(slide, "CRUD alternative", 0.65, 4.65, 12.0, 0.4,
        sz=15, bold=True, col=DANGER)
    code(slide,
         "SELECT m.name, COUNT(o.id), ...\n"
         "FROM   machines m\n"
         "  JOIN orders o  ON o.machine_id = m.id\n"
         "  JOIN users u   ON u.id = o.user_id\n"
         "WHERE  o.created_at > NOW() - INTERVAL '2 hours'\n"
         "GROUP  BY m.name\n"
         "-- 3 JOINs, full scan, one schema for every question",
         0.65, 5.05, 11.9, 1.5, sz=11)

    notes(slide,
          "You can have as many projections as you need. "
          "They're cheap to add because events never change. "
          "Each projection table is optimised for exactly one query pattern. "
          "Bean levels: point lookup by UUID. User stats: pre-aggregated counts, "
          "no GROUP BY at query time. Caffeine alerts: index-only scan on a time window. "
          "Compare with CRUD's normalised schema requiring JOINs across 3 tables. "
          "Projections aren't a luxury — they're why the read side is fast.")
    return slide
