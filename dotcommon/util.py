def strip(string, comment_chars):
    comment_start = string.find(comment_chars)
    if comment_start == -1:
        return string.strip()
    else:
        return string[:comment_start].strip()

