from dotcommon.util import lines_starting_with
from dotcommon.preset import preset

paths = (".vimrc", "vimrc", ".vim/vimrc")

set_statements = lines_starting_with("set", '"'), paths
