#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : KeyboardRow.py
# @Time    : 2017-08-20 16:33
# @Author  : zhang bo
# @Note    : 给定一个字符列表，返回那些可以由同一行内字母组成的字符
"""
import matplotlib.pyplot as plt

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """

    lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    res = []

    for line in lines:
        for word in words:
            num = 0
            for letter in word.lower():
                if letter not in line:
                    break
                else:
                    num += 1
                    if num == len(word):
                        res.append(word)
    return res


def findWords1(words):
    lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    res = []
    for line in lines:
        for word in words:
            if set(word.lower()).issubset(line):
                res.append(word)
    return res


def findWords2(words):
    lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    return [word for word in words for line in lines if set(word.lower()).issubset(line)]


words = ["Hello", "Alaska", "Dad", "Peace"] 0
print(findWords2(words))
