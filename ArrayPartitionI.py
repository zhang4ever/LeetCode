#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ArrayPartitionI.py
# @Time    : 2017-08-18 12:37
# @Author  : zhang bo
# @Note    : Given an array of 2n integers, your task is to group these integers into n pairs 
of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i 
from 1 to n as large as possible.
"""


def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None:
        return 0
    nums.sort()
    new = []
    print(nums)
    i = 0

    while i < len(nums):
        new.append(min(nums[i], nums[i + 1]))
        i += 2
        print(new)


def arrayPairSum2(nums):
    nums.sort()
    return sum([min(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)])

    
print(arrayPairSum2([1, 4, 3, 2]))
