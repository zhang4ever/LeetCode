#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MajorityElement.py
# @Time    : 2017-09-17 21:55
# @Author  : zhang bo
# @Note    : Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

# 逐个遍历
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    s = list(set(nums))
    for i in s:
        if nums.count(i) >= n/2:
            return i
    return None

# 排序法
def majorityElement2(nums):
    nums.sort()
    return nums[int(len(nums) / 2)]  # 如果存在，必须是n/2位置上的元素

print(majorityElement2(nums=[3, 2, 3]))
