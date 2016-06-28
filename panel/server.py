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

import threading
import socket
import fcntl
import struct
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer

class myHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    self.send_response(301)
    self.send_header('Location', ('10.8.0.1:8000', '10.8.0.1:8000/panel'))
    self.end_headers()

def start_server(port):
  server = HTTPServer(('', port), SimpleHTTPRequestHandler)
  thread = threading.Thread(target = server.serve_forever)
  thread.daemon = True
  try:
    thread.start()
  except KeyboardInterrupt:
    server.shutdown()
    sys.exit(0)

def get_ip_address(ifname):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
    0x8915,  # SIOCGIFADDR
    struct.pack('256s', ifname[:15]))[20:24])
