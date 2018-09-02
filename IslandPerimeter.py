#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : IslandPerimeter.py
# @Time    : 2017-08-22 19:55
# @Author  : zhang bo
# @Note    : 求岛屿边界数
"""


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                res += 4
                if i > 0 and grid[i - 1][j]:
                    res -= 2
                if j > 0 and grid[i][j - 1]:
                    res -= 2
    return res


grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]
print(islandPerimeter(grid))
