from dotcommon.util import lines_starting_with


class Bash:
    paths = (".bashrc", "bashrc")

    readline_macros = lines_starting_with("bind", "#")
    aliases = lines_starting_with("alias", "#")
    exports = lines_starting_with("export", "#")

    atomizers = readline_macros, aliases, exports
    preset = paths, atomizers


class Vim:
    paths = (".vimrc", "vimrc", ".vim/vimrc", "vim/.vimrc", "vim/vimrc")

    set_statements = lines_starting_with("set", '"')
    vundle = lines_starting_with("Plugin", '"')
    plug = lines_starting_with("Plug ", '"')

    atomizers = set_statements, vundle, plug
    preset = paths, atomizers
