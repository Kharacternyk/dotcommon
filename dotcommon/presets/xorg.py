"Xorg"

from dotcommon.util import lines_starting_with

paths = (".xinitrc", "xinitrc")


@lines_starting_with("Window managers", "exec ", "#")
def window_managers():
    pass


atomizers = window_managers,
preset = paths, atomizers
