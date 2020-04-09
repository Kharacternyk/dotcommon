#!/usr/bin/env python

from dotcommon.count_atoms import count_atoms
from dotcommon.write import write_header, write_table
from github import Github


def crawl(header, filename, *atomizers, count=2000):
    with open("token.gh") as token:
        g = Github(token.read().strip())

    files = g.search_code(query="filename:" + filename)[:count]

    write_header(header, "-")

    counters_atomizers = count_atoms(files, atomizers)
    for counter, atomizer in counters_atomizers:
        write_header(atomizer.__doc__, "~")
        write_table(counter)
