from dotcommon.util import strip
from dotcommon.preset import preset

paths = (".bashrc", "bashrc")

@preset(paths)
def readline_macros(text):
    lines = text.splitlines()
    for line in lines:
        stripped = strip(line, "#")
        if stripped.startswith("bind"):
            yield stripped

@preset(paths)
def aliases(text):
    lines = text.splitlines()
    for line in lines:
        stripped = strip(line, "#")
        if stripped.startswith("alias"):
            yield stripped
