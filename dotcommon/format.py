from tabulate import tabulate

def counter_to_table(counter, line_count):
    monospaced = ((f"``{c}``", i) for (c, i) in counter.most_common(line_count))
    return tabulate(monospaced, tablefmt="rst")
