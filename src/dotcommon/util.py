def lines_starting_with(doc, start):
    def _f(text):
        for line in text.splitlines():
            stripped = line.rstrip()
            if stripped.startswith(start):
                yield stripped

    _f.__doc__ = doc

    return lambda _: _f
