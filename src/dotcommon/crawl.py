#!/usr/bin/env python

from dotcommon.count_atoms import count_atoms
from dotcommon.write import write_header, write_table
from github import Github


def crawl(header, filename, atomizers):
    with open("token.gh") as token:
        g = Github(token.read().strip())

    files = g.search_code(query="filename:" + filename)[:2000]

    write_header(header, "-")

    counters_atomizers = count_atoms(files, atomizers)
    for counter, atomizer in counters_atomizers:
        write_header(atomizer.__doc__, "~")
        write_table(counter)
