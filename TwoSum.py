#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : TwoSum.py
# @Time    : 2017-09-15 22:11
# @Author  : zhang bo
# @Note    : Two Sum
"""

"""
题目描述：Given an array of integers, return indices of the two numbers such that they add up to a specific target.
示例：Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].
限制条件：You may assume that each input would have exactly one solution, and you may not use the same element twice.
思路：先对数组进行排序，然后使用首位两个指针向中间寻找。找到之后需要返回的是排序前的位置，所以还要在原始的数组中寻找这两个元素
"""

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            print(i)
            if numbers[i] + numbers[j] == target:
                return i, j

# 时间复杂度还是太高
def twoSum2(numbers, target):
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in numbers[i+1:]:
            return i + 1, numbers[i+1:].index(diff) +i + 2

# 设置首尾两个指针，向中间移动，O(nlog(n))的解法
def twoSum3(numbers, target):
    left = 0
    right = len(numbers)-1
    num = numbers[:]  # 保存原数组，后面校正时使用
    numbers.sort()
    while left < right:
        temp = numbers[left] + numbers[right]
        if temp > target:
            right -= 1
        elif temp < target:
            left += 1
        else:  # 找到，但是此时的数组已经排序，所以要在原数组中找到这两个元素的位置
            ans = [numbers[left], numbers[right]]  # 找到的两个数
            l, r = -1, -1
            for i in range(len(num)):
                if num[i] == ans[0] and l == -1:  # 找到第一个数后就找第二个数
                    l = i
                    continue
                if num[i] == ans[1] and r == -1:
                    r = i
                    continue
                if l != -1 and r != -1:  # 两个都找到了后停止遍历，没必要浪费时间
                    break
            return l, r
    return  # 没有找到


print(twoSum3([1, 1, 2], 4))
