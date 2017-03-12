#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    sock.bind(server_address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print('got a connection from {0}'.format(addr))
        msg = 'Thank you for connecting' + '\r\n'
        client.send(msg.encode('ascii'))
        client.close()
