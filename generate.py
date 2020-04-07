#!/usr/bin/env python

import dotcommon.crawler as c
import dotcommon.presets as p

from tabulate import tabulate
from github import Github

with open("token.gh") as token:
    g = Github(token.read().strip())

repos = c.get_repos(g)[:200]

with open("README-TEMPLATE.rst") as template:
    readme_intro = template.read()

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

