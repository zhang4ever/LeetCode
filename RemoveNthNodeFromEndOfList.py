#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RemoveNthNodeFromEndOfList.py
# @Time    : 2018-09-08 19:23
# @Author  : zhang bo
# @Note    : Remove Nth Node From End of List
"""
"""
题目描述：Given a linked list, remove the n-th node from the end of list and return its head.
示例：Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.
思路1：删除倒数第k个，等价于删除整数N-K个
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return
        cur = head
        length = 0  # 链表总长度
        while cur:
            length += 1
            cur = cur.next
        if n > length:
            return
        if n == length:
            return head.next
        cur = head
        for _ in range(length-n-1):
            cur = cur.next
        cur.next = cur.next.next
        return head

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
    solution.printList(solution.removeNthFromEnd(node1, n=2))
