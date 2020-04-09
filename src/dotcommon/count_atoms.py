from github import GithubException
from collections import Counter
from sys import stderr


def count_atoms(files, atomizers):
    counters_atomizers = [(Counter(), atomizer) for atomizer in atomizers]

    for file in files:
        try:
            text = file.decoded_content.decode("utf-8")
            for counter, atomizer in counters_atomizers:
                counter.update(atomizer(text))
        except (GithubException, AssertionError) as e:
            print(e, file=stderr)
            pass

    return counters_atomizers
