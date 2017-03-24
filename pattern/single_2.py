# -*- coding:utf-8 -*- 
# 2017/3/24


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        else:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance


class SingletonImpl(Singleton):
    def __init__(self):
        pass


if __name__ == '__main__':
    a = SingletonImpl()
    b = SingletonImpl()
    print id(a) == id(b)
