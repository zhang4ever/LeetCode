#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : PartitionList.py
# @Time    : 2018-09-03 11:22
# @Author  : zhang bo
# @Note    : Partition List
"""

"""
题目描述：Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
示例：Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
限制条件：You should preserve the original relative order of the nodes in each of the two partitions.
思路：将原始的链表划分为两部分，然后将其连接
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return
        dummy1 = p = ListNode(0)
        dummy2 = q = ListNode(0)
        while head:
            if head.val >= x:
                q.next = head
                q = q.next
            else:
                p.next = head
                p = p.next
            head = head.next
        q.next = None
        p.next = dummy2.next  # 去掉开始的0
        return dummy1.next

    def printList(self, head):
        while head:
            print(head.val, end='->')
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = ListNode(1), ListNode(4), ListNode(3)
    node4, node5, node6 = ListNode(2), ListNode(5), ListNode(2)
    node1.next, node2.next = node2, node3
    node3.next, node4.next = node4, node5
    node5.next = node6
    solution.printList(solution.partition(node1, 3))
