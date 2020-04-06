def preset(paths):
    return lambda atomizer: (atomizer, paths)


def strip(string, comment_chars):
    comment_start = string.find(comment_chars)
    if comment_start == -1:
        return string.strip()
    else:
        return string[:comment_start].strip()


def lines_starting_with(start, comment_chars):
    def _f(text):
        lines = text.splitlines()
        for line in lines:
            stripped = strip(line, '"')
            if stripped.startswith(start):
                yield stripped

    return _f
