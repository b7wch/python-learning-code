#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/12
import io
import socket

sock = socket.socket()
sock.setblocking(False)
try:
    sock.connect(('xkcd.com', 80))
except Exception:
    print('error')
    pass

request = 'GET / HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'
encoded = request.encode('ascii')
while True:
    try:
        sock.send(encoded)
        print("after sent")
        break
    except Exception:
        print('os error')
        pass
print("sent")
