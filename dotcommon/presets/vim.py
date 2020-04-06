from dotcommon.util import lines_starting_with

paths = (".vimrc", "vimrc", ".vim/vimrc")

set_statements = lines_starting_with("set", '"'), paths
