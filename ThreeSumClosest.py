#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ThreeSumClosest.py
# @Time    : 2018-09-04 17:23
# @Author  : zhang bo
# @Note    : 3Sum Closest
"""
"""
题目描述：Given an array nums of n integers and an integer target, find three integers in nums such that the sum is 
    closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
示例：Given array nums = [-1, 2, 1, -4], and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cur_min = nums[0] + nums[1] + nums[len(nums) - 1]  # 当前最接近target的和
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]  # 当前三个元素的和
                if abs(cur_sum - target) < abs(cur_min - target):
                    cur_min = cur_sum
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    return target
        return cur_min

if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,2]
    target = 3
    print(solution.threeSumClosest(nums, target))
