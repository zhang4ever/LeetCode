#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MaximalRectangle.py
# @Time    : 2018-09-12 20:46
# @Author  : zhang bo
# @Note    : Maximal Rectangle(矩阵中连续1的子矩阵最大面积)
"""
"""
题目描述：Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
示例：Input:[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 6 
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        maxArea = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for rows in matrix:
            for j in range(n):
                if rows[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))
            print(heights, maxArea)
        return maxArea

    # 计算直方图中的子矩阵的最大面积
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []
        for i in range(len(heights)+1):
            tmp = heights[i] if i != len(heights) else -1
            while stack and heights[stack[-1]] >= tmp:
                cur = stack.pop()
                maxArea = max(maxArea, heights[cur]*(i if not stack else (i-stack[-1]-1)))
            stack.append(i)
        return maxArea


if __name__ == '__main__':
    solution = Solution()
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    matrix = [['0', '1'], ['1', '0']]
    # matrix = []
    print(solution.maximalRectangle(matrix))