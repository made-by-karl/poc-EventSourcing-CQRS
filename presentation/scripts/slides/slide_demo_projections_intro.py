"""Slide — Demo intro: Projections in Action"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "Projections in Action")

    # Intro blurb
    rect(slide, 0.5, 1.05, 12.3, 0.88, fill=PANEL, line=BORDER)
    txt(slide,
        "Let\u2019s switch to the running application and look at "
        "how projections work end-to-end \u2014 dashboard, tables, code, and rebuild.",
        0.75, 1.12, 11.8, 0.74,
        sz=15, col=TEXT, wrap=True)

    # Four things to show
    items = [
        ("\U0001f4ca", "Dashboard",        "projections.html \u2014 bean levels,\nuser stats, caffeine alerts"),
        ("\U0001f5c3\ufe0f", "Projection Tables", "projection_machine_state,\nprojection_user_stats,\nprojection_double_espresso_log"),
        ("\U0001f4bb", "Code",              "ProjectionUpdater \u2014\nhow events become rows"),
        ("\U0001f504", "Rebuild",           "POST /admin/projections/rebuild\n\u2014 truncate + full replay"),
    ]
    for i, (icon, title, body) in enumerate(items):
        l = 0.4 + i * 3.2
        w = 3.0
        rect(slide, l, 2.18, w, 2.8, fill=PANEL, line=ACCENT, lw=Pt(2))
        txt(slide, icon, l + 0.9, 2.28, 1.2, 0.72,
            sz=30, col=ACCENT, align=PP_ALIGN.CENTER)
        txt(slide, title, l + 0.1, 3.05, w - 0.2, 0.48,
            sz=15, bold=True, col=TEXT, align=PP_ALIGN.CENTER)
        txt(slide, body, l + 0.1, 3.55, w - 0.2, 1.3,
            sz=11, col=MUTED, align=PP_ALIGN.CENTER, wrap=True)

    footer(slide, "Demo & Code")
    notes(slide,
          "[SWITCH TO APP] Open projections.html and walk through the three panels: "
          "bean levels, user stats, caffeine alerts. "
          "Then open pgAdmin or psql and show the projection tables — "
          "each one is a single-purpose read model. "
          "Show ProjectionUpdater code: the @TransactionalEventListener that turns "
          "domain events into projection rows. "
          "Finally, show the rebuild endpoint: POST /admin/projections/rebuild "
          "truncates all projection tables and replays every event from scratch.")
    return slide
