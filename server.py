#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple 
"""

import socketserver
import sys 
import os


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
	
	elif METHOD == 'ACK'
		aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + audio)
		print("Executing...", aEjecutar)
		print()
		os.system(aEjecutar)

	elif METHOD == 'BYE':
		self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

	
if __name__=="main__":
	
	try:
		IP_s = sys.argv[1]
		PORT_s = int(sys.argv[2])
		audio = sus.argv[3]

	try:
		serv.serve_forever()
	except KeyboardInterrupt:
		print()
		print("Finalizado Servidor")
		



