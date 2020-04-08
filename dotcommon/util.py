def strip(string, comment_chars):
    comment_start = string.find(comment_chars)
    if comment_start == -1:
        return string.rstrip()
    else:
        return string[:comment_start].rstrip()


def lines_starting_with(doc, start, comment_chars):
    def _f(text):
        for line in text.splitlines():
            stripped = strip(line, comment_chars)
            if stripped.startswith(start):
                yield stripped

    _f.__doc__ = doc

    return lambda _: _f
