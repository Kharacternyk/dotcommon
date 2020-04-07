from dotcommon.util import lines_starting_with, preset, strip

bash_paths = (".bashrc", "bashrc")
bash_readline_macros = lines_starting_with("bind", "#"), bash_paths
bash_aliases = lines_starting_with("alias", "#"), bash_paths

vim_paths = (".vimrc", "vimrc", ".vim/vimrc", "vim/.vimrc", "vim/vimrc")
vim_set_statements = lines_starting_with("set", '"'), vim_paths


@preset(vim_paths)
def vim_maps(text):
    lines = text.splitlines()
    for line in lines:
        stripped = strip(line, '"')
        space_index = line.find(" ")
        if space_index != -1 and stripped[:space_index].endswith("map"):
            yield stripped

vim_vundle = lines_starting_with("Plugin", '"'), vim_paths
vim_plug = lines_starting_with("Plug ", '"'), vim_paths
