#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ValidPalindrome.py
# @Time    : 2018-09-11 15:25
# @Author  : zhang bo
# @Note    : Valid Palindrome(回文)
"""

"""
题目描述：Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
示例：Input: "A man, a plan, a canal: Panama"； Output: true
    Input: "race a car"； Output: false
    
"""
class Solution(object):
    # 思路1:直接快速求解
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x for x in list(s.lower()) if x.isalnum()]
        return s == s[::-1]

    # 思路2：递归
    def isPalindrome2(self, s):
        s = [x for x in list(s.lower()) if x.isalnum()]
        def check(s, l, r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return check(s, l+1, r-1)
        return check(s, 0, len(s)-1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome2(s="A man, sa plan, a canal: Panama"))
    print(solution.isPalindrome2(s="race a car"))
    print(solution.isPalindrome2(s=""))