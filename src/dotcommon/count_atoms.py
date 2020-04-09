from github import GithubException
from collections import Counter


def count_atoms(files, paths, atomizers):
    counters_atomizers = [(Counter(), atomizer) for atomizer in atomizers]

    for file in files:
        text = file.decoded_content.decode("utf-8")
        for counter, atomizer in counters_atomizers:
            counter.update(atomizer(text))

    return counters_atomizers
