#!/bin/python3 -i

import github
from github import Github
from getpass import getpass
from collections import Counter
from pprint import pprint

def auth():
    username = input("Username: ")
    password = getpass("Password: ")
    return Github(username, password)

def common(count, atomizer, paths):
    github_instance = auth()
    counter = Counter()
    dot_repos = github_instance.search_repositories(query="topic:dotfiles")

    for i, repo in enumerate(dot_repos[:count]):
        for path in paths:
            try:
                text = repo.get_contents(path).decoded_content.decode('utf-8')
                counter.update(atomizer(text))
                print(f"Repo #{i}: found {path}")
                break
            except github.GithubException:
                print(f"Repo #{i}: no {path}")
                pass

    pprint(counter.most_common(10))
