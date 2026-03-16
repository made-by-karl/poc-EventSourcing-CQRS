"""Slide 26 — When to Choose ES+CQRS"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Good fits vs Poor fits")

    # Good fits
    rect(slide, 0.4, 1.05, 5.8, 5.5, fill=PANEL, line=SUCCESS, lw=Pt(2))
    txt(slide, "✓  Good fits", 0.65, 1.15, 5.3, 0.48,
        sz=17, bold=True, col=SUCCESS)
    good = [
        "Audit and compliance are\nfirst-class requirements",
        "Read/write loads differ greatly\n— high fan-out queries",
        "Complex domain where history\nmatters (finance, medical, logistics)",
    ]
    for i, item in enumerate(good):
        rect(slide, 0.6, 1.78 + i * 1.52, 5.5, 1.38, fill=BG, line=BORDER)
        txt(slide, item, 0.8, 1.88 + i * 1.52, 5.1, 1.18,
            sz=13, col=TEXT, wrap=True)

    # Poor fits
    rect(slide, 7.13, 1.05, 5.8, 5.5, fill=PANEL, line=DANGER, lw=Pt(2))
    txt(slide, "✗  Poor fits", 7.38, 1.15, 5.3, 0.48,
        sz=17, bold=True, col=DANGER)
    bad = [
        "Simple CRUD — user profiles,\nsettings, content management",
        "Evolving domain: frequent shifts in aggregates and business rules make event schemas unstable",
        "Strong consistency required\nacross aggregates in one transaction",
    ]
    for i, item in enumerate(bad):
        rect(slide, 7.33, 1.78 + i * 1.52, 5.5, 1.38, fill=BG, line=BORDER)
        txt(slide, item, 7.53, 1.88 + i * 1.52, 5.1, 1.18,
            sz=13, col=TEXT, wrap=True)

    notes(slide,
          "The coffee machine demo is deliberately low-stakes. "
          "But the medical audit requirement is a real-world constraint. "
          "If you're on a compliance system, this is your pattern. "
          "If you're building a blog, it's not.")
    return slide
