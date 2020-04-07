#!/usr/bin/env python

import dotcommon.crawler as c
import dotcommon.presets as p

from tabulate import tabulate
from github import Github

token = open("token.gh")
g = Github(token.read().strip())
token.close()

repos = c.get_repos(g)[:10]

readme_intro = """
dotcommon is a crawler that is built to answer questions
*What are the most popular Bash aliases?*,
*What are the most popular Vundle plugins for Vim?*, etc.
It crawls GitHub repos that match topic ``dotfiles`` and counts such things.

.. contents:: Navigation:
   :backlinks: none
"""

readme = open("README.rst", "w")

def echo(*args):
    print(*args, file=readme)

echo(readme_intro)

for preset in p.Vim, p.Bash: 
    echo()
    echo(preset.__name__)
    echo("------------------")
    echo()

    counters = c.count_atoms(repos, *preset.preset)
    for counter in counters:
        echo(tabulate(counter.most_common(10), tablefmt="rst"))

