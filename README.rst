dotcommon is a crawler that is built to answer questions
*What are the most popular Bash aliases?*,
*What are the most popular Vundle plugins for Vim?*, etc.
It crawls 250 the most starred GitHub repos that match topic
``dotfiles`` and counts such things.

.. contents:: Here are top-tens of various things:


Vim
------------------

73 configs were found.

Set statements
~~~~~~~~~~~~~~~~~~~~~

====================  ==
``set incsearch``     47
``set ignorecase``    44
``set laststatus=2``  43
``set hlsearch``      42
``set expandtab``     41
``set nocompatible``  39
``set number``        38
``set smartcase``     38
``set autoindent``    36
``set wildmenu``      35
====================  ==

Vundle plugins
~~~~~~~~~~~~~~~~~~~~~

===========================================  =
``Plugin 'scrooloose/nerdtree'``             9
``Plugin 'VundleVim/Vundle.vim'``            7
``Plugin 'airblade/vim-gitgutter'``          7
``Plugin 'vim-airline/vim-airline'``         7
``Plugin 'tpope/vim-fugitive'``              6
``Plugin 'tpope/vim-surround'``              6
``Plugin 'vim-airline/vim-airline-themes'``  6
``Plugin 'scrooloose/syntastic'``            4
``Plugin 'SirVer/ultisnips'``                4
``Plugin 'Valloric/YouCompleteMe'``          4
===========================================  =

Vim-plug plugins
~~~~~~~~~~~~~~~~~~~~~

==================================  ==
``Plug 'tpope/vim-fugitive'``       18
``Plug 'tpope/vim-surround'``       12
``Plug 'tpope/vim-repeat'``          9
``Plug 'tpope/vim-unimpaired'``      7
``Plug 'airblade/vim-gitgutter'``    7
``Plug 'w0rp/ale'``                  7
``Plug 'junegunn/vim-easy-align'``   6
``Plug 'pangloss/vim-javascript'``   6
``Plug 'junegunn/fzf.vim'``          6
``Plug 'junegunn/goyo.vim'``         5
==================================  ==


Bash
------------------

40 configs were found.

Readline macros
~~~~~~~~~~~~~~~~~~~~~

============================================================  =
``bind "set completion-ignore-case on"``                      1
``bind "set show-all-if-ambiguous on"``                       1
``bind -x '"\C-p": fvim'``                                    1
``bind -m vi-insert '"\C-x\C-e": edit-and-execute-command'``  1
``bind -m vi-command '"\C-w": emacs-editing-mode'``           1
``bind -m vi-insert '"\C-w": emacs-editing-mode'``            1
``bind -m emacs-standard '"\C-w": vi-editing-mode'``          1
``bind -m vi-insert '"jj": vi-movement-mode'``                1
``bind -m vi-insert '"\C-p": previous-history'``              1
``bind -m vi-insert '"\C-n": next-history'``                  1
============================================================  =

Aliases
~~~~~~~~~~~~~~~~~~~~~

========================================================================================================================================================================  =
``alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'``  4
``alias grep='grep --color=auto'``                                                                                                                                        4
``alias ..='cd ..'``                                                                                                                                                      4
``alias ll='ls -alF'``                                                                                                                                                    4
``alias ls='ls --color=auto'``                                                                                                                                            4
``alias la='ls -A'``                                                                                                                                                      3
``alias l='ls -CF'``                                                                                                                                                      3
``alias cp='cp -i'``                                                                                                                                                      2
``alias vi='vim'``                                                                                                                                                        2
``alias tmux="tmux -2"``                                                                                                                                                  2
========================================================================================================================================================================  =

Exports
~~~~~~~~~~~~~~~~~~~~~

=================================================  =
``export EDITOR=vim``                              5
``export HISTSIZE=10000``                          4
``export HISTTIMEFORMAT="%Y/%m/%d %H:%M:%S:   "``  3
``export HISTCONTROL=erasedups``                   3
``export HISTSIZE=``                               3
``export GPG_TTY``                                 2
``export PAGER=less``                              2
``export HISTCONTROL=ignoreboth:erasedups``        2
``export HISTSIZE=50000``                          2
``export HISTFILESIZE=50000``                      2
=================================================  =

PS1
~~~~~~~~~~~~~~~~~~~~~

=======================================================================================================================================================================================  =
``PS1='[\[\033[1;31m\]\u\[\033[0m\]@\H \w]$ '``                                                                                                                                          1
``PS1='\[[01;32m\]\u@\h\[[00m\]:\[[01;34m\]\w\[[00m\] \[[01;33m\]$(parse_git_branch)\[[00m\]\$ '``                                                                                                                        1
``PS1="\[$BOLD_GREEN\][\[$BOLD_YELLOW\]\u\[$BOLD_GREEN\]@\[$BOLD_BLUE\]\h:\[$BOLD_RED\]"'`pwd`'"\[$BOLD_GREEN\]] "'`git_branch`'" \[$GRAY\]\t\n\[$BOLD_GREEN\]"'\$'"\[$COLOR_NONE\] "``  1
``PS1="$WHITE\W\$(__git_ps1 ' (%s)') $BLUEλ $WHITE"``                                                                                                                                    1
``PS1="\[\e[0;31m\]┌─╼[\[\e[m\]\w\[\e[0;31m\]] \$SSH_PS1\$TOOLBOX_PS1\$GIT_PS1``                                                                                                         1
``PS1="\n \[\033[0;34m\]┌─────(\[\033[1;35m\]\u\[\033[0;34m\])─────(\[\033[1;32m\]\w\[\033[0;34m\]) \n └> \[\033[1;36m\]\$ \[\033[0m\]"``                                                1
``PS1="\[${yellow}\]\w\[${red}\]\$(__git_ps1)\n\[${green}\]$ \[${color_off}\]"``                                                                                                         1
``PS1='\W \[\e[1;32m\]\$\[\e[m\] '``                                                                                                                                                     1
``PS1="\u@\[\e[1;30m\]\h\[\e[0m\]:\[\e[0;33m\]\w\[$txtcyn\]\$git_branch\[$txtred\]\$git_dirty\[\e[0;34m\]%\[\e[0m\] "``                                                                  1
``PS1='[\u@\h \W]\$ '``                                                                                                                                                                  1
=======================================================================================================================================================================================  =


Xorg
------------------

17 configs were found.

Window managers
~~~~~~~~~~~~~~~~~~~~~

====================================================================  =
``exec i3``                                                           5
``exec xmonad``                                                       2
``exec dwm``                                                          1
``exec openbox-session``                                              1
``exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &``  1
``exec bspwm``                                                        1
``exec "$@"``                                                         1
``exec "$wm"``                                                        1
``exec awesome --no-argb &> /tmp/awesome.log``                        1
====================================================================  =

