#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


@lines_starting_with("Set statements", "set ")
def set_statements():
    pass


@lines_starting_with("<leader> key mappings", "let mapleader")
def leader():
    pass


@lines_starting_with("Vundle plugins", "Plugin ")
def vundle():
    pass


@lines_starting_with("Vim-plug plugins", "Plug ")
def plug():
    pass


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
