# -*- coding:utf-8 -*- 
# 2017/5/23
import sys
import logging
import cgitb
import traceback


logger = logging.Logger('test', logging.DEBUG)
handle = logging.StreamHandler(sys.stdout)
logger.addHandler(handle)


def f():
    1/0

if __name__ == '__main__':
    cgitb.enable(format='text')
    try:
        f()
    except Exception, e:
        a, b, c = sys.exc_info()
        traceback.print_exception(a, b, c)
        print '----' * 10
        for filename, linenum, funcname, source in traceback.extract_tb(c):
            print "%-23s:%s '%s' in %s()" % (filename, linenum, source, funcname)