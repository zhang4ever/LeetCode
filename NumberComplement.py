#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : NumberComplement.py
# @Time    : 2017-08-19 10:15
# @Author  : zhang bo
# @Note    : 返回num的补码的十进制值
"""


def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    bits = bin(num)
    bits = bits.replace('0b', '')
    new = ''
    for i in range(len(bits)):
        if bits[i] == '0':
            new += '1'
        else:
            new += '0'
    return int(new, 2)

print(findComplement(5))
 