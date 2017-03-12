#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print(sys.stderr)
    print('connctiong to {0}'.format(server_address))
    sock.connect(server_address)
    msg = sock.recv(1024)
    sock.close()
    print(msg.decode('ascii'))
