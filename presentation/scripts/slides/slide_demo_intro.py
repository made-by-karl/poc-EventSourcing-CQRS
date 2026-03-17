"""Slide 14 — Introducing the Smart Coffee System"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Smart Coffee — OR Coffee Machine")

    # Context blurb
    rect(slide, 0.5, 1.05, 12.3, 0.88, fill=PANEL, line=BORDER)
    txt(slide,
        "Three machines in a hospital operating room. "
        "Every dispensed cup, every refill, every state change — immutably recorded.",
        0.75, 1.12, 11.8, 0.74,
        sz=15, col=TEXT, wrap=True)

    # Machine badges
    machines = [
        ("OR Machine 1",   "60 beans"),
        ("OR Machine 2",   "60 beans"),
        ("Doctors' Lounge", "40 beans"),
    ]
    for i, (name, beans) in enumerate(machines):
        l = 0.4 + i * 4.265
        rect(slide, l, 2.18, 4.0, 2.0, fill=PANEL, line=ACCENT, lw=Pt(2))
        txt(slide, "☕", l + 1.5, 2.27, 1.0, 0.78,
            sz=32, col=ACCENT, align=PP_ALIGN.CENTER)
        txt(slide, name,  l + 0.1, 3.12, 3.8, 0.5,
            sz=15, bold=True, col=TEXT, align=PP_ALIGN.CENTER)
        txt(slide, beans, l + 0.1, 3.62, 3.8, 0.45,
            sz=13, col=MUTED, align=PP_ALIGN.CENTER)

    # Stack badge strip
    rect(slide, 0.5, 4.45, 12.3, 0.72, fill=BORDER, line=BORDER)
    txt(slide,
        "Spring Boot 4  ·  Java 24  ·  PostgreSQL  ·  Flyway  ·  Docker",
        0.7, 4.5, 11.9, 0.62,
        sz=15, col=ACCENT, align=PP_ALIGN.CENTER)

    footer(slide, "Open http://localhost:8080 and http://localhost:8081 now")
    notes(slide,
          "Point the audience to the running app. If you have it open, switch to it now. "
          "Three machines, all pre-seeded via DataInitializer on startup.")
    return slide
