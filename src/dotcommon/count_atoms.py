from github import GithubException
from collections import Counter
from sys import stderr


def count_atoms(files, atomizers):
    counters_atomizers = [(Counter(), atomizer) for atomizer in atomizers]

    try:
        for file in files:
            try:
                text = file.decoded_content.decode("utf-8")
            except (GithubException, AssertionError, UnicodeDecodeError, TypeError) as e:
                print(e, file=stderr)
                pass
            else:
                for counter, atomizer in counters_atomizers:
                    counter.update(atomizer(text))
    except IndexError:
        print("Interrupted")

    return counters_atomizers
