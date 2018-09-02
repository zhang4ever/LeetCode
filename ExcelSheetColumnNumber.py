#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ExcelSheetColumnNumber.py
# @Time    : 2017-09-13 20:44
# @Author  : zhang bo
# @Note    : Given a column title as appear in an Excel sheet, return its corresponding column number.

"""

def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {}
    res = 0
    # 建立一个字母表
    for i in range(1, 27):
        dic[chr(64 + i)] = i
    l = len(s)
    # 设置两个指针
    i = l-1
    t = 0
    while i >= 0:  # 从右往左遍历
        res += 26**t * dic[s[i]]
        t += 1
        i -= 1
    return res

s = 'BBA'
print('%s --> %s' % (s, titleToNumber(s)))
