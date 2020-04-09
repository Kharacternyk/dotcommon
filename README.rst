dotcommon is a crawler that is built to answer questions
*What are the most popular Bash aliases?*,
*What are the most popular Vundle plugins for Vim?*, etc.
It searches GitHub for configs and counts such things.

.. contents:: Here are top-tens of various things:

Bash
----


Aliases
~~~~~~~


========================================================================================================================================================================  ===
``alias la='ls -A'``                                                                                                                                                      263
``alias l='ls -CF'``                                                                                                                                                      244
``alias ll='ls -alF'``                                                                                                                                                    241
``alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'``  195
``alias ls='ls --color=auto'``                                                                                                                                             83
``alias rm='rm -i'``                                                                                                                                                       52
``alias ..='cd ..'``                                                                                                                                                       49
``alias ll='ls -l'``                                                                                                                                                       42
``alias grep='grep --color=auto'``                                                                                                                                         42
``alias cp='cp -i'``                                                                                                                                                       40
========================================================================================================================================================================  ===


Exports
~~~~~~~


=================================  ==
``export EDITOR=vim``              70
``export CLICOLOR=1``              34
``export NVM_DIR="$HOME/.nvm"``    29
``export HISTCONTROL=ignoreboth``  24
``export VISUAL=vim``              21
``export HISTSIZE=10000``          21
``export PATH``                    20
``export EDITOR="vim"``            20
``export EDITOR='vim'``            15
``export LANG=en_US.UTF-8``        15
=================================  ==


PS1
~~~


==============================================================================================================================  ==
``PS1='[\u@\h \W]\$ '``                                                                                                         44
``PS1="${TITLEBAR}\``                                                                                                            4
``PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '``                    3
``PS1="$LIGHT_GRAY\$(date +%H:%M) \w$YELLOW \$(parse_git_branch)$LIGHT_GREEN\$ $LIGHT_GRAY"``                                    3
``PS1='`[ $? = 0 ] && echo "\[\033[01;34m\]✔\[\033[00m\]"\``                                                                     2
``PS1='`[ $? = 0 ] && echo "\[\033[01;34m\]✔\[\033[00m\]" ||\``                                                                  2
``PS1="$PS1\n\$ "``                                                                                                              2
``PS1='\h:\W$(__git_ps1 "(%s)") \u\$ '``                                                                                         2
``PS1="\[$GREEN\]\t\[$RED\]-\[$YELLOW\]\u@\h:\[$BLUE\]\[$BLUE\]\w\[\033[m\]\[$GREEN\]\$(parse_git_branch)\[$NO_COLOR\]\n\$ "``   2
``PS1="\w$YELLOW\$(parse_git_branch)$NO_COLOR\$ "``                                                                              2
==============================================================================================================================  ==


PS2
~~~


============================================  =
``PS2='> '``                                  4
``PS2='\[${C_PINK}\]>>> \[${C_COMMANDE}\]'``  2
``PS2="\[${yellow}\]-> \[${reset}\]";``       1
``PS2="loop \$ "``                            1
============================================  =


Radline macros
~~~~~~~~~~~~~~


==========================================  =
``bind '"\e[A": history-search-backward'``  8
``bind '"\e[B": history-search-forward'``   8
``bind "set completion-ignore-case on"``    7
``bind 'set completion-ignore-case on'``    4
``bind 'set show-all-if-ambiguous on'``     3
``bind "set show-all-if-ambiguous on"``     3
``bind '"[A":history-search-backward'``                                             2
``bind '"[B":history-search-forward'``                                             2
``bind 'set visible-stats on'``             2
``bind 'Space:magic-space'``                2
==========================================  =


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


sxhkd
-----


Commands bound to keybinds
~~~~~~~~~~~~~~~~~~~~~~~~~~


=========================================================  ===
``pkill -USR1 -x sxhkd``                                   142
``bspc desktop -l next``                                   111
``bspc node -{f,s} {west,south,north,east}``                88
``bspc node -p {west,south,north,east}``                    87
``bspc node -p cancel``                                     83
``bspc node -o 0.{1-9}``                                    81
``bspc node -t {tiled,pseudo_tiled,floating,fullscreen}``   80
``bspc quit``                                               77
``bspc node -{c,k}``                                        75
``rofi -show run``                                          73
=========================================================  ===


Commands bound to keybinds (except bspc)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============================  ===
``pkill -USR1 -x sxhkd``      142
``rofi -show run``             73
``firefox``                    56
``urxvt``                      55
``mpc toggle``                 42
``termite``                    40
``amixer set Master toggle``   40
``xbacklight -dec 10``         38
``xbacklight -inc 10``         36
``urxvtc``                     35
============================  ===


Vim
---


Set statements
~~~~~~~~~~~~~~


=======================  ===
``set expandtab``        465
``set number``           398
``set nocompatible``     353
``set hlsearch``         344
``set laststatus=2``     326
``set shiftwidth=4``     317
``set tabstop=4``        304
``set incsearch``        289
``set autoindent``       272
``set background=dark``  255
=======================  ===


<leader> key mappings
~~~~~~~~~~~~~~~~~~~~~


==============================================  ===
``,``                                           196
`` ``                                            36
``\<Space>``                                     32
``;``                                             8
````                                              6
``pleader="," " leader is comm``                  2
``\\``                                            2
``-``                                             2
``\<space>``                                      2
``=" "          " one space as the map leade``    1
==============================================  ===


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ===
``Plugin 'VundleVim/Vundle.vim'``            100
``Plugin 'scrooloose/nerdtree'``              69
``Plugin 'tpope/vim-fugitive'``               63
``Plugin 'gmarik/Vundle.vim'``                48
``Plugin 'vim-airline/vim-airline'``          44
``Plugin 'Valloric/YouCompleteMe'``           40
``Plugin 'vim-airline/vim-airline-themes'``   35
``Plugin 'tpope/vim-surround'``               34
``Plugin 'scrooloose/syntastic'``             31
``Plugin 'majutsushi/tagbar'``                29
===========================================  ===


Vim-plug plugins
~~~~~~~~~~~~~~~~


=========================================  ==
``Plug 'tpope/vim-fugitive'``              70
``Plug 'scrooloose/nerdtree'``             60
``Plug 'tpope/vim-surround'``              49
``Plug 'vim-airline/vim-airline'``         47
``Plug 'airblade/vim-gitgutter'``          45
``Plug 'vim-airline/vim-airline-themes'``  35
``Plug 'junegunn/fzf.vim'``                30
``Plug 'tpope/vim-commentary'``            30
``Plug 'scrooloose/nerdcommenter'``        29
``Plug 'majutsushi/tagbar'``               25
=========================================  ==


Custom functions per vimrc
~~~~~~~~~~~~~~~~~~~~~~~~~~


======  ===
``0``   704
``1``   134
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

