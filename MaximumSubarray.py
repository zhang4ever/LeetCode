#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MaximumSubarray.py
# @Time    : 2017-12-20 14:09
# @Author  : zhang bo
# @Note    : 
"""
def maxSubArray(
        nums):
    """
    :type nums: List[int]
    :rtype: int
    这是一个动态规划的例子，当局部最优解不是全局最优解时，动态调整，时间复杂度O(N)
    """
    local_max = nums[0]
    global_max = nums[0]
    for i in range(len(nums)):
        if local_max < 0:  # 如果局部最优解<0, 则舍弃
            local_max = 0
        local_max = local_max + nums[i]
        global_max = max(local_max, global_max)

    return global_max


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))