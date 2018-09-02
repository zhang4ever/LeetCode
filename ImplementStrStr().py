#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ImplementStrStr().py
# @Time    : 2017-08-16 18:58
# @Author  : zhang bo
# @Note    : Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        elif needle != '' and haystack =='':
            return -1
        else:
            start = needle[0]
            for i in range(len(haystack)):
                if haystack[i] == start:
                    if needle == haystack[i: i+len(needle+'\n')]:
                        return i
            #return [i for i in range(len(haystack)) if haystack[i] == needle[0] and needle ==haystack[i: i+len(needle)]][0]
            #return -1



sol = Solution()
hay ='zhang'
nee = 'z'
print(sol.strStr(hay, nee))


