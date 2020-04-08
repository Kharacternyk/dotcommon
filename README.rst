dotcommon is a crawler that is built to answer questions
*What are the most popular Bash aliases?*,
*What are the most popular Vundle plugins for Vim?*, etc.
It crawls 500 of the most starred GitHub repos that match topic
``dotfiles`` and counts such things.

.. contents:: Here are top-tens of various things:

Bash
----

75 configs were found.

Readline macros
~~~~~~~~~~~~~~~


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
~~~~~~~


========================================================================================================================================================================  =
``alias ls='ls --color=auto'``                                                                                                                                            8
``alias grep='grep --color=auto'``                                                                                                                                        7
``alias ..='cd ..'``                                                                                                                                                      7
``alias ll='ls -alF'``                                                                                                                                                    7
``alias la='ls -A'``                                                                                                                                                      7
``alias l='ls -CF'``                                                                                                                                                      7
``alias cp='cp -i'``                                                                                                                                                      6
``alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'``  5
``alias mv='mv -i'``                                                                                                                                                      5
``alias fgrep='fgrep --color=auto'``                                                                                                                                      5
========================================================================================================================================================================  =


Exports
~~~~~~~


=================================================  =
``export EDITOR=vim``                              6
``export HISTSIZE=10000``                          5
``export LESS="-R"``                               4
``export EDITOR="vim"``                            4
``export HISTCONTROL=erasedups``                   4
``export PATH``                                    4
``export HISTCONTROL=ignoreboth:erasedups``        3
``export HISTTIMEFORMAT="%Y/%m/%d %H:%M:%S:   "``  3
``export GREP_COLOR="1;31"``                       3
``export QT_QPA_PLATFORMTHEME=qt5ct``              3
=================================================  =


PS1
~~~


=======================================================================================================================================================================================  =
``PS1='[\u@\h \W]\$ '``                                                                                                                                                                  2
``PS1='[\[\033[1;31m\]\u\[\033[0m\]@\H \w]$ '``                                                                                                                                          1
``PS1='\[[01;32m\]\u@\h\[[00m\]:\[[01;34m\]\w\[[00m\] \[[01;33m\]$(parse_git_branch)\[[00m\]\$ '``                                                                                                                        1
``PS1="\[$BOLD_GREEN\][\[$BOLD_YELLOW\]\u\[$BOLD_GREEN\]@\[$BOLD_BLUE\]\h:\[$BOLD_RED\]"'`pwd`'"\[$BOLD_GREEN\]] "'`git_branch`'" \[$GRAY\]\t\n\[$BOLD_GREEN\]"'\$'"\[$COLOR_NONE\] "``  1
``PS1="$WHITE\W\$(__git_ps1 ' (%s)') $BLUEλ $WHITE"``                                                                                                                                    1
``PS1="\[\e[0;31m\]┌─╼[\[\e[m\]\w\[\e[0;31m\]] \$SSH_PS1\$TOOLBOX_PS1\$GIT_PS1``                                                                                                         1
``PS1="\n \[\033[0;34m\]┌─────(\[\033[1;35m\]\u\[\033[0;34m\])─────(\[\033[1;32m\]\w\[\033[0;34m\]) \n └> \[\033[1;36m\]\$ \[\033[0m\]"``                                                1
``PS1="\[${yellow}\]\w\[${red}\]\$(__git_ps1)\n\[${green}\]$ \[${color_off}\]"``                                                                                                         1
``PS1='\W \[\e[1;32m\]\$\[\e[m\] '``                                                                                                                                                     1
``PS1="\u@\[\e[1;30m\]\h\[\e[0m\]:\[\e[0;33m\]\w\[$txtcyn\]\$git_branch\[$txtred\]\$git_dirty\[\e[0;34m\]%\[\e[0m\] "``                                                                  1
=======================================================================================================================================================================================  =


Vim
---

167 configs were found.

Set statements
~~~~~~~~~~~~~~


====================  ===
``set incsearch``     109
``set ignorecase``    105
``set expandtab``     100
``set laststatus=2``   99
``set hlsearch``       98
``set autoindent``     96
``set number``         94
``set smartcase``      92
``set nocompatible``   89
``set showcmd``        78
====================  ===


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ==
``Plugin 'scrooloose/nerdtree'``             19
``Plugin 'tpope/vim-fugitive'``              15
``Plugin 'VundleVim/Vundle.vim'``            13
``Plugin 'vim-airline/vim-airline'``         13
``Plugin 'airblade/vim-gitgutter'``          11
``Plugin 'vim-airline/vim-airline-themes'``  11
``Plugin 'tpope/vim-surround'``              10
``Plugin 'scrooloose/syntastic'``             9
``Plugin 'gmarik/Vundle.vim'``                9
``Plugin 'Raimondi/delimitMate'``             7
===========================================  ==


Vim-plug plugins
~~~~~~~~~~~~~~~~


=================================  ==
``Plug 'tpope/vim-fugitive'``      43
``Plug 'tpope/vim-surround'``      33
``Plug 'tpope/vim-repeat'``        24
``Plug 'airblade/vim-gitgutter'``  23
``Plug 'junegunn/fzf.vim'``        22
``Plug 'tpope/vim-commentary'``    19
``Plug 'w0rp/ale'``                19
``Plug 'tpope/vim-unimpaired'``    18
``Plug 'tpope/vim-endwise'``       16
``Plug 'tpope/vim-abolish'``       15
=================================  ==


Custom functions per vimrc
~~~~~~~~~~~~~~~~~~~~~~~~~~


======  ==
``0``   75
``1``   29
``2``   12
``3``   11
``4``    8
``8``    7
``11``   4
``9``    4
``6``    3
``5``    3
======  ==


Xorg
----

40 configs were found.

Window managers
~~~~~~~~~~~~~~~


====================================================================  ==
``exec i3``                                                           14
``exec bspwm``                                                         5
``exec xmonad``                                                        2
``exec dwm``                                                           1
``exec openbox-session``                                               1
``exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &``   1
``exec "$@"``                                                          1
``exec "$wm"``                                                         1
``exec awesome --no-argb &> /tmp/awesome.log``                         1
``exec dbus-launch i3``                                                1
====================================================================  ==

