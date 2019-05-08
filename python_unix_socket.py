#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import sys
import socket
import click

server_address='./uds_socket'

def client():
    try:
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(server_address)
    except socket.error, msg:
        print >>sys.stderr, msg
        sys.exit(1)

    try:
    
        # Send data
        message = 'This is the message.  It will be repeated.'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message[:16])

        amount_received = 0
        #amount_expected = len(message)
        amount_expected = 16
    
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data
    except socket.error, msg:
        print >>sys.stderr, msg
        sys.exit(1)

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()

def handle_client(clientSocket):
    
    try:
        data = clientSocket.recv(16)
        clientSocket.sendall(data)
    except socket.error, msg:
        print >>sys.stderr, msg
    finally:
        print >>sys.stderr, 'closing socket'
        clientSocket.close()

def server():
    try:
        os.unlink(server_address)
    except Exception as e:
        print 'Unlink Exception:',e
        sys.exit(2)

    try:
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.bind(server_address)
	sock.listen(1)
    except Exception as e:
        print 'Exception:',e
        sys.exit(2)

    while 1:
        connection ,cliaddress = sock.accept()
        handle_client(connection)

@click.command()
@click.option('--type', default='server')
def main(type):
    if type == 'server':
        server()
    else:
        client()    


if __name__ == '__main__':
    main()
