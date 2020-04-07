from dotcommon.util import lines_starting_with, preset, strip

bash_paths = (".bashrc", "bashrc")
bash_readline_macros = lines_starting_with("bind", "#", bash_paths)
bash_aliases = lines_starting_with("alias", "#", bash_paths)
bash_exports = lines_starting_with("export", "#", bash_paths)

vim_paths = (".vimrc", "vimrc", ".vim/vimrc", "vim/.vimrc", "vim/vimrc")
vim_set_statements = lines_starting_with("set", '"', vim_paths)
vim_vundle = lines_starting_with("Plugin", '"', vim_paths)
vim_plug = lines_starting_with("Plug ", '"', vim_paths)
