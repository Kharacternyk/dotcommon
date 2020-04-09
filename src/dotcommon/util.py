def lines_starting_with(start, text):
    for line in text.splitlines():
        stripped = line.rstrip()
        if stripped.startswith(start):
            yield stripped
