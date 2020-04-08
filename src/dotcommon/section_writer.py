from tabulate import tabulate

class SectionWriter:
    def __init__(self, filename):
        self.file = open(filename, "w")

    def echo(self, *args):
        print(*args, file=self.file)

    def write_table(self, counter):
        monospaced = ((f"``{c}``", i) for (c, i) in counter.most_common(10))
        self.echo()
        self.echo(tabulate(monospaced, tablefmt="rst"))
        self.echo()

    def write_header(self, header):
        self.echo()
        self.echo(header)
        self.echo("-" * len(header))
        self.echo()
