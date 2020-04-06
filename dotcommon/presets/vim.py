def atomize(text):
    lines = text.splitlines()
    for line in lines:
        comment_start = line.find('"')
        if comment_start == -1:
            stripped_line = line.strip()
        else:
            stripped_line = line[:comment_start].strip()

        if stripped_line.startswith("set"):
            yield stripped_line


paths = (".vimrc", "vimrc", ".vim/vimrc")

preset = (atomize, paths)
