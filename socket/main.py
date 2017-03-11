#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock.gethostname())
