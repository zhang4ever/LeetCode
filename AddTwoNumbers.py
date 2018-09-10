#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : AddTwoNumbers.py
# @Time    : 2018-09-10 16:27
# @Author  : zhang bo
# @Note    : Add Two Numbers
"""
"""
题目描述：You are given two non-empty linked lists representing two non-negative integers. The digits are stored in 
    reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
示例：Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value_l1 = self.getValueOfList(l1)
        value_l2 = self.getValueOfList(l2)
        sum_value = value_l1 + value_l2
        dummy = cur = ListNode(-1)
        while sum_value >= 10:
            cur.next = ListNode(sum_value % 10)  # 最后一位
            cur = cur.next
            sum_value //= 10
        cur.next = ListNode(sum_value)
        return dummy.next


    def getValueOfList(self, head):
        pos = 1
        res = 0
        while head:
            res += pos * head.val
            pos *= 10
            head = head.next
        return res

    def printList(self, head):
        while head:
            print(head.val, end='->')
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = ListNode(2), ListNode(4), ListNode(3)
    node4, node5, node6 = ListNode(5), ListNode(6), ListNode(4)
    node1.next, node2.next = node2, node3
    node4.next, node5.next = node5, node6
    l1, l2 = node1, node4
    solution.printList(solution.addTwoNumbers(l1, l2))