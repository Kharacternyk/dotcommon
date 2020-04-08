#!/usr/bin/env python

from dotcommon.count_atoms import count_atoms
from dotcommon.section_writer import SectionWriter
from github import Github

def crawl(header, paths, atomizers, outputpath):
    with open("token.gh") as token:
        g = Github(token.read().strip())

    repos = g.search_repositories(query="topic:dotfiles", sort="stars")[:10]

    output = SectionWriter(outputpath)
    output.write_header(header)

    succeeded, counters_atomizers = count_atoms(repos, paths, atomizers)
    output.echo(succeeded, "configs were found.")
    for counter, atomizer in counters_atomizers:
        output.write_header(atomizer.__doc__)
        output.write_table(counter)
