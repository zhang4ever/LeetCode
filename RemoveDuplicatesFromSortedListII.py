#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : RemoveDuplicatesFromSortedListII.py
# @Time    : 2018-09-03 16:40
# @Author  : zhang bo
# @Note    : Remove Duplicates from Sorted List II
"""

"""
题目描述：Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
示例：Input: 1->2->3->3->4->4->5; Output: 1->2->5
"""
# Definition for singly-linked list.
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
        if head is None:
            return
        curr = head
        dummy = res = ListNode(0)
        while curr and curr.next:
            if curr.val != curr.next.val:
                res.next = curr
                curr = curr.next
                res = res.next
            else:  # 有重复，则删除
                res.next = None
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
        if curr:
            res.next = curr
        return dummy.next

    def printList(self, head):
        while head:
            print(head.val, end="->")
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = ListNode(1), ListNode(1), ListNode(1)
    node4, node5 = ListNode(2), ListNode(3)
    node1.next, node2.next = node2, node3
    node3.next, node4.next = node4, node5
    solution.printList(solution.deleteDuplicates(node1))