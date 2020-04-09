#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


@lines_starting_with("Window managers", "exec ", "#")
def window_managers():
    pass


crawl("Xorg", "xinitrc", window_managers)
