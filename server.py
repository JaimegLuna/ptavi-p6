#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple 
"""

import socketserver
import sys


class EchoHandler(socket.server.DatagramRequestHandler):
	"""
	Echo server class
	"""
def handle(self):

	"""
	Metodos
	"""
	if METHOD == 'INVITE':
		self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n")
		self.wfile.write(b"SIP/2.0 180 Ring\r\n\r\n")
		self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
	
if __name__=="main__":
