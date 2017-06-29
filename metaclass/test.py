# -*- coding:utf-8 -*-
# 2017/6/29


class Meta(type):
    def __new__(mcs, *args, **kwargs):
        print "Meta new func is invoke ", args, kwargs
        return super(Meta, mcs).__new__(mcs, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print "Meta init func is invoke ", args, kwargs
        super(Meta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print "invoke Meta __call__"
        return super(Meta, cls).__call__(*args, **kwargs)


class B:
    pass


class A(dict, B):
    __metaclass__ = Meta

    def f(self):
        pass

    def __call__(self, *args, **kwargs):
        print "instance __call__ invoked"
print "instance a"
a = A()
a()
print "instance a finish"
b = A()
b()
print "instance b finish"
