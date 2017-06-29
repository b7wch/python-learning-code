# -*- coding:utf-8 -*- 
# 2017/3/28


def naive_max_perm(M, A=None):
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A


m = [2, 2, 0, 5, 3, 5, 7, 4]
print naive_max_perm(m)
