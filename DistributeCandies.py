#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : DistributeCandies.py
# @Time    : 2017-08-21 14:36
# @Author  : zhang bo
# @Note    : 
"""


def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    kind = len(set(candies))
    num = len(candies) /2

    if kind > num:
        return num
    else:
        return kind

candies = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
print(distributeCandies(candies))


