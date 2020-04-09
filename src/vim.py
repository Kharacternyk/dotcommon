#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def set_statements(text):
    "Set statements"
    return lines_starting_with("set ", text)


def leader(text):
    "<leader> key mappings"
    for line in text.splitlines():
        if line.startswith("let mapleader"):
            stripped = line.rstrip()
            quote = stripped[-1]
            char = stripped[stripped.find(quote) + 1 : -1]
            return (char,)
    return ()


def vundle(text):
    "Vundle plugins"
    return lines_starting_with("Plugin ", text)


def plug(text):
    "Vim-plug plugins"
    return lines_starting_with("Plug ", text)


def custom_functions(text):
    "Custom functions per vimrc"
    count = 0
    for line in text.splitlines():
        stripped = line.rstrip()
        if stripped.startswith("endfun"):
            count += 1
    # A tuple!
    return (count,)


crawl("Vim", "vimrc", set_statements, leader, vundle, plug, custom_functions)
