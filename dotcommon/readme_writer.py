from tabulate import tabulate

class ReadmeWriter:
    def __init__(self, filename):
        self.file = open(filename, "w")

    def echo(self, *args):
        print(*args, file=self.file)

    def write_counter(self, counter):
        monospaced = ((f"``{c}``", i) for (c, i) in counter.most_common(10))
        self.echo()
        self.echo(tabulate(monospaced, tablefmt="rst"))
        self.echo()

    def write_preset(self, preset):
        header = preset.__doc__
        self.echo()
        self.echo(header)
        self.echo("-" * len(header))
        self.echo()

    def write_atomizer(self, atomizer):
        header = atomizer.__doc__
        self.echo()
        self.echo(header)
        self.echo("~" * len(header))
        self.echo()
