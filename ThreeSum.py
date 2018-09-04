#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ThreeSum.py
# @Time    : 2018-09-04 15:21
# @Author  : zhang bo
# @Note    : 3Sum
"""
"""
题目描述：Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
        Find all unique triplets in the array which gives the sum of zero.
示例：Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:[[-1, 0, 1],[-1, -1, 2]]
思路：和2Sum的情况类似，可以设置两个指针left(i+1)和right，然后使用类似于2Sum的方式向中间寻找。
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return
        res = []
        nums.sort()  # 排序
        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1] and i > 1:  # i去重
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:  # 两个指针向中间找
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum > 0:
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:  # 刚好找到,但是找到了后还要继续找
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  # 去除left指向的重复元素
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  # 去除right指向的重复元素
                        right -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))
