#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
 
if len(sys.argv)!=3:
	sys.exit('USage: Python client.py method recieevr@IP:SIPport')
# Cliente UDP simple.

try:
	METHOD = str(sys.argv[1])
	RECEPTOR = str(sys.argv[2])
except:
	sys.exit("Usage: python3 client.py method reciver@IP:SIPport")
	
SERVER = 'localhost'
plin = RECEPTOR.split('@')
LOGIN = plin[0]
IP = plin[1][:-5]
PORT = int(plin[1][:-4])

# Contenido que vamos a enviar

LINE = str(METHOD + 'sip': + RECEPTOR + '@' + IP + 'SIP/2.0\r\n\r\n')

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect(SERVER, PORT))
 
print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recivido  ', data.decode('utf-8'))

#if recv_invite == ['SIP/2.0 100 Trying', 'SIP/2.0 180 Ring', 'SIP/2.0 200 OK']:
#	LINE_ACK = 'ACK sip:' + LOGIN + '@' + IP + 'SIP\r\n\r\n'
#	print("Enviando: " + LINE_ACK)
#	my_socket.send(bytes(LINE_ACK, 'utf-8') + b'\r\n')
#	data = my_socket.recv(1024)
if METHOD  == 'INVITE':
	ACK_line = str('ACK' + 'sip:' + LOGIN + '@' + IP + 'SIP/2.0\r\n')
	print("enviando: " + ACK_line)
	my_socket.send(bytes(ACK_line, 'utf-8) + b'\r\n')

elif METHOD == 'BYE': 
	# Cerramos todo
	print("socket terminado")
	my_socket.close()
	print("Fin.")
