#!/usr/bin/env python

from dotcommon.util import lines_starting_with
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


atomizers = set_statements, vundle, plug

crawl("Vim", paths, atomizers, "data/vim")
