#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : TwoSum.py
# @Time    : 2017-09-15 22:11
# @Author  : zhang bo
# @Note    : 从一个已经排好序的列表numbers中找到两个数，使得他们的和等于target。
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
                return i + 1, j + 1

# 时间复杂度还是太高
def twoSum2(numbers, target):
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in numbers[i+1:]:
            return i + 1, numbers[i+1:].index(diff) +i + 2

# 设置首尾两个指针，向中间移动
def twoSum3(numbers, target):
    i = 0
    j = len(numbers)-1
    while i < j:
        temp = numbers[i] + numbers[j]
        if temp > target:
            j -= 1
        elif temp < target:
            i += 1
        else:
            return i+1, j+1
    return None  # 没有找到

print(twoSum3([1, 1, 3, 4], 7))
