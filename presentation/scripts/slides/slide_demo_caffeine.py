"""Slide 19 — Demo 4: Caffeine Alerts (Real-Time Projection)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Demo 4 — Real-Time Projection")

    # Left panel — alert banner mock
    rect(slide, 0.4, 1.05, 5.8, 5.3, fill=PANEL, line=BORDER)
    txt(slide, "projections.html — Caffeine Alerts",
        0.65, 1.15, 5.3, 0.42, sz=12, col=MUTED)
    # Orange alert banner
    rect(slide, 0.55, 1.7, 5.5, 1.12, fill="e65100", line=ACCENT, lw=Pt(2))
    txt(slide, "⚠  CAFFEINE ALERT",
        0.75, 1.78, 5.1, 0.45, sz=17, bold=True, col="ffffff")
    txt(slide, "Dr. Smith — 3 double espressos in 2 hours",
        0.75, 2.24, 5.1, 0.42, sz=13, col="ffffff")
    txt(slide, "Auto-refreshes every 3 seconds",
        0.65, 3.0, 5.3, 0.42, sz=12, col=MUTED, italic=True)

    # Right panel — SQL
    rect(slide, 6.5, 1.05, 6.6, 5.3, fill=PANEL, line=BORDER)
    txt(slide, "SQL behind the alert:",
        6.75, 1.15, 6.1, 0.45, sz=14, bold=True, col=ACCENT)
    code(slide,
         "SELECT username, COUNT(*) AS cnt\n"
         "FROM   projection_double_espresso_log\n"
         "WHERE  occurred_at > NOW()\n"
         "                   - INTERVAL '2 hours'\n"
         "GROUP  BY username\n"
         "HAVING COUNT(*) >= 3;",
         6.75, 1.72, 6.1, 3.5, sz=13)

    footer(slide, "A projection built for exactly one business rule.")
    notes(slide,
          "[DEMO] Dispense 3 double espressos for the same user. "
          "Watch the orange alert banner appear within 3 seconds (auto-refresh). "
          "The projection is a dedicated table — fast, simple, single-purpose.")
    return slide
