# -*- coding:utf-8 -*- 
# 2017/3/27
import copy

if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1,]
    a.append(b)
    print "init the value a"
    print 'a:', a
    c = copy.copy(a)
    print 'c:', c
    d = copy.deepcopy(a)
    print 'd:', d
    b.append(2)
    print 'after append value to b'
    print 'a(after append):', a
    print 'b(after append):', b
    print 'c(copy after append value to b):', c
    print 'd(deepcopy after append value to b):', d
