# -*- coding:utf-8 -*- 
# 2017/3/28
from random import randint, randrange
from collections import defaultdict


def count_sort(t):
    result = []
    temp = defaultdict(list)
    for k in t:
        temp[k].append(k)
    for j in range(min(temp), max(temp) + 1):
        result.extend(temp[j])
    return result


a = [randint(0, 30) for i in range(30)]
print a
print count_sort(a)

