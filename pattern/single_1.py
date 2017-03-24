# -*- coding:utf-8 -*- 
# 2017/3/24
from functools import wraps


def singleton(cls):
    instance = dict()

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class Singleton(object):
    def __init__(self):
        print 'create impl'

# help(Singleton)
if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print id(a), id(b)
