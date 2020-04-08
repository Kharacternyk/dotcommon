#!/usr/bin/env python

from dotcommon.count_atoms import count_atoms
from dotcommon.presets import vim, bash, xorg

from tabulate import tabulate
from github import Github

with open("token.gh") as token:
    g = Github(token.read().strip())

repos = g.search_repositories(query="topic:dotfiles", sort="stars")[:20]

with open("README-TEMPLATE.rst") as template:
    readme_intro = template.read()

readme = open("README.rst", "w")


def echo(*args):
    print(*args, file=readme)


echo(readme_intro)

for preset in vim, bash, xorg:
    echo()
    echo(preset.__doc__)
    echo("------------------")
    echo()

    succeeded, counters_atomizers = count_atoms(repos, *preset.preset)
    echo(succeeded, "configs were found.")
    echo()
    for counter, atomizer in counters_atomizers:
        echo(atomizer.__doc__)
        echo("~~~~~~~~~~~~~~~~~~~~~")
        echo()
        echo(tabulate(counter.most_common(10), tablefmt="rst"))
        echo()
