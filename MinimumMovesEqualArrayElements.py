#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MinimumMovesEqualArrayElements.py
# @Time    : 2017-09-13 14:29
# @Author  : zhang bo
# @Note    : 给定一个非空的数组，找出需要多少次的操作，能使得数组中的每个元素相等，每次操作只能给n-1个元素同时+1

"""

# 此法时间复杂度较高，适合较小的数
def minMoves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num = nums[:]
    n = len(num)-1
    cont = 0
    while len(set(num)) != 1:
        num.sort()
        print(num)
        num[:n] = [num[i]+1 for i in range(n)]
        cont += 1
    print(num)
    return cont

# 原题目的等价命题就是给较小的数-1， 直到所有的数都等于较小的数
def minMoves2(nums):
    min_all = min(nums) # 最小的数
    # for i in range(len(nums)):
    #     cont += (nums[i]-min_all)
    cont = sum([(nums[i] - min_all) for i in range(len(nums))])
    return cont

def minMoves3(nums):
    return sum(nums) - min(nums)* len(nums)
nums = [3, 4, 5]
print(minMoves3(nums))