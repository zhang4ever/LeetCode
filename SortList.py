#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SortList.py
# @Time    : 2018-09-01 22:43
# @Author  : zhang bo
# @Note    : Sort List
"""
"""
题目描述：Sort a linked list in O(n log n) time using constant space complexity.
示例：Input: 4->2->1->3;Output: 1->2->3->4
    Input: -1->5->3->4->0;Output: -1->0->3->4->5
思路：O(n log n)的时间复杂度，可以考虑快速排序或者归并排序等
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        left = head
        middle = self.FindMidNode(head)
        right = middle.next
        middle.next = None
        head1 = self.sortList(left)  # 递归
        head2 = self.sortList(right)
        return self.merge(head1, head2)  # 归并


    def FindMidNode(self, head):
        # 使用快慢两个指针
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow


    def merge(self, head1, head2):
        curr = ListNode(None)
        node = curr
        while head1 and head2:
            if head1.val <= head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        node.next = head1 or head2
        # 将已经合并好的复制到原始的数组中
        return curr.next


if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    ans = solution.sortList(node1)
    while ans:
        print(ans.val)
        ans = ans.next