#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SearchInsertPosition.py
# @Time    : 2017-08-16 19:52
# @Author  : zhang bo
# @Note    : Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        if target > max(nums):
            return len(nums)
        for i in range(len(nums)):
            if nums[i] > target:
                return i


sol = Solution()
nums = [0, 1, 5, 6]
target = [5, 2, 7, -1]
for t in target:
    print(t, sol.searchInsert(nums, t))