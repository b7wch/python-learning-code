# -*- coding:utf-8 -*- 
# 2017/3/27


class Borg(object):
    __share_dict = {}

    def __init__(self):
        self.__dict__ = self.__share_dict
        self.state = 'init'

    def __repr__(self):
        return self.state


class BorgImpl(Borg):
    pass


if __name__ == '__main__':
    a = Borg()
    a.state = 'a'
    print a
    b = Borg()
    b.state = 'b'
    print a, b
    c = Borg()
    print a, b, c
    print id(a), id(b), id(c)
