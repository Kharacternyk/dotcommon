#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


@lines_starting_with("Aliases", "alias ", "#")
def aliases():
    pass


@lines_starting_with("Exports", "export ", "#")
def exports():
    pass


@lines_starting_with("PS1", "PS1=", "#")
def ps1():
    pass


@lines_starting_with("Readline macros", "bind ", "#")
def readline_macros():
    pass


crawl("Bash", "bashrc", aliases, exports, ps1, readline_macros)
