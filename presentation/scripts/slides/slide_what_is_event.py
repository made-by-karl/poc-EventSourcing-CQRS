"""Slide 07 — What is an Event?"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from common import *


def add_slide(prs):
    slide = new_slide(prs)
    hdr(slide, "An Event is an Immutable Fact")

    props = [
        ("Past tense name",
         "CoffeeProduced, BeansRefilled,\nMachineRegistered\n\n"
         "Naming signals immutability.\n\n"
         "Takes place in one aggregate.\n\n"
         "Final result of a transaction."),
        ("Timestamped",
         "When it happened, to the\nmillisecond."),
        ("Carries context",
         "Who, what, how much — everything\nneeded to reconstruct state\nfrom scratch."),
        ("Never updated or deleted",
         "Append-only. Once written, an event\nis a permanent fact in the ledger."),
    ]
    for i, (title, body) in enumerate(props):
        l = 0.4 + i * 3.25
        card(slide, l, 1.05, 3.0, 4.35, title, body, tsz=15, bsz=12)

    # Command vs Event distinction
    rect(slide, 2.0, 5.62, 9.3, 0.88, fill=BORDER, line=ACCENT)
    txt(slide,
        '"PlaceOrder" is a command.   "OrderPlaced" is an event.   Past tense signals immutability.',
        2.15, 5.68, 9.0, 0.76,
        sz=13, col=TEXT, align=PP_ALIGN.CENTER)

    notes(slide,
          "Naming matters. Past tense is a design signal — it tells every reader "
          "'this already happened; you cannot un-happen it.' "
          "Commands are intentions; events are facts. "
          "The distinction shapes the entire architecture.")
    return slide
