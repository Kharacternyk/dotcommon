#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def modkey(text):
    "Modkey"
    return lines_starting_with("set $mod ", text)


def font(text):
    "Font"
    return lines_starting_with("font ", text)


def keybindings(text):
    "Keybindings"
    return lines_starting_with("bindsym ", text)


def modes(text):
    "Modes"
    return lines_starting_with("mode ", text)


def inner_gaps(text):
    "Inner gaps"
    return lines_starting_with("gaps inner ", text)


def outer_gaps(text):
    "Outer gaps"
    return lines_starting_with("gaps outer ", text)


def autostart(text):
    "exec"
    return lines_starting_with("exec --no-startup-id ", text)


crawl("i3wm", "config", modkey, font, keybindings, modes, inner_gaps, outer_gaps, autostart, path="i3")
