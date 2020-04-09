#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def window_managers(text):
    "Window managers"
    return lines_starting_with("exec ", text)


crawl("Xorg", "xinitrc", window_managers)
