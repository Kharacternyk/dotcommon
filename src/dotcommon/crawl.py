#!/usr/bin/env python

from dotcommon.count_atoms import count_atoms
from dotcommon.write import write_header, write_table
from github import Github


def crawl(header, paths, atomizers):
    with open("token.gh") as token:
        g = Github(token.read().strip())

    query = " ".join("filename:" + path for path in paths)
    files = g.search_code(query=query)[:10]

    write_header(header, "-")

    counters_atomizers = count_atoms(files, paths, atomizers)
    for counter, atomizer in counters_atomizers:
        write_header(atomizer.__doc__, "~")
        write_table(counter)
