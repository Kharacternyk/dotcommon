#!/bin/python3

import github as github_module
from github import Github
from getpass import getpass
from collections import Counter
from pprint import pprint

username = input("Username: ")
password = getpass("Password: ")
github = Github(username, password)

counter = Counter()
dot_repos = github.search_repositories(query="topic:dotfiles")

def strip_comment(line):
    i = line.find('"')
    if i == -1:
        return line
    return line[:i]

for i, repo in enumerate(dot_repos[:300]):
    try:
        vimrc = repo.get_contents(".vimrc")
        lines = vimrc.decoded_content.decode("utf-8").splitlines()
        counter.update(strip_comment(line) for line in lines)
        print(i, "+1")
    except Exception:
        print(i, ":(")

pprint(counter)
