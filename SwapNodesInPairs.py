#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SwapNodesInPairs.py
# @Time    : 2018-09-08 16:20
# @Author  : zhang bo
# @Note    : Swap Nodes in Pairs
"""

"""
题目描述：Given a linked list, swap every two adjacent nodes and return its head.
示例：Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 递归
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newStart = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(newStart)
        return head

    def printList(self, head):
        while head:
            print(head.val, end='->')
            head = head.next

if __name__ == '__main__':
    solution = Solution()
    node1, node2 = ListNode(1), ListNode(2)
    node3, node4 = ListNode(3), ListNode(4)
    node1.next, node2.next = node2, node3
    node3.next = node4
    solution.printList(solution.swapPairs(node1))
