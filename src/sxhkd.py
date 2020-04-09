#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def commands(text):
    "Commands bound to keybinds"
    indented = lines_starting_with(" ", text)
    stripped = (line.strip() for line in indented)
    return stripped


crawl("sxhkd", "sxhkdrc", commands, count=15)
