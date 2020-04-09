#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def window_rules(text):
    "Window rules"
    return lines_starting_with("bspc rule ", text)


def gap_border(text):
    "Window gap/border width"
    gap = "unset"
    border = "unset"
    for line in text.splitlines():
        stripped = line.rstrip()
        if stripped.startswith("bspc config window_gap "):
            gap = stripped[stripped.rfind(" ") + 1 :]
        elif stripped.startswith("bspc config border_width "):
            border = stripped[stripped.rfind(" ") + 1 :]
    # Tuple!
    return (f"{gap}/{border}",)


crawl("BSPWM", "bspwmrc", window_rules, gap_border)
