#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RansomNote.py
# @Time    : 2017-09-14 10:20
# @Author  : zhang bo
# @Note    : 
"""

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    j = 0
    cont = 0
    for i in ransomNote:
        if i in magazine[j:len(magazine)]:
            j = magazine.index(i)
            j += 1
            cont += 1
    if cont == len(ransomNote):
        return True
    return False


def canConstruct2(ransomNote, magazine):
    boo = True
    magazine = [i for i in magazine]
    for i in ransomNote:
        print(i)
        if i in magazine:
            magazine.remove(i)
            print(magazine)
        else:
            boo = False
            break
    return boo

print(canConstruct2("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))