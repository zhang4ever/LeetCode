#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MergeKSortedLists.py
# @Time    : 2018-09-08 17:21
# @Author  : zhang bo
# @Note    : Merge k Sorted Lists
"""
"""
题目描述：Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
示例:Input:[1->4->5,1->3->4,2->6]
    Output: 1->1->2->3->4->4->5->6
思路：将K个链表合并的原始的问题分成多次两个链表合并的子问题， 时间复杂度O(nlog(n))
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        while len(lists) > 1:
            lists.insert(0, self.mergeTwoLists(lists[-1], lists[-2]))  # 合并前两个，并插入
            lists.pop()  # 依次丢掉已经合并过的链表
            lists.pop()
        return lists[0]


    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return
        if list1 is None or list2 is None:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


    def printList(self, head):
        while head:
            print(head.val, end='->')
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    n11, n12, n13 = ListNode(1), ListNode(4), ListNode(5)
    n11.next, n12.next = n12, n13
    n21, n22, n23 = ListNode(1), ListNode(3), ListNode(4)
    n21.next, n22.next = n22, n23
    n31, n32 = ListNode(2), ListNode(6)
    n31.next = n32
    lists = [n11, n21, n31]
    solution.printList(solution.mergeKLists(lists))
