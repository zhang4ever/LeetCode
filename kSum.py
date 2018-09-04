#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : kSum.py
# @Time    : 2018-09-04 16:19
# @Author  : zhang bo
# @Note    : kSum
"""
"""
题目描述：Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that 
    a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
示例：Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
    A solution set is:[[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
拓展到kSum
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        k = 4
        res = []
        nums.sort()
        self.kSum(nums, target, k, [], res)
        return res

    def kSum(self, nums, target, k, ans, res):
        if len(nums) < k or k < 2:
            return
        if k == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    res.append(ans + [nums[left], nums[right]])
                    # left += 1
                    # while left < right and nums[left] == nums[left - 1]:
                    #     left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        else:  # k>2
            for i in range(len(nums) - k + 1):  # 遍历
                if i > 0 and nums[i] == nums[i-1]:  # i去重
                    continue
                self.kSum(nums[i+1:], target-nums[i], k-1, ans+[nums[i]], res)  # 递归


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(solution.fourSum(nums, target))
