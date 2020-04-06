from dotcommon.util import lines_starting_with

bash_paths = (".bashrc", "bashrc")
bash_readline_macros = lines_starting_with("bind", "#"), bash_paths
bash_aliases = lines_starting_with("alias", "#"), bash_paths

vim_paths = (".vimrc", "vimrc", ".vim/vimrc")
vim_set_statements = lines_starting_with("set", '"'), vim_paths
