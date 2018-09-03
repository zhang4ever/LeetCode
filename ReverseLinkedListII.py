#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReverseLinkedListII.py
# @Time    : 2018-09-02 22:27
# @Author  : zhang bo
# @Note    : Reverse Linked List II
"""
"""
题目描述：Reverse a linked list from position m to n. Do it in one-pass.
示例：Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
限制条件：1 ≤ m ≤ n ≤ length of list.
思路:先找到m的位置，然后反转[m,n]之间的节点，最后将剩下的的节点连接起来。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m > n:
            return
        dummy = ListNode(0)
        dummy.next = head  # 0>1>2>3>4>5
        prev = dummy
        for _ in range(m-1):
            prev = prev.next  # prev:0>1; m=2, n=4
        start = prev.next  # start: 2
        then = start.next  # then :3
        for _ in range(n-m):  # 反转中间
            start.next = then.next
            then.next = prev.next
            prev.next = then
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
    ans = solution.reverseBetween(node1, 2, 4)
    solution.printList(ans)


