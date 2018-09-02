#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : LinkedListCycleII.py
# @Time    : 2018-09-02 14:33
# @Author  : zhang bo
# @Note    : Linked List Cycle II
"""

"""
题目描述：Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.Without using extra space?
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        meetingNode = self.GetMeetingNode(head)
        if meetingNode is None:
            return
        # 统计环中的节点数
        index = 1
        p = meetingNode
        while p.next != meetingNode:
            index += 1
            p = p.next
        slow, fast = head, head

        for _ in range(index):  # fast先走
            fast = fast.next

        while slow != fast:  # slow和fast一起走
            slow = slow.next
            fast = fast.next
        return fast


    def GetMeetingNode(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow
        return


if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = ListNode(1), ListNode(2), ListNode(3)
    node4, node5, node6 = ListNode(4), ListNode(5), ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3
    print(solution.detectCycle(node1).val)