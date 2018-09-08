#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReverseLinkedList.py
# @Time    : 2018-09-02 22:01
# @Author  : zhang bo
# @Note    : Reverse Linked List
"""
"""
题目描述：Reverse a singly linked list.
示例：Input: 1->2->3->4->5->NULL； Output: 5->4->3->2->1->NULL
限制条件：A linked list can be reversed either iteratively or recursively.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 使用递归
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        reversedList = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversedList

    # 使用迭代的思路
    def reverseListIterately(self, head):
        if head is None:
            return
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        start = pre.next
        then = start.next
        while then:
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return dummy.next

    def printList(self, head):
        while head:
            print(head.val, end='->')
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = ListNode(1), ListNode(2), ListNode(3)
    node4, node5 = ListNode(4), ListNode(5)
    node1.next, node2.next = node2, node3
    node3.next, node4.next = node4, node5
    res = solution.reverseListIterately(node1)
    solution.printList(res)