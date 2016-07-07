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

#Information
info ="""
[---]         SniffVPN - Traffic monitor for your VPN          [---]
[---]          Created by: Alvaro Nunez (toolsprods)           [---]
[---]                     Version: 0.2                         [---]
[---]                Codename: 'Alfa Version'                  [---]
[---]        Follow me on GitHub: github.com/toolsprods/       [---]
"""

#InfoColors
infocol = "\n"
infocol += chr(27) + "[0;94m" + "[---]         SniffVPN - Traffic monitor for your VPN          [---]\n"
infocol += "[---]          Created by: " + chr(27) + "[0;91m" + "Alvaro Nunez " + chr(27)+"[0;94m" + "(" + chr(27)+"[0;92m" + "toolsprods" + chr(27)+"[0;94m" + ")           [---]\n"
infocol += "[---]                     Version: " + chr(27) + "[0;91m" + "0.2                         " + chr(27) + "[0;94m" + "[---]\n"
infocol += "[---]                Codename: '" + chr(27) + "[0;93m" + "Alfa Version" + chr(27) + "[0;94m" + "'                  [---]\n"
infocol += "[---]        Follow me on GitHub: " + chr(27) + "[0;95m" + "github.com/toolsprods/       " + chr(27) + "[0;94m" + "[---]\n"+ chr(27)+"[0m"

# Banner 1
banner1 = chr(27) + "[0;32m" + """
    _________      .__  _____  _________   _____________________
   /   _____/ ____ |__|/ ____\/ ____\   \ /   /\______   \      \ 
   \_____  \ /    \|  \   __\\\   __\ \   Y   /  |     ___/   |   \ 
   /        \   |  \  ||  |   |  |    \     /   |    |  /    |    \ 
  /_______  /___|  /__||__|   |__|     \___/    |____|  \____|__  /
          \/     \/                                             \/
""" + chr(27) + "[0m"

# Banner 2
banner2 = chr(27) + "[0;97m" + """
                            .-.           
                       .-. /    \         ___  ___
        .--.  ___ .-. ( __)| .`. ; .-.   (   )(   ).-.. ___ .-.
      /  _  \(   )   \(''")| |(___/    \  | |  |  /    (   )   \ 
     . .' `. ;|  .-. . | | | |_   | .`. ; | |  | ' .-,  |  .-. .
     | '   | || |  | | | |(   __) | |(___)| |  | | |  . | |  | |
     _\_`.(___| |  | | | | | |    | |_    | |  | | |  | | |  | |
    (   ). '. | |  | | | | | |   (   __)  ' '  ; | |  | | |  | |
     | |  `\ || |  | | | | | |    | |      \ `' /| |  ' | |  | |
     ; '._,' '| |  | | | | | |    | |       '_.' | `-'  | |  | |
      '.___.'(___)(___(___(___)   | |            | \__.(___)(___)
                                  | |            | |
                                 (___)          (___)
""" + chr(27) + "[0m"

# Banner 3
banner3 = chr(27) + "[0;93m" + """
               _____     _ ___ ___ _____ _____ _____
              |   __|___|_|  _|  _|  |  |  _  |   | |
              |__   |   | |  _|  _|  |  |   __| | | |
              |_____|_|_|_|_| |_|  \___/|__|  |_|___|
""" + chr(27) + "[0;36m"

# Banner 4
banner4 = chr(27) + "[0;31m" + """
   ______           _    ___   ___ ____   ____ _______ ____  _____
 .' ____ \         (_) .' ..].' ..|_  _| |_  _|_   __ |_   \|_   _|
 | (___ \_|_ .--.  __ _| |_ _| |_   \ \   / /   | |__) ||   \ | |
  _.____`.[ `.-. |[  '-| |-'-| |-'   \ \ / /    |  ___/ | |\ \| |
 | \____) || | | | | | | |   | |      \ ' /    _| |_   _| |_\   |_
  \______.[___||__[___[___] [___]      \_/    |_____| |_____|\____|
""" + chr(27) + "[0m"

# Banner 5
banner5 = chr(27)+"[0;31m" + """
              .---..-. .-,-,---,---.-.   .-,---. .-. .-.
             ( .-._|  \| |(| .-| .-'\ \ / /| .-.\|  \| |
            (_) \  |   | (_| `-| `-. \ V / | |-' |   | |
            _  \ \ | |\  | | .-| .-'  ) /  | |--'| |\  |
           ( `-'  )| | |)| | | | |   (_)   | |   | | |)|
            `----' /(  (_`-)\| )\|         /(    /(  (_)
                  (__)    (__)(__)        (__)  (__)
""" + chr(27) + "[0m"

# Banner 6
banner6 = chr(27)+"[0;36m"+"""
               _____     _ ___ ___ _____ _____ _____
              |   __|___|_|  _|  _|  |  |  _  |   | |
              |__   |   | |  _|  _|  |  |   __| | | |
              |_____|_|_|_|_| |_|  \___/|__|  |_|___|
""" + chr(27) + "[0m"

def get_banner():
    banners = [banner1, banner2, banner3, banner4, banner5, banner6]
    return random.choice(banners) + infocol
