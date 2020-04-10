#!/usr/bin/env python

from dotcommon.count_atoms import count_atoms
from dotcommon.write import write_header, write_table
from github import Github


def crawl(header, filename, *atomizers, count=None, path=None):
    with open("token.gh") as token:
        g = Github(token.read().strip())

    query = "filename:" + filename
    if path != None:
        query += " path:" + path

    files = g.search_code(query=query, sort='indexed', order='desc')

    if count != None:
        files = files[:count]

    write_header(header, "-")

    counters_atomizers = count_atoms(files, atomizers)
    for counter, atomizer in counters_atomizers:
        write_header(atomizer.__doc__, "~")
        write_table(counter)
