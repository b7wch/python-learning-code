# -*- coding:utf-8 -*- 
# 2017/3/28

import sys


class Count(object):
    def __init__(self):
        print "init count"
        self.a = 0

    def up(self):
        print "+1"
        self.a += 1

    def down(self):
        print "-1"
        self.a -= 1


sys.modules[__name__] = Count()
