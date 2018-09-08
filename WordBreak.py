#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : WordBreak.py
# @Time    : 2018-09-04 22:43
# @Author  : zhang bo
# @Note    : Word Break
"""
"""
题目描述：Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s 
        can be segmented into a space-separated sequence of one or more dictionary words.
示例：Input: s = "leetcode", wordDict = ["leet", "code"]； Output: true
    Input: s = "applepenapple", wordDict = ["apple", "pen"]； Output: true
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        for w in wordDict:
            while w in s:
                s = s.replace(w, '')
        if len(s) == 0:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = "leetcodeleets"
    wordDict = ["leet", "code"]
    print(solution.wordBreak(s, wordDict))