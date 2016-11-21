#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys



if len(sys.argv) !=4:   
    sys.exit('Usage: python server.py IP port audio_file')


IP_S = sys.argv[1]
PORT_S = int(sys.argv[2])
FILE = sys.argv[3]

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
  

    METODOS = ['INVITE', 'BYE', 'ACK']

    def handle(self):
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            method = line.decode('utf-8').split(' ')[0]
            
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

            if not method in METODOS: 
                self.wfile.write(b'SIP/2.0 405 method not allowed\r\n\r\n')
            elif method == 'INVITE':
                send = b'SIP/2.0 100 Trying\r\n\r\nSIP/2.0 100 Trying\r\n\r\n' + b'SIP/2.0 100 Trying\r\n\r\n'
                self.wfile.write(send)
            elif method == 'ACK':
                aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + FILE
                print('Vamos a ejecutar', aEjecutar)
                os.system(aEjecutar)
            elif method == 'BYE':
                self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')

            else:
                self.wfile.write(b'SIP/2.0 400 Bad request\r\n\r\n')  


if __name__ == "__main__":

    serv = socketserver.UDPServer((IP_S, PORT_S), EchoHandler)
    print('Listening...')
    serv.serve_forever()
