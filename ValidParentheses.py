#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ValidParentheses.py
# @Time    : 2017-08-16 11:05
# @Author  : zhang bo
# @Note    : Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []
        for each in s:
            if each in left:
                stack.append(each)
            elif each in right:
                if not stack or (not 1 <= (ord(each) - ord(stack[-1])) <= 2):
                    return False
                else:  # 匹配
                    stack.pop()
            else:
                return False  # 欧赫然
        print(stack)
        if len(stack) == 0:
            return True
        else:
            return False

solution = Solution()
print(solution.isValid('{[)}'))
