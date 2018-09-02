#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : FirstBadVersion.py
# @Time    : 2017-08-17 15:53
# @Author  : zhang bo
# @Note    : 
"""

def isBadVersion(i, bad=2):
    if i == bad:
        return True


'''使用折半查找'''
def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        half = left + int((right-left) / 2)
        if not isBadVersion(half):
            right = half
        else:
            left = half + 1
    return left


n = 100
bad = 9
print('0' * (bad - 1) + '1' * (n - bad+1))
print(firstBadVersion(n))