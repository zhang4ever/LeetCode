#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SingleNumber.py
# @Time    : 2017-08-27 21:42
# @Author  : zhang bo
# @Note    : 
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    for i in nums:
        temp = nums[:]
        temp.remove(i)
        if i not in temp:
            return i

def singleNumber2(nums):
    nums.sort()
    res = 0
    i = 0
    while i < len(nums):
        if i == len(nums) -1:
            res = nums[-1]
            break
        else:
            if nums[i] != nums[i+1]:
                res = nums[i]
                break
        i += 2
    return res


nums = [1, 1, 3, 2, 2]
print(singleNumber2(nums))