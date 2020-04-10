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
``alias la='ls -A'``                                                                                                                                                      183
``alias l='ls -CF'``                                                                                                                                                      178
``alias ll='ls -alF'``                                                                                                                                                    158
``alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'``  144
``alias ls='ls --color=auto'``                                                                                                                                             83
``alias grep='grep --color=auto'``                                                                                                                                         48
``alias ..='cd ..'``                                                                                                                                                       38
``alias gs='git status'``                                                                                                                                                  36
``alias mv='mv -i'``                                                                                                                                                       34
``alias rm='rm -i'``                                                                                                                                                       30
========================================================================================================================================================================  ===


Exports
~~~~~~~


==========================================================================================  ==
``export EDITOR=vim``                                                                       74
``export NVM_DIR="$HOME/.nvm"``                                                             50
``export PATH``                                                                             33
``export CLICOLOR=1``                                                                       30
``export TERM=xterm-256color``                                                              27
``export LC_ALL=en_US.UTF-8``                                                               25
``export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'``  23
``export VISUAL=vim``                                                                       23
``export LANG=en_US.UTF-8``                                                                 22
``export HISTCONTROL=ignoreboth``                                                           19
==========================================================================================  ==


PS1
~~~


=============================================================================================================================================================================================  ==
``PS1='[\u@\h \W]\$ '``                                                                                                                                                                        29
``PS1="$"``                                                                                                                                                                                    28
``PS1='[\u@\h \w \t \# ]\$ '``                                                                                                                                                                  2
``PS1='\[\e[01;31m\]\h\[\e[01;34m\] \W \$\[\e[00m\] '``                                                                                                                                         2
``PS1=' \w \$ '``                                                                                                                                                                               2
``PS1="$DGY_ON_GY\W $BU_ON_GY$NO_COLOR\$(~/bin/prompt_git.sh)\$ "``                                                                                                                             2
``PS1='${debian_chroot:+($debian_chroot)}\[\033[01;30m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$\n'``                                                2
``PS1="\n\[\e[0;34m\]┌─[\[\e[1;36m\u\e[0;34m\]]──[\e[1;37m\w\e[0;34m]──[\[\e[1;36m\]${HOSTNAME%%.*}\[\e[0;34m\]]\[\e[1;35m\]: \$\[\e[0;34m\]\n\[\e[0;34m\]└─╼ \[\e[1;35m\]>> \[\e[00;00m\]"``   2
``PS1="${COLOR_RED}\$(SELECT)${COLOR_GREEN}\\w ${COLOR_PURPLE}\$(precmd)${COLOR_RESET}``                                                                                                        2
``PS1="$G┌─[$BR\u$G]$BY@$G[$BW${HOSTNAME%%.*}$G]$B:\w\n$G└──>$BR \\$ $NONE"``                                                                                                                   2
=============================================================================================================================================================================================  ==


PS2
~~~


==============================================================  =
``PS2="loop \$ "``                                              1
``PS2='             \[\033[1m\]>>\[\033[0m\] '``                1
``PS2="\[$(tput setaf 51)\]$(tput bold)└─‖ \[$(tput sgr0)\]"``  1
``PS2="\[${fcya}\]> \[${fdef}\]"``                              1
``PS2='>>> '``                                                  1
``PS2="> "``                                                    1
==============================================================  =


Radline macros
~~~~~~~~~~~~~~


============================================  ==
``bind "set completion-ignore-case on"``      18
``bind "set show-all-if-ambiguous on"``       16
``bind '"\e[A": history-search-backward'``    13
``bind '"\e[B": history-search-forward'``     13
``bind 'set show-all-if-ambiguous on'``        7
``bind "set completion-map-case on"``          7
``bind "set mark-symlinked-directories on"``   6
``bind 'set completion-ignore-case on'``       5
``bind '"\e[A":history-search-backward'``      4
``bind '"\e[B":history-search-forward'``       4
============================================  ==


Bspwm
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


Neovim
------


Set statements
~~~~~~~~~~~~~~


=======================  ===
``set number``           300
``set expandtab``        290
``set background=dark``  225
``set hidden``           196
``set shiftwidth=4``     191
``set ignorecase``       182
``set tabstop=4``        179
``set autoindent``       174
``set smartcase``        163
``set incsearch``        162
=======================  ===


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ==
``Plugin 'scrooloose/nerdtree'``             17
``Plugin 'VundleVim/Vundle.vim'``            16
``Plugin 'vim-airline/vim-airline'``         11
``Plugin 'vim-airline/vim-airline-themes'``  10
``Plugin 'tpope/vim-fugitive'``              10
``Plugin 'scrooloose/nerdcommenter'``         7
``Plugin 'fatih/vim-go'``                     7
``Plugin 'majutsushi/tagbar'``                7
``Plugin 'tpope/vim-surround'``               6
``Plugin 'airblade/vim-gitgutter'``           6
===========================================  ==


Vim-plug plugins
~~~~~~~~~~~~~~~~


=====================================================================  ===
``Plug 'tpope/vim-fugitive'``                                          182
``Plug 'vim-airline/vim-airline'``                                     156
``Plug 'tpope/vim-surround'``                                          152
``Plug 'vim-airline/vim-airline-themes'``                              140
``Plug 'junegunn/fzf.vim'``                                            140
``Plug 'scrooloose/nerdtree'``                                         135
``Plug 'airblade/vim-gitgutter'``                                      105
``Plug 'tpope/vim-commentary'``                                         94
``Plug 'jiangmiao/auto-pairs'``                                         83
``Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }``   82
=====================================================================  ===


Custom functions per vimrc
~~~~~~~~~~~~~~~~~~~~~~~~~~


======  ===
``0``   576
``1``   129
``2``    74
``4``    60
``3``    55
``5``    17
``12``   13
``13``   11
``7``    11
``6``     8
======  ===


Sxhkd
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


Termite
-------


Font
~~~~


=============================  ==
``font = monospace 9``         55
``font = monospace 12``        53
``font = monospace 11``        36
``font = monospace 10``        22
``font = hack 10``             18
``font = hack 11``             16
``font = source code pro 10``  16
``font = source code pro 11``  13
``font = hack 12``             12
``font = hack 9``              11
=============================  ==


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

