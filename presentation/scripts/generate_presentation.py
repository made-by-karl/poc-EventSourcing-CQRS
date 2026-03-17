#!/usr/bin/env python3
"""
generate_presentation.py — Master script for "Facts over State" developer talk.

Usage:
    pip install python-pptx
    python3 scripts/generate_presentation.py

Output: facts-over-state.pptx  (project root)
"""

import os
import sys

# Ensure scripts/ is on the path so common.py and the slides package are found
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS_DIR)

from pptx import Presentation
from pptx.util import Inches

from common import SW, SH

# Import every slide module in presentation order
from slides import slide_title
from slides import slide_product
from slides import slide_scenario
from slides import slide_divider_es
from slides import slide_traditional
from slides import slide_lost
from slides import slide_shift
from slides import slide_what_is_event
from slides import slide_aggregate
from slides import slide_event_stream
from slides import slide_domain_events_table
from slides import slide_demo_intro
from slides import slide_demo_event_stored
from slides import slide_demo_time_travel
from slides import slide_demo_concurrent
from slides import slide_divider_cqrs
from slides import slide_rw_mismatch
from slides import slide_cqrs_two_models
from slides import slide_projections
from slides import slide_write_read_loop
from slides import slide_demo_projections_intro
from slides import slide_demo_caffeine
from slides import slide_demo_rebuild
from slides import slide_divider_perf
from slides import slide_snapshotting
from slides import slide_append_only
from slides import slide_scaling_writes
from slides import slide_scaling_reads
from slides import slide_costs
from slides import slide_when_to_use
from slides import slide_getting_started
from slides import slide_the_shift
from slides import slide_thankyou

SLIDE_MODULES = [
    slide_title,
    slide_product,
    # Event Sourcing
    slide_divider_es,
    slide_scenario,
    slide_traditional,
    slide_lost,
    slide_shift,
    slide_what_is_event,
    slide_aggregate,
    slide_event_stream,
    slide_domain_events_table,
    slide_demo_intro,
    slide_demo_event_stored,
    slide_demo_time_travel,
    slide_demo_concurrent,
    # CQRS
    slide_divider_cqrs,
    slide_rw_mismatch,
    slide_cqrs_two_models,
    slide_projections,
    slide_write_read_loop,
    slide_demo_projections_intro,
    slide_demo_caffeine,
    slide_demo_rebuild,
    # Performance ES
    slide_divider_perf,
    slide_append_only,
    slide_snapshotting,
    # Performance CQRS
    slide_scaling_writes,
    slide_scaling_reads,
    # Closing
    slide_costs,
    slide_when_to_use,
    slide_getting_started,
    slide_the_shift,
    slide_thankyou,
]


def main() -> None:
    prs = Presentation()
    prs.slide_width  = Inches(SW)
    prs.slide_height = Inches(SH)

    for i, module in enumerate(SLIDE_MODULES, start=1):
        module.add_slide(prs)
        print(f"  [{i:02d}/{len(SLIDE_MODULES)}]  {module.__name__}")

    # Save to parent of scripts folder
    out = os.path.join(os.path.dirname(SCRIPTS_DIR), "facts-over-state.pptx")
    prs.save(out)
    print(f"\n✓  Saved {len(SLIDE_MODULES)} slides → {out}")


if __name__ == "__main__":
    main()
