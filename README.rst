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
``bspc rule -a Screenkey manage=off``                        260
``bspc rule -a Kupfer.py focus=on``                          209
``bspc rule -a mplayer2 state=floating``                     195
``bspc rule -a Gimp desktop='^8' state=floating follow=on``  182
``bspc rule -a Chromium desktop='^2'``                       162
``bspc rule -a Zathura state=tiled``                         140
``bspc rule -r "*"``                                         126
``bspc rule -a Emacs state=tiled``                            75
``bspc rule -a feh state=floating``                           59
``bspc rule -a Galculator state=floating``                    40
===========================================================  ===


Window gap/border width
~~~~~~~~~~~~~~~~~~~~~~~


===============  ===
``12/2``         151
``unset/unset``   76
``10/2``          66
``15/3``          35
``0/1``           27
``0/2``           26
``8/2``           26
``0/0``           18
``5/2``           18
``10/1``          18
===============  ===


Neovim
------


Set statements
~~~~~~~~~~~~~~


=======================  ===
``set expandtab``        391
``set number``           378
``set hidden``           320
``set ignorecase``       284
``set background=dark``  270
``set shiftwidth=4``     270
``set smartcase``        258
``set mouse=a``          255
``set nobackup``         250
``set tabstop=4``        247
=======================  ===


Colorschemes
~~~~~~~~~~~~


============================  ==
``colorscheme gruvbox``       97
``colorscheme dracula``       35
``colorscheme onedark``       32
``colorscheme nord``          22
``colorscheme molokai``       21
``colorscheme PaperColor``    17
``colorscheme one``           17
``colorscheme solarized``     16
``colorscheme OceanicNext``   15
``colorscheme NeoSolarized``  14
============================  ==


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ==
``Plugin 'VundleVim/Vundle.vim'``            10
``Plugin 'scrooloose/nerdtree'``             10
``Plugin 'tpope/vim-fugitive'``               8
``Plugin 'vim-airline/vim-airline-themes'``   8
``Plugin 'airblade/vim-gitgutter'``           7
``Plugin 'vim-airline/vim-airline'``          7
``Plugin 'ryanoasis/vim-devicons'``           5
``Plugin 'tpope/vim-surround'``               5
``Plugin 'Yggdroot/indentLine'``              4
``Plugin 'godlygeek/tabular'``                4
===========================================  ==


Vim-plug plugins
~~~~~~~~~~~~~~~~


===================================================  ===
``Plug 'tpope/vim-fugitive'``                        288
``Plug 'tpope/vim-surround'``                        260
``Plug 'junegunn/fzf.vim'``                          242
``Plug 'vim-airline/vim-airline'``                   231
``Plug 'neoclide/coc.nvim', {'branch': 'release'}``  202
``Plug 'scrooloose/nerdtree'``                       193
``Plug 'tpope/vim-commentary'``                      188
``Plug 'airblade/vim-gitgutter'``                    185
``Plug 'vim-airline/vim-airline-themes'``            177
``Plug 'jiangmiao/auto-pairs'``                      135
===================================================  ===


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


======================  ===
``set expandtab``       434
``set number``          415
``set laststatus=2``    339
``set hlsearch``        339
``set shiftwidth=4``    323
``set nocompatible``    312
``set incsearch``       307
``set tabstop=4``       300
``set encoding=utf-8``  291
``set ignorecase``      290
======================  ===


Colorschemes
~~~~~~~~~~~~


==========================  ==
``colorscheme gruvbox``     65
``colorscheme solarized``   41
``colorscheme desert``      26
``colorscheme molokai``     21
``colorscheme onedark``     18
``colorscheme jellybeans``  17
``colorscheme dracula``     16
``colorscheme PaperColor``  13
``colorscheme nord``        10
``colorscheme elflord``      9
==========================  ==


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ===
``Plugin 'VundleVim/Vundle.vim'``            117
``Plugin 'tpope/vim-fugitive'``               70
``Plugin 'scrooloose/nerdtree'``              69
``Plugin 'tpope/vim-surround'``               49
``Plugin 'vim-airline/vim-airline'``          46
``Plugin 'vim-airline/vim-airline-themes'``   35
``Plugin 'kien/ctrlp.vim'``                   33
``Plugin 'pangloss/vim-javascript'``          28
``Plugin 'gmarik/Vundle.vim'``                27
``Plugin 'scrooloose/nerdcommenter'``         25
===========================================  ===


Vim-plug plugins
~~~~~~~~~~~~~~~~


=========================================  ===
``Plug 'tpope/vim-fugitive'``              149
``Plug 'tpope/vim-surround'``              142
``Plug 'junegunn/fzf.vim'``                127
``Plug 'vim-airline/vim-airline'``         124
``Plug 'scrooloose/nerdtree'``             110
``Plug 'airblade/vim-gitgutter'``          107
``Plug 'vim-airline/vim-airline-themes'``   87
``Plug 'tpope/vim-commentary'``             87
``Plug 'itchyny/lightline.vim'``            79
``Plug 'tpope/vim-repeat'``                 67
=========================================  ===


Xorg
----


Window managers
~~~~~~~~~~~~~~~


========================  ===
``exec i3``               223
``exec bspwm``            129
``exec dwm``               94
``exec awesome``           28
``exec xmonad``            23
``exec $(get_session)``    20
``exec openbox-session``   15
``exec emacs``              8
``exec startplasma-x11``    7
``exec sowm``               6
========================  ===

