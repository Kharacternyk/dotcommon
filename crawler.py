#!/usr/bin/env python

from dotcommon.count_atoms import count_atoms
from dotcommon.presets import vim, bash, xorg
from dotcommon.readme_writer import ReadmeWriter
from github import Github

with open("token.gh") as token:
    g = Github(token.read().strip())

repos = g.search_repositories(query="topic:dotfiles", sort="stars")[:250]

with open("README-TEMPLATE.rst") as template:
    readme_intro = template.read()

readme = ReadmeWriter("README.rst")
readme.echo(readme_intro)

for preset in vim, bash, xorg:
    readme.write_preset(preset)
    succeeded, counters_atomizers = count_atoms(repos, *preset.preset)
    readme.echo(succeeded, "configs were found.")
    for counter, atomizer in counters_atomizers:
        readme.write_atomizer(atomizer)
        readme.write_counter(counter)
