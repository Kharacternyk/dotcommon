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
``bspc rule -a Screenkey manage=off``                        302
``bspc rule -a Kupfer.py focus=on``                          256
``bspc rule -a mplayer2 state=floating``                     218
``bspc rule -a Gimp desktop='^8' state=floating follow=on``  185
``bspc rule -a Chromium desktop='^2'``                       155
``bspc rule -a Emacs state=tiled``                            54
``bspc rule -a Zathura state=tiled``                          53
``bspc rule -a Chromium desktop=^2``                          41
``bspc rule -a mplayer2 floating=on``                         40
``bspc rule -a Gimp desktop=^8 follow=on floating=on``        37
===========================================================  ===


Window gap/border width
~~~~~~~~~~~~~~~~~~~~~~~


===============  ===
``21/2``         163
``unset/unset``  100
``0/2``           52
``01/2``          45
``0/1``           29
``5/2``           25
``21/3``          19
``21/1``          18
``21/0``          17
``unset/2``       17
===============  ===


Vim
---


Set statements
~~~~~~~~~~~~~~


====================  ===
``set expandtab``     578
``set nocompatible``  555
``set number``        511
``set hlsearch``      486
``set incsearch``     472
``set laststatus=2``  426
``set shiftwidth=4``  382
``set ignorecase``    378
``set tabstop=4``     371
``set ruler``         362
====================  ===


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ===
``Plugin 'VundleVim/Vundle.vim'``            103
``Plugin 'scrooloose/nerdtree'``              74
``Plugin 'tpope/vim-fugitive'``               66
``Plugin 'gmarik/Vundle.vim'``                51
``Plugin 'vim-airline/vim-airline'``          44
``Plugin 'Valloric/YouCompleteMe'``           43
``Plugin 'tpope/vim-surround'``               39
``Plugin 'scrooloose/syntastic'``             37
``Plugin 'vim-airline/vim-airline-themes'``   36
``Plugin 'majutsushi/tagbar'``                33
===========================================  ===


Vim-plug plugins
~~~~~~~~~~~~~~~~


=========================================  ==
``Plug 'tpope/vim-fugitive'``              75
``Plug 'scrooloose/nerdtree'``             62
``Plug 'tpope/vim-surround'``              52
``Plug 'vim-airline/vim-airline'``         50
``Plug 'airblade/vim-gitgutter'``          47
``Plug 'vim-airline/vim-airline-themes'``  39
``Plug 'junegunn/fzf.vim'``                32
``Plug 'tpope/vim-commentary'``            32
``Plug 'scrooloose/nerdcommenter'``        31
``Plug 'majutsushi/tagbar'``               28
=========================================  ==


Custom functions per vimrc
~~~~~~~~~~~~~~~~~~~~~~~~~~


======  ===
``0``   702
``1``   135
``2``    53
``5``    32
``4``    23
``3``    22
``6``    10
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

