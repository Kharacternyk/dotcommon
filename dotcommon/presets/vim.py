from dotcommon.util import strip

paths = (".vimrc", "vimrc", ".vim/vimrc")

def atomize_set_statements(text):
    lines = text.splitlines()
    for line in lines:
        stripped = strip(line, '"')
        if stripped.startswith("set"):
            yield stripped
