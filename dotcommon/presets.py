from dotcommon.util import lines_starting_with


class Bash:
    paths = (".bashrc", "bashrc")

    @lines_starting_with("Readline macros", "bind ", "#")
    def readline_macros():
        pass

    @lines_starting_with("Aliases", "alias ", "#")
    def aliases():
        pass

    @lines_starting_with("Exports", "export ", "#")
    def exports():
        pass

    atomizers = readline_macros, aliases, exports
    preset = paths, atomizers


class Vim:
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
