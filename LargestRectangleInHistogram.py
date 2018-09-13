#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : LargestRectangleInHistogram.py
# @Time    : 2018-09-12 21:14
# @Author  : zhang bo
# @Note    : Largest Rectangle in Histogram
"""
"""
题目描述：Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
    find the area of largest rectangle in the histogram.
示例：Input: [2,1,5,6,2,3]
    Output: 10
"""

class Solution(object):
    # 解法1：O(n^2)的解法
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        for i in range(len(heights)):
            if i < len(heights) - 1 and heights[i] <= heights[i + 1]:  # 如果bar的高度递增，则继续
                continue
            curH = heights[i]  # 正向遍历到的当前bar
            for j in range(i, -1, -1):  # 逆向遍历到i以前的bar
                curH = min(curH, heights[j])  # 找到最矮的
                maxArea = max((i - j + 1) * curH, maxArea)  # 计算公共矩形的面积
        return maxArea

    # 解法2：O(n)的解法，使用一个递增栈，存放递增的bar的坐标
    def largestRectangleArea2(self, heights):
        maxArea = 0
        stack = []
        for i, x in enumerate(heights):
            cur = i
            while stack and x <= stack[-1][1]:  # 遇到递减的，开始处理
                cur, y = stack.pop()
                maxArea = max(maxArea, (i - cur) * y)  # 找到“上坡”阶段可能出现的最大面积
            stack.append((cur, x))
        print(stack)
        while stack:  # 在剩下的“上坡”阶段继续寻找可能的最大面积
            cur, y = stack.pop()
            maxArea = max(maxArea, (len(heights)-cur)*y)
        return maxArea

    # 解法3：O(n), one pass
    def largestRectangleArea3(self, heights):
        maxArea = 0
        stack = []
        for i in range(len(heights)+1):
            tmp = -1 if i == len(heights) else heights[i]  # 为了解决最后一个元素的问题
            while stack and tmp <= heights[stack[-1]]:  # 遇到递减的，开始处理
                cur = stack.pop()
                # 找到“上坡”阶段可能出现的最大面积，因为上一步已经pop了，所以宽度要-1
                maxArea = max(maxArea, heights[cur]*(i if not stack else (i - stack[-1] - 1)))
            stack.append(i)
        return maxArea

if __name__ == '__main__':
    solution = Solution()
    heights = [1]
    print(solution.largestRectangleArea2(heights))
    print(solution.largestRectangleArea3(heights))