# -*- coding:utf-8 -*- 
# 2017/3/29


def lazy_decorator(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


class Circle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @lazy_decorator
    def area(self):
        print "compute"
        return self.x * self.y


if __name__ == '__main__':
    c = Circle(1, 2)
    print c.area
    print type(c.area)
    print c.area
