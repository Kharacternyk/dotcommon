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

for repo in dot_repos[:200]:
    try:
        vimrc = repo.get_contents(".vimrc")
        counter.update(vimrc.decoded_content.decode("utf-8").splitlines())
        print("+1")
    except github_module.GithubException:
        print(":(")

pprint(counter)
