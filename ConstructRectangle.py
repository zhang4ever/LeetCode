#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ConstructRectangle.py
# @Time    : 2017-09-12 14:16
# @Author  : zhang bo
# @Note    : 
"""

def constructRectangle(area):
    """
    :type area: int
    :rtype: List[int]
    """
    tmp = [[i, int(area / i)] for i in range(1, area + 1) if (area % i == 0) and (i >= int(area / i))]
    diffs = [(index[0] - index[1]) for index in tmp]
    min_index = diffs.index(min(diffs))
    min_index
    return tmp[min_index]


def constructRectangle2(area):
    min = area
    res = [0, 0]
    for i in range(1, area + 1):
        if area % i == 0:
            w = int(area / i)
            if i >= w:
                diff = i - w
                if min > diff:
                    min = diff
                    res = [i, w]
    return res


def constructRectangle3(area):
    import numpy as np
    w = int(np.sqrt(area))
    l = w
    while w > 0:
        if area % w == 0:
            l = int(area / w)
            break
        w -= 1
    return [l, w]

print(constructRectangle3(1))
