#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def aliases(text):
    "Aliases"
    return lines_starting_with("alias ", text)


def exports(text):
    "Exports"
    return lines_starting_with("set -x ", text)


crawl("Fish", "config.fish", aliases, exports)
