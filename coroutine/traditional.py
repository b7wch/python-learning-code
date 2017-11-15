#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/12
import socket


def fetch():
    sock = socket.socket()
    sock.connect(('xkcd.com', 80))
    request = 'GET /353/ HTTP/1.1\r\nHost: xkcd.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    print response


fetch()
