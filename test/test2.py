# -*- coding:utf-8 -*- 
# 2017/3/30


def ins_sort_rec(seq, i):
    if i == 0:
        return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1


a = [1, 4, 3, 2, 5, 7, 8, 6, 0, 8]

ins_sort_rec(a, len(a))
print a
