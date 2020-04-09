dotcommon is a crawler that is built to answer questions
*What are the most popular Bash aliases?*,
*What are the most popular Vundle plugins for Vim?*, etc.
It crawls 2000 of top results of GitHub search.

.. contents:: Here are top-tens of various things:

Bash
----


Readline macros
~~~~~~~~~~~~~~~


==========================================  =
``bind '"\e[A": history-search-backward'``  9
``bind '"\e[B": history-search-forward'``   9
``bind "set completion-ignore-case on"``    4
``bind 'set completion-ignore-case on'``    3
``bind -m vi-insert "\C-l":clear-screen``   3
``bind C-l:clear-screen``                   2
``bind '"\eOA": history-search-backward'``  2
``bind '"\eOB": history-search-forward'``   2
``bind -x '"\C-p": vim $(fzf);'``           2
``bind '"\e[1~": beginning-of-line'``       2
==========================================  =


Aliases
~~~~~~~


========================================================================================================================================================================  ===
``alias la='ls -A'``                                                                                                                                                      297
``alias l='ls -CF'``                                                                                                                                                      286
``alias ll='ls -alF'``                                                                                                                                                    282
``alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'``  222
``alias ls='ls --color=auto'``                                                                                                                                             75
``alias rm='rm -i'``                                                                                                                                                       67
``alias mv='mv -i'``                                                                                                                                                       57
``alias cp='cp -i'``                                                                                                                                                       54
``alias grep='grep --color=auto'``                                                                                                                                         46
``alias ..='cd ..'``                                                                                                                                                       46
========================================================================================================================================================================  ===


Exports
~~~~~~~


======================================  ==
``export EDITOR=vim``                   52
``export HISTCONTROL=ignoreboth``       34
``export CLICOLOR=1``                   34
``export NVM_DIR="$HOME/.nvm"``         32
``export PATH="$PATH:$HOME/.rvm/bin"``  25
``export HISTCONTROL=ignoredups``       21
``export EDITOR='vim'``                 20
``export LANG=en_US.UTF-8``             20
``export EDITOR="vim"``                 19
``export HISTSIZE=10000``               18
======================================  ==


PS1
~~~


===================================================================================================================================================================================================  ==
``PS1='[\u@\h \W]\$ '``                                                                                                                                                                              29
``PS1="$LIGHT_GRAY\$(date +%H:%M) \w$YELLOW \$(parse_git_branch)$LIGHT_GREEN\$ $LIGHT_GRAY"``                                                                                                         3
``PS1="${TITLEBAR}\``                                                                                                                                                                                 3
``PS1='\[\e[$RED\]\u\[\e[$LGREEN\]@\[\e[$BROWN\]\h\[\e[$LBLUE\] \w \$\[\e[$WHITE\] '``                                                                                                                2
``PS1="${GREEN}\w${END}${GIT_BR_TAG}${BLUE}$ ${END}"``                                                                                                                                                2
``PS1='\[\e[1;30m\][\[\e[m\e[0;31m\]\D{%m-%d %H:%M}\[\e[m\e[1;30m\]][\[\e[m\e[0;32m\]\u\[\e[m\e[1;30m\]@\[\e[m\e[0;34m\]\h\[\e[m\e[1;30m\]]\[\e[m\] \w\$ '``                                          2
``PS1='\[\033[1;35m\]\t\[\033[0;36m\]::\[\033[1;31m\]\u \[\033[0;36m\]{ \[\033[01;34m\]\w \[\033[0;36m\]} $(__git_ps1 "{ \[\033[01;34m\]%s \[\033[0;36m\]}") \n\[\033[1;35m\]-> $ \[\033[0;30m\]'``   2
``PS1="\h:\W\$(grb_git_prompt) \u\$ "``                                                                                                                                                               2
``PS1='└──── '``                                                                                                                                                                                      2
``PS1=${lt_blue}'\u'${norm}'@'${HOSTCOLOUR}'\h '${norm}'['${green}'\@'${norm}'] '${yellow}'\w\n'${norm}'${ERROR_FLAG:+'${lt_red}'}\$${ERROR_FLAG:+'${norm}'} '``                                      2
===================================================================================================================================================================================================  ==


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

