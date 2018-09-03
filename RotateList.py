#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RotateList.py
# @Time    : 2018-09-03 22:38
# @Author  : zhang bo
# @Note    : Rotate List
"""
"""
题目描述：Given a linked list, rotate the list to the right by k places, where k is non-negative.
示例：Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1  # 得到链表的长度
        k = k % n  # 如果n<k时
        if k == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(n - k):  # 找到需要反转的位置
            pre = pre.next
        new = cur = pre.next
        pre.next = None  # 以该位置截断
        while cur.next:
            cur = cur.next
        cur.next = dummy.next  # 拼接
        return new

    def printList(self, head):
        while head:
            print(head.val, end="->")
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3, node4, node5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5),
    node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
    solution.printList(solution.rotateRight(node1, k=2))