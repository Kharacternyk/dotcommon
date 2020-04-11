#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def aliases(text):
    "Aliases"
    return lines_starting_with("alias ", text)

def theme(text):
    "Theme"
    return lines_starting_with("ZSH_THEME=", text)

def exports(text):
    "Exports"
    return lines_starting_with("export ", text)

def keybindings(text):
    "Keybindings"
    return lines_starting_with("bindkey ", text)

crawl("ZSH", "zshrc", aliases, exports, theme, keybindings)
