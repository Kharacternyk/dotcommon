dotcommon is a crawler that is built to answer questions
*What are the most popular Bash aliases?*,
*What are the most popular Vundle plugins for Vim?*, etc.
It crawls the most starred GitHub repos that match topic
``dotfiles`` and counts such things.

.. contents:: Navigation:


Vim
------------------

4 configs were found.

Set statements
~~~~~~~~~~~~~~~~~~~~~

==============================  =
set nocompatible                3
set wildmenu                    3
set backspace=indent,eol,start  3
set hlsearch                    3
set ignorecase                  3
set laststatus=2                3
set mouse=a                     3
set nostartofline               3
set ruler                       3
set background=dark             2
==============================  =

Vundle plugins
~~~~~~~~~~~~~~~~~~~~~



Vim-plug plugins
~~~~~~~~~~~~~~~~~~~~~

========================================  =
Plug 'ap/vim-css-color'                   1
Plug 'bling/vim-airline'                  1
Plug 'FelikZ/ctrlp-py-matcher'            1
Plug 'guns/vim-clojure-static'            1
Plug 'joker1007/vim-ruby-heredoc-syntax'  1
Plug 'junegunn/vim-easy-align'            1
Plug 'junegunn/vim-emoji'                 1
Plug 'junegunn/goyo.vim'                  1
Plug 'kchmck/vim-coffee-script'           1
Plug 'ctrlpvim/ctrlp.vim'                 1
========================================  =


Bash
------------------

3 configs were found.

Readline macros
~~~~~~~~~~~~~~~~~~~~~



Aliases
~~~~~~~~~~~~~~~~~~~~~

====================================================================================================================================================================  =
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'  1
alias ssh="gpg-connect-agent updatestartuptty /bye >/dev/null; ssh"                                                                                                   1
====================================================================================================================================================================  =

Exports
~~~~~~~~~~~~~~~~~~~~~

==============  =
export GPG_TTY  1
==============  =

