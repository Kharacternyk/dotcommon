#!/bin/python3

import github as github_module
from github import Github
from getpass import getpass
from collections import Counter
from pprint import pprint

def auth():
    username = input("Username: ")
    password = getpass("Password: ")
    return Github(username, password)

def strip_comment(line, comment_chars):
    i = line.find(comment_chars)
    if i == -1:
        return line
    return line[:i]

def count_lines(comment_chars, count, *paths):
    github = auth()
    counter = Counter()

    dot_repos = github.search_repositories(query="topic:dotfiles")

    for i, repo in enumerate(dot_repos[:count]):
        for path in paths:
            try:
                cfg = repo.get_contents(path)
                lines = cfg.decoded_content.decode("utf-8").splitlines()
                counter.update(strip_comment(line, comment_chars) for line in lines)
                print(i)
                break
            except Exception:
                pass

    pprint(counter)
