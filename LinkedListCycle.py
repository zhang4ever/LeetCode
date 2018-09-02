#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : LinkedListCycle.py
# @Time    : 2018-09-02 13:48
# @Author  : zhang bo
# @Note    : Linked List Cycle
"""
"""
题目描述：Given a linked list, determine if it has a cycle in it.Can you solve it without using extra space?
思路：设置两个指针slow(走一步)和fast(走两步)，fast先走，如果slow和fast相遇，则说明有环
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


