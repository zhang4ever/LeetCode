#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReverseBits.py
# @Time    : 2017-08-16 20:36
# @Author  : zhang bo
# @Note    : 将32位的无符号整数转化成32位二进制然后反转
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits1(self, n):
        bit = bin(n).replace('0b', '')
        bit = '0'*(32-len(bit)) + bit
        return int(bit[::-1], 2)



sol = Solution()
n = 1
print(sol.reverseBits1(n))