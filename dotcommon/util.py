def strip(string, comment_chars):
    comment_start = string.find(comment_chars)
    if comment_start == -1:
        return string.rstrip()
    else:
        return string[:comment_start].rstrip()


def lines_starting_with(start, comment_chars):
    def _f(text):
        for line in text.splitlines():
            stripped = strip(line, '"')
            if stripped.startswith(start):
                yield stripped

    return _f
