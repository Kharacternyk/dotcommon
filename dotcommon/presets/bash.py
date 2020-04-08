"Bash"

from dotcommon.util import lines_starting_with

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
