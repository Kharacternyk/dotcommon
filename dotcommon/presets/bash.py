from dotcommon.util import strip

paths = (".bashrc", "bashrc")

def atomize_readline_macros(text):
    lines = text.splitlines()
    for line in lines:
        stripped = strip(line, "#")
        if stripped.startswith("bind"):
            yield stripped

def atomize_aliases(text):
    lines = text.splitlines()
    for line in lines:
        stripped = strip(line, "#")
        if stripped.startswith("alias"):
            yield stripped
