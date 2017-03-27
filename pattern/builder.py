# -*- coding:utf-8 -*- 
# 2017/3/27


class Distribute(object):
    def __init__(self):
        self.builder = None

    def build_process(self):
        self.builder.init_building()
        self.builder.build_kinds()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


class Building(object):
    def __init__(self):
        self.size = ""
        self.kinds = ""

    def __repr__(self):
        return 'building type:{0}, building size:{1}'.format(self.kinds, self.size)


class Builder(object):
    def __init__(self):
        self.building = None

    def init_building(self):
        self.building = Building()

    def build_size(self):
        raise NotImplementedError

    def build_kinds(self):
        raise NotImplementedError


class HouseBuilder(Builder):
    def build_kinds(self):
        self.building.kinds = 'house'

    def build_size(self):
        self.building.size = '500*600M'


class BuildingBuilder(Builder):
    def build_size(self):
        self.building.kinds = 'building'

    def build_kinds(self):
        self.building.size = '10*10M'

if __name__ == '__main__':
    distribute = Distribute()
    distribute.builder = HouseBuilder()
    distribute.build_process()
    print distribute.get_building()
    distribute = Distribute()
    distribute.builder = BuildingBuilder()
    distribute.build_process()
    print distribute.get_building()