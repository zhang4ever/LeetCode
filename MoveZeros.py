#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MoveZeros.py
# @Time    : 2017-08-16 17:27
# @Author  : zhang bo
# @Note    : 
"""

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    for x in nums:
        if x != 0:
            nums[i] = x
            i += 1
        else:
            j += 1
    for z in range(j):
        nums[i+z] = 0
    return nums


nums = [0, 1, 0, 3, 12]
print(nums)
print(moveZeroes(nums))