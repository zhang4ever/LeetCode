#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : JumpGame.py
# @Time    : 2018-09-13 16:39
# @Author  : zhang bo
# @Note    : Jump Game(贪心)
"""

"""
题目描述：Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
示例：Input: [2,3,1,1,4], Output: true;
    Input: [3,2,1,0,4], Output: false
思路：贪心
"""
class Solution:
    # 思路1：使用贪心算法。target设置为最后一位， cur为当前的位置，如果达能亲啊位置能跳到target，即target-cur >= nums[cur],
    # 这时将target更新到cur，cur-=1, 原问题转化为跳到新的target， 依次类推。
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return True
        target = len(nums) - 1  # 最终的目标
        cur_pos = len(nums) - 2  # 当前的最保险的位置
        while cur_pos >= 0:
            if target - cur_pos <= nums[cur_pos]:  # 当前位置一定能到达，转移目标
                target = cur_pos
            cur_pos -= 1  # 当前位置后退
        if target == 0:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]
    print(solution.canJump(nums1))