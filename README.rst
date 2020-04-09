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


bspwm
-----


Window rules
~~~~~~~~~~~~


===========================================================  ===
``bspc rule -a Screenkey manage=off``                        299
``bspc rule -a Kupfer.py focus=on``                          247
``bspc rule -a mplayer2 state=floating``                     207
``bspc rule -a Gimp desktop='^8' state=floating follow=on``  182
``bspc rule -a Chromium desktop='^2'``                       152
``bspc rule -a Zathura state=tiled``                          57
``bspc rule -a Emacs state=tiled``                            56
``bspc rule -a mplayer2 floating=on``                         46
``bspc rule -a Gimp desktop=^8 follow=on floating=on``        45
``bspc rule -a mpv state=floating``                           35
===========================================================  ===


Window gap/border width
~~~~~~~~~~~~~~~~~~~~~~~


===============  ===
``12/2``         180
``unset/unset``  103
``10/2``          42
``0/1``           35
``5/2``           30
``0/2``           29
``12/4``          20
``8/2``           20
``0/0``           19
``12/0``          17
===============  ===


Vim
---


Set statements
~~~~~~~~~~~~~~


=======================  ===
``set expandtab``        462
``set number``           399
``set nocompatible``     350
``set hlsearch``         341
``set laststatus=2``     323
``set shiftwidth=4``     316
``set tabstop=4``        303
``set incsearch``        289
``set autoindent``       273
``set background=dark``  252
=======================  ===


<leader> key mappings
~~~~~~~~~~~~~~~~~~~~~


==============================  ===
``let mapleader = ","``         104
``let mapleader=","``            59
``let mapleader = "\<Space>"``   25
``let mapleader = " "``          18
``let mapleader=','``            16
``let mapleader = ','``          15
``let mapleader=" "``            10
``let mapleader="\<Space>"``      6
``let mapleader = ' '``           4
``let mapleader=";"``             4
==============================  ===


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ===
``Plugin 'VundleVim/Vundle.vim'``            104
``Plugin 'scrooloose/nerdtree'``              70
``Plugin 'tpope/vim-fugitive'``               64
``Plugin 'gmarik/Vundle.vim'``                48
``Plugin 'vim-airline/vim-airline'``          45
``Plugin 'Valloric/YouCompleteMe'``           41
``Plugin 'vim-airline/vim-airline-themes'``   35
``Plugin 'tpope/vim-surround'``               34
``Plugin 'scrooloose/syntastic'``             32
``Plugin 'majutsushi/tagbar'``                30
===========================================  ===


Vim-plug plugins
~~~~~~~~~~~~~~~~


=========================================  ==
``Plug 'tpope/vim-fugitive'``              70
``Plug 'scrooloose/nerdtree'``             59
``Plug 'tpope/vim-surround'``              49
``Plug 'vim-airline/vim-airline'``         48
``Plug 'airblade/vim-gitgutter'``          45
``Plug 'vim-airline/vim-airline-themes'``  36
``Plug 'tpope/vim-commentary'``            32
``Plug 'junegunn/fzf.vim'``                31
``Plug 'scrooloose/nerdcommenter'``        29
``Plug 'majutsushi/tagbar'``               25
=========================================  ==


Custom functions per vimrc
~~~~~~~~~~~~~~~~~~~~~~~~~~


======  ===
``0``   700
``1``   135
``2``    54
``5``    32
``4``    23
``3``    22
``6``    11
``8``     7
``7``     6
``11``    5
======  ===


Xorg
----


Window managers
~~~~~~~~~~~~~~~


========================  ===
``exec i3``               268
``exec bspwm``             57
``exec xmonad``            47
``exec dwm``               44
``exec awesome``           39
``exec $(get_session)``    36
``exec openbox-session``   26
``exec startxfce4``        18
``exec startkde``          11
``exec dbus-launch i3``     7
========================  ===

