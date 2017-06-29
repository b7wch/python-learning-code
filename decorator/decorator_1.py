# -*- coding:utf-8 -*- 
# 2017/3/29


class lazy_property(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return instance
        value = self.func(instance)
        setattr(instance, self.func.__name__, value)
        return value


class Cycle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @lazy_property
    def area(self):
        print "compute stage "
        return self.x * self.y


if __name__ == '__main__':
    c = Cycle(1, 2)
    s = c.area
    print s
    ss = c.area
    print ss
    c.area = '3'
    print c.area
