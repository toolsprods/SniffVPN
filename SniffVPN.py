#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Alvaro Nuñez
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
----------------------------------------------------------------------------
	    SniffVPN -- Analyzer malicious urls over VPN
----------------------------------------------------------------------------
The author is not responsible for any misuse of the application!
"""

## LIBRARIES ##
import os
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import argparse

from argparse import RawTextHelpFormatter
from scapy.all import *
from core.banners import get_banner
from core.logger import write_logger

## CONTEXT VARIABLES ##
version='0.1'
codename='Alpha version'
interface='tun0' #Define the interface, tun0 for VPN
count=0
logs=None

def parse_args():
  parser = argparse.ArgumentParser(description="SniffVPN v{} - '{}'".format(version,codename)+"\nA tool to sniff all HTTP traffic passing through your VPN and analyzer malicious urls",
				   version="SniffVPN v{} - '{}'".format(version, codename),
				   usage='python SniffVPN.py [options]',
				   epilog="The author is not responsible for any misuse of the application",
				   formatter_class=RawTextHelpFormatter)
  #parser.add_argument('-i', dest='interface', type=str, help="Interface to use for sniff, default tun0 for VPN")
  parser.add_argument('--nologs', action='store_false', help="Disable logs")
  return parser.parse_args()

#Function to detect if VPN is installed
def detectVPN():
  return(os.path.isdir("/etc/openvpn"))

#Function to get the urls, http only
def packet(x):
  getpacket=x.sprintf("{Raw:%Raw.load%\n}")
  if getpacket[1:4]=="GET":
    list=getpacket.split(r"\r\n")
    if len(list)>2:
      resource=list[0]
      host=list[1]
      url=host[6:]+resource[5:(len(resource)-9)]
      #IPs info for logs
      time=x.sprintf("%pkt.time%")
      ipsrc=x.sprintf("%IP.src%")
      ipdst=x.sprintf("%IP.dst%")
      portsrc=x.sprintf("%IP.sport%")
      portdst=x.sprintf("%IP.dport%")
      iporig=getOriginalIP(ipsrc)
      if logs:
        write_logger(time,iporig,ipsrc,ipdst,portsrc,portdst,url)
    return url+"\n"

#Function to get the original IP
def getOriginalIP(privip):
  file=open('/var/log/openvpn-status.log','r')
  for line in file:
    if line.find(privip)==0:
      ipOrig=line.split(',')
  file.close()
  return ipOrig[2].split(':')[0]

#Function main
def main():
  #global interface
  global logs
  args=parse_args()
  #interface=args.interface
  logs=args.nologs
  if detectVPN():
    print get_banner()
    #Start sniff, method from scapy
    sniff(iface=interface, prn=packet, count=count)
  else:
    print 'Installing OpenVPN undetected.\nPlease check OpenVPN is installed correctly'

main()
