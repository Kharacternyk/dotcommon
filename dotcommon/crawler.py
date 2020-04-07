from github import GithubException
from collections import Counter


def get_repos(github, query="topic:dotfiles"):
    return github.search_repositories(query=query)


def count_atoms(repos, atomizer, paths, *, repo_count=100, quite=False):
    counter = Counter()

    processed_repos = 0
    succeeded_repos = 0
    for repo in repos[:repo_count]:
        for path in paths:
            try:
                contents = repo.get_contents(path)
                if type(contents) == list:
                    # It's a dir.
                    continue
                text = contents.decoded_content.decode("utf-8")
                counter.update(atomizer(text))
                succeeded_repos += 1
                break
            except (GithubException, AssertionError):
                pass
        if not quite:
            processed_repos += 1
            print(f"[#{processed_repos}]({succeeded_repos}): {repo.full_name}")

    return counter
