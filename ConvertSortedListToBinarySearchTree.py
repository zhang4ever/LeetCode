#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ConvertSortedListToBinarySearchTree.py
# @Time    : 2018-09-02 16:31
# @Author  : zhang bo
# @Note    : Convert Sorted List to Binary Search Tree
"""
"""
题目描述：Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        return self.dfs(head, None)

    def dfs(self, start, end):
        if start == end:
            return
        # 找到中间的节点作为根节点
        slow = fast = start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.dfs(start, slow)
        root.right = self.dfs(slow.next, end)
        return root

    def printTree(self, root):
        print(root.val)
        if root.left:
            self.printTree(root.left)
        if root.right:
            self.printTree(root.right)


if __name__ == '__main__':
    solution = Solution()
    node1, node2 = ListNode(-10), ListNode(-3)
    node3, node4 = ListNode(0), ListNode(5)
    node5 = ListNode(9)
    node1.next, node2.next = node2, node3
    node3.next, node4.next = node4, node5
    ans = solution.sortedListToBST(node1)
    solution.printTree(ans)