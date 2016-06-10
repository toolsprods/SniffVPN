#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Alvaro Nunez
#
#This file is part of SniffVPN.
#
#SniffVPN is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#SniffVPN is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with SniffVPN.  If not, see <http://www.gnu.org/licenses/>.

import random

# Banner 1
banner1 = """
    _________      .__  _____  _________   _____________________
   /   _____/ ____ |__|/ ____\/ ____\   \ /   /\______   \      \ 
   \_____  \ /    \|  \   __\\\   __\ \   Y   /  |     ___/   |   \ 
   /        \   |  \  ||  |   |  |    \     /   |    |  /    |    \ 
  /_______  /___|  /__||__|   |__|     \___/    |____|  \____|__  /
          \/     \/                                             \/
"""
# Banner 2
banner2 = """
                          .-.    .-.
                     .-. /    \ /    \ 
      .--.  ___ .-. ( __)| .`. ;| .`. ; ___  ___ .-.. ___ .-.
    /  _  \(   )   \(''")| |(___| |(___(   )(   /    (   )   \ 
   . .' `. ;|  .-. . | | | |_   | |_    | |  | ' .-,  |  .-. .
   | '   | || |  | | | |(   __)(   __)  | |  | | |  . | |  | |
   _\_`.(___| |  | | | | | |    | |     | |  | | |  | | |  | |
  (   ). '. | |  | | | | | |    | |     | |  | | |  | | |  | |
   | |  `\ || |  | | | | | |    | |     ' '  ; | |  ' | |  | |
   ; '._,' '| |  | | | | | |    | |      \ `' /| `-'  | |  | |
    '.___.'(___)(___(___(___)  (___)      '_.' | \__.(___)(___)
                                               | |
                                              (___)
"""
# Banner 3
banner3 = """
   _____     _ ___ ___ _____ _____ _____
  |   __|___|_|  _|  _|  |  |  _  |   | |
  |__   |   | |  _|  _|  |  |   __| | | |
  |_____|_|_|_|_| |_|  \___/|__|  |_|___|
"""
# Banner 4
banner4 = """
    ______           _    ___   ___ ____   ____ _______ ____  _____
  .' ____ \         (_) .' ..].' ..|_  _| |_  _|_   __ |_   \|_   _|
  | (___ \_|_ .--.  __ _| |_ _| |_   \ \   / /   | |__) ||   \ | |
   _.____`.[ `.-. |[  '-| |-'-| |-'   \ \ / /    |  ___/ | |\ \| |
  | \____) || | | | | | | |   | |      \ ' /    _| |_   _| |_\   |_
   \______.[___||__[___[___] [___]      \_/    |_____| |_____|\____|
"""
# Banner 5
banner5 = """
     .---..-. .-,-,---,---.-.   .-,---. .-. .-.
    ( .-._|  \| |(| .-| .-'\ \ / /| .-.\|  \| |
   (_) \  |   | (_| `-| `-. \ V / | |-' |   | |
   _  \ \ | |\  | | .-| .-'  ) /  | |--'| |\  |
  ( `-'  )| | |)| | | | |   (_)   | |   | | |)|
   `----' /(  (_`-)\| )\|         /(    /(  (_)
         (__)    (__)(__)        (__)  (__)
"""
# Banner 6
banner6 = chr(27)+"[0;36m"+"""
   _____     _ ___ ___ _____ _____ _____
  |   __|___|_|  _|  _|  |  |  _  |   | |
  |__   |   | |  _|  _|  |  |   __| | | |
  |_____|_|_|_|_| |_|  \___/|__|  |_|___|
"""+chr(27)+"[0m"

def get_banner():
    banners = [banner1, banner2, banner3, banner4, banner5, banner6]
    return random.choice(banners)
