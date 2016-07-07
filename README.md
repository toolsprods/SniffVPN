![Version](https://img.shields.io/badge/SniffVPN-0.2%20--%20Alfa%20Version-red.svg?style=flat-square)
![License](https://img.shields.io/badge/license-GNU-green.svg?style=flat-square)
![Supported Python versions](https://img.shields.io/badge/python-2.7-blue.svg?style=flat-square)
![Supported OS](https://img.shields.io/badge/Supported%20OS-Linux-yellow.svg?style=flat-square)

# SniffVPN

SniffVPN is a tool for Linux written in Python that logs all HTTP requests that are made through our VPN connection.

This allows collection of information about URLs that pass through the VPN in order to analyze them for possible malware.

Prerequisities
==============

You need to have configured a VPN with OpenVPN and installed Scapy and tcpdump for the SniffVPN works:

```
sudo apt-get install python-scapy tcpdump
```

Installing
==========

To start SniffVPN simply run:

```
python SniffVPN.py
```

You can run the program without saving the logs by running:

```
python SniffVPN.py --nologs
```

Authors
=======

**Álvaro Núñez** - <toolsprods@gmail.com>

**Original idea: Chema Alonso** - elladodelmal.com

License
=======

This project is licensed under the GNU General Public License - see the LICENSE file for details
