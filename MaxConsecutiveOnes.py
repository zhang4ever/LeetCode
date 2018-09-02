#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""d
# @File    : MaxConsecutiveOnes.py
# @Time    : 2017-09-11 10:15
# @Author  : zhang bo
# @Note    : 找出连续1的最大长度

"""

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    len = 0
    max = 0
    for i in nums:
        if i == 1:
            len += 1
            if len > max:
                max = len
        else:
            len = 0
    return max

nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print(findMaxConsecutiveOnes(nums))
