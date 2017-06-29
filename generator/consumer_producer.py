# -*- coding:utf-8 -*- 
# 2017/5/20

def consumer():
    state = True
    while True:
        n = yield state
        print "get " + str(n)
        if n == 3:
            state = False


def producer(cons):
    n = 5
    while n > 0:
        yield cons.send(n)
        n -= 1


if __name__ == '__main__':
    c = consumer()
    c.send(None)
    p = producer(c)
    for state in p:
        print state
        if not state:
            print 'only 3,4,5'
            break
    print 'finish'
