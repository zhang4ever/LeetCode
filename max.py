#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : max.py
# @Time    : 2017-09-10 20:01
# @Author  : zhang bo
# @Note    : 
"""
s = '((())()())'
max = 0  # 最后的最大深度
count = 0
x = 0
y = 0
for i in range(len(s)):
    if s[i] == '(':
        count += 1
        x += 1
        if count > max:
            max = count
    elif s[i] == ')':
        count = 0
        y += 1
    if y > x:
        print('error')
        break
if x == y:
    print(max)
elif x > y:
    print('error')
