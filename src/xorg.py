#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def window_managers(text):
    "Window managers"
    return lines_starting_with("exec ", text)


def daemons(text):
    "Daemons"
    for line in text.splitlines():
        stripped = line.rstrip()
        if stripped != "" and stripped[-1] == "&":
            if stripped.split()[0] not in ("done", "fi", "esac"):
                yield stripped


crawl("Xorg", "xinitrc", window_managers, daemons)
