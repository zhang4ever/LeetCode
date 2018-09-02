#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : UglyNumber.py
# @Time    : 2017-08-17 22:09
# @Author  : zhang bo
# @Note    : 
"""


def isUgly(num):
    if num == 1:
        return True
    chushu = num
    re = []
    label = [2, 3, 5]
    i = 2
    while i <= num:
        shang = chushu / i
        chushu = shang
        if shang % i == 0:
            re.append(i)
            if shang ==1:
                break
            continue
        else:
            i += 1
    print(re)
    for x in re:
        if x in label:
            return True
        else:
            return False

print(isUgly(14))