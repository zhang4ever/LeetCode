#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RoundPrint.py
# @Time    : 2018-03-14 21:24
# @Author  : zhang bo
# @Note    : 题目要求：将一个圆形划分为N个扇形，现有M中不同的颜色， 要求这N块相邻的区域不同色，
            问共有多少种不同的涂色方案（N>=1,M>=3）

"""

def round_print(m, n):
    if m < 3 or n < 1:
        return -1

    if n < 3:
        return combination(m, 2)

    # res = (m-1)**n + (-1)**n * (m-1)
    res = m*(m-1)**(n-1) - round_print(m, n-1)
    return res


# 计算n的阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


# 计算排列组合
def combination(n, m):
    return factorial(n) / factorial(n-m)

if __name__ == '__main__':
    M = 5
    N = 5
    print(round_print(M, N))
