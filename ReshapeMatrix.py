#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReshapeMatrix.py
# @Time    : 2017-08-21 14:56
# @Author  : zhang bo
# @Note    : 
"""


def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    tmp = [n for num in nums for n in num]
    if r*c > len(tmp) or r*c < len(tmp):
        return nums
    res = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(tmp[0])
            tmp.remove(tmp[0])
        res.append(row)
    return res

nums = [[1, 2], [3, 4], [5, 6]]
r = 2
c = 2
print(matrixReshape(nums, r, c))