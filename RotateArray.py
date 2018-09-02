#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RotateArray.py
# @Time    : 2017-08-16 21:22
# @Author  : zhang bo
# @Note    : For example, with n = 7 and k = 3, 
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

"""
class Solution(object):
    #
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead
        """
        if k == 0:
            return nums
        t = len(nums)-k
        for i in range(k):
            print(nums)
            tmp = nums[t+i]
            nums[t+i] = nums[i]
            nums[i] = tmp
        return nums


    '''使用下标取余遍历更新列表元素'''

    def rotate1(self, nums, k):
        old = nums[:]
        for i in range(len(nums)):
            nums[(i+k) % len(nums)] = old[i]
            print(nums)
        return nums


    '''将最后的元素一次与前面的交换'''
    def rotate2(self, nums, k):
        for i in range(k):
            needle = nums[-1]
            for j in range(len(nums)):
                tmp = needle
                needle = nums[j]
                nums[j] = tmp
        return nums


sol = Solution()
nums = [1, ]
k = 0
print(sol.rotate2(nums, k))

