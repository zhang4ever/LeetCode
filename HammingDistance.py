#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : HammingDistance.py
# @Time    : 2017-08-18 11:18
# @Author  : zhang bo
# @Note    : 
"""


def hammingDistance(self, x, y):
    """
    :type nums: List[int]
    :rtype: int
    """
    if x < 0 or x >= 2 ** 31 or y < 0 or y >= 2 ** 31:
        return 0
    bx = bin(x).replace('0b', '')
    by = bin(y).replace('0b', '')
    if len(bx) >= len(by):
        by = '0' * (len(bx) - len(by)) + by
    else:
        bx = '0' * (len(by) - len(bx)) + bx
    j = 0
    for i in range(len(bx)):
        if bx[i] != by[i]:
            j += 1
    return j