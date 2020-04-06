from github import GithubException
from collections import Counter

def get_repos(github, query="topic:dotfiles"):
    return github.search_repositories(query=query)

def count_atoms(
    repos, atomizer, paths, *, repo_count=100, progress_reporter=(lambda repo: None)
):
    counter = Counter()

    for repo in repos[:repo_count]:
        progress_reporter(repo)
        for path in paths:
            try:
                text = repo.get_contents(path).decoded_content.decode("utf-8")
                counter.update(atomizer(text))
                break
            except GithubException:
                pass

    return counter
