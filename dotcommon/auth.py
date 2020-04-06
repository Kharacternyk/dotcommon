from github import Github
from getpass import getpass

_github = None


def auth():
    global _github
    if _github == None:
        username = input("Username: ")
        password = getpass("Password: ")
        _github = Github(username, password)
    return _github
