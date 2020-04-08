from tabulate import tabulate

def write_table(counter):
    monospaced = ((f"``{c}``", i) for (c, i) in counter.most_common(10))
    print()
    print(tabulate(monospaced, tablefmt="rst"))
    print()

def write_header(header, char):
    print()
    print(header)
    print(char * len(header))
    print()
