#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReverseWords.py
# @Time    : 2017-08-20 18:45
# @Author  : zhang bo
# @Note    : Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    res = []
    for each in s.split(' '):
        each = each[::-1]
        res.append(each)
        res.append(' ')
    res.pop()

    s = ''
    for i in res:
        s += i
    return s


def reverseWords1(s):
    res = [each[::-1]for each in s.split(' ')]
    return ' '.join(res)

s = "Let's take LeetCode contest"
print(reverseWords(s))