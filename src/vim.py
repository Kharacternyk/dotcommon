#!/usr/bin/env python

from dotcommon.util import lines_starting_with, strip
from dotcommon.crawl import crawl

paths = (".vimrc", "vimrc", ".vim/vimrc", "vim/.vimrc", "vim/vimrc")


@lines_starting_with("Set statements", "set ", '"')
def set_statements():
    pass


@lines_starting_with("Vundle plugins", "Plugin ", '"')
def vundle():
    pass


@lines_starting_with("Vim-plug plugins", "Plug ", '"')
def plug():
    pass

def custom_functions(text):
    "Custom functions per vimrc"
    count = 0
    for line in text.splitlines():
        stripped = strip(line, '"')
        if stripped.startswith("endfun"):
            count += 1
    # A tuple!
    return count,


atomizers = set_statements, vundle, plug, custom_functions

crawl("Vim", paths, atomizers)
