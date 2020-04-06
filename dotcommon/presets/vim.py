from dotcommon.util import strip
from dotcommon.preset import preset

paths = (".vimrc", "vimrc", ".vim/vimrc")

@preset(paths)
def set_statements(text):
    lines = text.splitlines()
    for line in lines:
        stripped = strip(line, '"')
        if stripped.startswith("set"):
            yield stripped
