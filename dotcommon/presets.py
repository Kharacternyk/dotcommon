from dotcommon.util import lines_starting_with

bash_paths = (".bashrc", "bashrc")
bash_readline_macros = lines_starting_with("bind", "#")
bash_aliases = lines_starting_with("alias", "#")
bash_exports = lines_starting_with("export", "#")

vim_paths = (".vimrc", "vimrc", ".vim/vimrc", "vim/.vimrc", "vim/vimrc")
vim_set_statements = lines_starting_with("set", '"')
vim_vundle = lines_starting_with("Plugin", '"')
vim_plug = lines_starting_with("Plug ", '"')
