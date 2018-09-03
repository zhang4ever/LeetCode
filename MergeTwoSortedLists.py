#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MergeTwoSortedLists.py
# @Time    : 2017-08-16 13:28
# @Author  : zhang bo
# @Note    : Merge two sorted linked lists
"""

"""
题目描述：Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
示例：Input: 1->2->4, 1->3->4；
    Output: 1->1->2->3->4->4
    
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
        if l1 is None or l2 is None:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def printList(self, head):
        while head:
            print(head.val, end="->")
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node11, node12, node13 = ListNode(1), ListNode(2), ListNode(4)
    node11.next, node12.next = node12, node13
    node21, node22, node23 = ListNode(1), ListNode(3), ListNode(4)
    node21.next, node22.next = node22, node23
    solution.printList(solution.mergeTwoLists(node11, node21))


