#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : JumpGameII.py
# @Time    : 2018-09-14 14:48
# @Author  : zhang bo
# @Note    : 45. Jump Game II
"""
"""
题目描述：Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position. 
    Your goal is to reach the last index in the minimum number of jumps.
示例：Input: [2,3,1,1,4]；Output: 2
"""
class Solution:
    # O(n)时间, 贪心算法
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int, 到达last index需要的最少的jump数。
        """
        steps = 0
        curFurthest = 0  # 当前位置可能到达的最远范围
        lastFurthest = 0  # 上一次jump可能到达的最远距离
        for i in range(len(nums)):
            curFurthest = max(curFurthest, i+nums[i])
            if i == lastFurthest:  # 如果到达上次的最远距离，再跳一次
                steps += 1
                lastFurthest = curFurthest
                if curFurthest >= len(nums) - 1:
                    break
        return steps


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    print(solution.jump(nums))