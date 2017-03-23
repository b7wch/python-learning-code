# -*- coding:utf-8 -*- 
# 2017/3/23
# mail:912493785@qq.com


class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self


if __name__ == '__main__':
    """archive binary tree"""
    b = Bunch(left=Bunch(left='a', right='b'), right=Bunch(left='c', right='d'))
    print b
