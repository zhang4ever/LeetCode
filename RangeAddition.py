#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RangeAddition.py
# @Time    : 2017-09-12 21:47
# @Author  : zhang bo
# @Note    : 
"""

def maxCount(m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    import numpy as np
    M = []
    for i in range(m):
        M.append([0] * n)
    M = np.mat(M)
    print(M)
    for op in ops:
        M[:op[0], :op[1]] += 1
    return M.max()

# 时间复杂度太高
def maxCount2(m, n, ops):
    M = []
    for i in range(m):
        M.append([0] * n)

    for op in ops:
        for i in range(op[0]):
            for j in range(op[1]):
                M[i][j] += 1
    print(M)
    mx = 0
    cont = 0
    for i in range(m):
        if mx < max(M[i]):
            mx = max(M[i])
        cont += M[i].count(mx)
    print(mx)
    return cont

def maxCount3(m, n, ops):
    '''思路就是：
    ops我的操作都是从左上角开始向下延伸的，只要找出操作的次数最多的单元的即可，也就是最小的行集合
    最小的列对应的，它的乘积就是最后的个数
    '''
    row = m
    col = n
    for op in ops:
        row = min(row, op[0])
        col = min(col, op[1])
    return row * col

print(maxCount3(40000, 40000, [[2, 2], [3, 3]]))
