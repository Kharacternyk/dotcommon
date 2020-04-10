#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def set_statements(text):
    "Set statements"
    return lines_starting_with("set ", text)


def colorschemes(text):
    "Colorschemes"
    return lines_starting_with("colorscheme ", text)


def vundle(text):
    "Vundle plugins"
    return lines_starting_with("Plugin ", text)


def plug(text):
    "Vim-plug plugins"
    return lines_starting_with("Plug ", text)


crawl("Vim", "vimrc", set_statements, colorschemes, vundle, plug)
