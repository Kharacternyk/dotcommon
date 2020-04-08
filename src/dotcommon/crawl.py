#!/usr/bin/env python

from dotcommon.count_atoms import count_atoms
from dotcommon.write import write_header, write_table
from github import Github


def crawl(header, paths, atomizers):
    with open("token.gh") as token:
        g = Github(token.read().strip())

    repos = g.search_repositories(query="topic:dotfiles", sort="stars")[:500]

    write_header(header, "-")

    succeeded, counters_atomizers = count_atoms(repos, paths, atomizers)
    print(succeeded, "configs were found.")
    for counter, atomizer in counters_atomizers:
        write_header(atomizer.__doc__, "~")
        write_table(counter)
