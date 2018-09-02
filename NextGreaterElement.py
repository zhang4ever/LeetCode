#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : NextGreaterElement.py
# @Time    : 2017-08-26 12:16
# @Author  : zhang bo
# @Note    : 
"""


def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    
    """
    res = []
    for x in findNums:
        index = nums.index(x)
        for i in range(index, len(nums)):
            if nums[i] > x:
                res.append(nums[i])
                break
            if i == len(nums) - 1:
                res.append(-1)
    return res

findNums = [3, 2, ]
nums = [1, 3, 4, 2]
print(nextGreaterElement(findNums, nums))
