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

import json

def write_logjson(time,iporig,ipsrc,ipdst,portsrc,portdst,url):
  data = '{"time":"'+time+'","iporig":"'+iporig+'","ipsrc":"'+ipsrc+'","ipdst":"'+ipdst+'","portsrc":"'+portsrc+'","portdst":"'+portdst+'","url":"'+url+'"},'

  filejson = open("panel/data/logs.json", "a")
  filejson.write(data)
  filejson.close()