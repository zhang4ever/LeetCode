#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RemoveDuplicatesFromSortedList.py
# @Time    : 2018-09-03 15:36
# @Author  : zhang bo
# @Note    : Remove Duplicates from Sorted List
"""

"""
题目描述：Given a sorted linked list, delete all duplicates such that each element appear only once.
示例：Input: 1->1->2 ； Output: 1->2
    Input: 1->1->2->3->3； Output: 1->2->3
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy


    def printList(self, head):
        while head:
            print(head.val, end="->")
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = ListNode(1), ListNode(1), ListNode(1)
    node4, node5 = ListNode(3), ListNode(3)
    node1.next, node2.next = node2, node3
    node3.next, node4.next = node4, node5
    solution.printList(solution.deleteDuplicates(node1))