# -*- coding:utf-8 -*- 
# 2017/5/20

def f():
    print "start"
    n = 0
    while n < 100:
        print 'yield ', str(n)
        yield n
        print 'after yield'
        n += 1


t = f()
# for each in range(100):
#     print 'in for loop', t.send(None)
a = t.send(None)
print a
print t.next()
import cgitb