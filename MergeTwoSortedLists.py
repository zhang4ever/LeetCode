#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MergeTwoSortedLists.py
# @Time    : 2017-08-16 13:28
# @Author  : zhang bo
# @Note    : Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def mergeTwoLists(self, l1, l2):
            if l1 == None and l2 == None:
                return None
            if l1 == None:
                return l2
            if l2 == None:
                return l1
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

solution = Solution()
l1 = ListNode(1)

l2 = ListNode(2)

print('l1:', l1.val)
print('l2:', l2.val)


l = solution.mergeTwoLists(l1, l2)
print(l)


