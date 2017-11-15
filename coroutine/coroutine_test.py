#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/2
import socket
import selectors34

selector = selectors34.DefaultSelector()


class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)


class Task(object):
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            print "task resume coroutine"
            next_future = self.coro.send(future.result)
            print " coroutine  stop wait for event to resume"
        except StopIteration:
            print "task return"
            return
        next_future.add_done_callback(self.step)


class Fetcher(object):
    def __init__(self, url, name='1'):
        self.response = b''
        self.url = url
        self.sock = None
        self.name = name

    def fetch(self):
        print("start Fetcher {0}".format(self.name))
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('xkcd.com', 80))
        except Exception:
            print "socket exception"
            pass
        f = Future()

        def on_connected():
            print "write able callback"
            f.set_result(None)

        print "register"
        selector.register(self.sock.fileno(), selectors34.EVENT_WRITE, on_connected)
        print "yield"
        yield f
        print('connected')
        print('start send request')
        selector.unregister(self.sock.fileno())
        request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
        self.sock.send(request.encode('ascii'))
        while True:
            f = Future()
            _sock = self.sock

            def on_readable():
                f.set_result(_sock.recv(4096))

            selector.register(self.sock.fileno(), selectors34.EVENT_READ, on_readable)
            chunk = yield f
            selector.unregister(self.sock.fileno())
            if chunk:
                self.response += chunk
            else:
                break
        print(self.response)


stopped = False


def loop():
    while not stopped:
        events = selector.select()
        print events
        for event_key, event_mask in events:
            callback = event_key.data
            print "loop callback"
            callback()


fetcher = Fetcher('/353/', name='Fist One')
Task(fetcher.fetch())
fetcher = Fetcher('/353/', name='Fist Tow')
Task(fetcher.fetch())
loop()
