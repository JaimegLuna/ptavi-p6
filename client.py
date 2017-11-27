#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
 
# Cliente UDP simple.

SERVER = 'localhost'
METHOD = sys.argv[1]
DIR = sys.argv[2]
LOGIN = DIR.split('@')[0]
IP = DIR.split(':')[0],split('@')[1]
PORT = int(DIR.split(':')[1])

# Contenido que vamos a enviar

LINE = METHOD + 'sip': + RECEPTOR + '@' + IP + 'SIP'/2.0\r\n\r\n' 

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))
 
print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

if recv_invite == ['SIP/2.0 100 Trying', 'SIP/2.0 180 Ring', 'SIP/2.0 200 OK']:
	LINE_ACK = 'ACK sip:' + LOGIN + '@' + IP + 'SIP\r\n\r\n'
	print("Enviando: " + LINE_ACK)
	my_socket.send(bytes(LINE_ACK, 'utf-8') + b'\r\n')
	data = my_socket.recv(1024)

recivido = data.decode('utf-8').split('\r\n\r\n')[0:-1]
 
# Cerramos todo
my_socket.close()
print("Fin.")
