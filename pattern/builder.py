# -*- coding:utf-8 -*- 
# 2017/3/27


class Distribute(object):
    def __init__(self):
        pass

    def build_process(self):
        pass


class Building(object):
    def __init__(self):
        self.size = ""
        self.kinds = ""


class Builder(object):
    def __init__(self):
        self.building = None

    @staticmethod
    def build_size():
        raise NotImplementedError

    @staticmethod
    def build_kinds():
        raise NotImplementedError

