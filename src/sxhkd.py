#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def commands(text):
    "Commands bound to keybinds"
    indented = lines_starting_with(" ", text)
    stripped = (line.strip() for line in indented if not line.isspace())
    return stripped


def commands_no_bspc(text):
    "Commands bound to keybinds (except bspc)"
    return (command for command in commands(text) if command.split()[0] != "bspc")


crawl("Sxhkd", "sxhkdrc", commands, commands_no_bspc)
