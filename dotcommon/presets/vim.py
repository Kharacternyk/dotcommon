"Vim"

from dotcommon.util import lines_starting_with

paths = (".vimrc", "vimrc", ".vim/vimrc", "vim/.vimrc", "vim/vimrc")


@lines_starting_with("Set statements", "set ", '"')
def set_statements():
    pass


@lines_starting_with("Vundle plugins", "Plugin ", '"')
def vundle():
    pass


@lines_starting_with("Vim-plug plugins", "Plug ", '"')
def plug():
    pass


atomizers = set_statements, vundle, plug
preset = paths, atomizers
