"""Slide — Adding projections doesn't slow commands"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Adding projections doesn't slow commands")

    # ── Flow diagram ─────────────────────────────────────────────────────────
    # Left: command handler box
    rect(slide, 0.6, 1.2, 3.8, 1.6, fill=PANEL, line=ACCENT, lw=Pt(2))
    txt(slide, "Command handler", 0.8, 1.28, 3.4, 0.38,
        sz=14, bold=True, col=ACCENT)
    txt(slide, "append(event)\nCOMMIT → 200 OK", 0.8, 1.72, 3.4, 0.95,
        fn=MONO, sz=13, col=TEXT)

    # Arrow
    txt(slide, "── AFTER_COMMIT ──→", 4.55, 1.65, 3.3, 0.5,
        fn=MONO, sz=12, col=MUTED, align=PP_ALIGN.CENTER)

    # Right: projection boxes
    proj_names = ["Projection 1", "Projection 2", "Projection 3", "Projection N"]
    for i, name in enumerate(proj_names):
        y = 1.15 + i * 0.42
        rect(slide, 8.1, y, 2.8, 0.36, fill=PANEL, line=BORDER)
        txt(slide, name, 8.2, y + 0.02, 2.6, 0.32,
            sz=12, col=TEXT, align=PP_ALIGN.CENTER)
    txt(slide, "(separate tx)", 8.1, 2.85, 2.8, 0.3,
        sz=11, col=MUTED, italic=True, align=PP_ALIGN.CENTER)

    # ── Code block ───────────────────────────────────────────────────────────
    code(slide,
         "@TransactionalEventListener(phase = AFTER_COMMIT)\n"
         "@Transactional(propagation = REQUIRES_NEW)\n"
         "public void on(EventStoreUpdatedEvent wrapper) {\n"
         "    apply(wrapper.getDomainEvent());\n"
         "}",
         0.6, 3.35, 10.5, 1.55, sz=13)

    # ── Two key-point cards ──────────────────────────────────────────────────
    card(slide, 0.6, 5.15, 5.6, 1.5,
         "Write latency is constant",
         "The command returns after ONE INSERT. "
         "Adding projection #4 or #40 doesn't add to response time.",
         tsz=14, bsz=12)

    card(slide, 6.6, 5.15, 5.6, 1.5,
         "Eventual consistency is the trade-off",
         "Projections update milliseconds later. "
         "The 3-second auto-refresh in our UI masks this entirely.",
         tsz=14, bsz=12)

    footer(slide,
           "Projections are observers, not participants in the write transaction.")

    notes(slide,
          "TransactionalEventListener(AFTER_COMMIT) means projection updates don't start "
          "until the event store tx commits and HTTP 200 returns. REQUIRES_NEW means "
          "projections run in their own transaction. Command latency = one INSERT, "
          "regardless of projection count. Trade-off: brief eventual consistency window "
          "(milliseconds). In the demo, 3-second auto-refresh masks it completely.")
    return slide
