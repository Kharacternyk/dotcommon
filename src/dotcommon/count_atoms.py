from github import GithubException
from collections import Counter


def count_atoms(repos, paths, atomizers, *, quite=False):
    counters_atomizers = [(Counter(), atomizer) for atomizer in atomizers]

    processed_repos = 0
    succeeded_repos = 0
    for repo in repos:
        for path in paths:
            try:
                contents = repo.get_contents(path)
                if type(contents) == list:
                    # It's a dir.
                    continue
                text = contents.decoded_content.decode("utf-8")
                succeeded_repos += 1
                for counter, atomizer in counters_atomizers:
                    counter.update(atomizer(text))
                break
            except (GithubException, AssertionError):
                pass
        if not quite:
            processed_repos += 1
            print(f"[#{processed_repos}]({succeeded_repos}): {repo.full_name}")

    return succeeded_repos, counters_atomizers
