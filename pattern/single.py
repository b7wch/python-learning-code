# -*- coding:utf-8 -*- 
# 2017/3/23
# mail:yangnianqiu@gmail.com


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        super(Singleton, cls).__init__(*args, **kwargs)
        cls._single_instance = None

    def __call__(cls, *args, **kwargs):
        print "metaclass been invoked"
        if cls._single_instance:
            return cls._single_instance
        else:
            print 'before invoke super call'
            cls._single_instance = super(Singleton, cls).__call__(*args, **kwargs)
            print "after invoke super call"
        return cls._single_instance


class SingleImpl(object):
    __metaclass__ = Singleton

    def __init__(self):
        print "create a SingleImpl instance, and you know SingleImpl is the instance of Singleton"

if __name__ == '__main__':
    a = SingleImpl.__call__()
    print '--' * 10
    b = SingleImpl()
    c = SingleImpl()
    print id(a), id(b), id(c)
    print b.__dict__
