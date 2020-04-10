#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def font(text):
    "Font"
    fonts = lines_starting_with("font = ", text)
    return (font.lower() for font in fonts)


crawl("Termite", "config", font, path="termite")
