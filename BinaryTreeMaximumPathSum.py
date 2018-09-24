#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : BinaryTreeMaximumPathSum.py
# @Time    : 2018-09-23 23:54
# @Author  : zhang bo
# @Note    : Binary Tree Maximum Path Sum
"""
"""
题目说明：Given a non-empty binary tree, find the maximum path sum。For this problem, a path is defined as any 
    sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path 
    must contain at least one node and does not need to go through the root.
示例：Input: [1,2,3] ；Output: 6
    Input: [-10,9,20,null,null,15,7]；Output: 42
思路：先序，递归。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        self.ans = -10000001
        self.findPath(root)
        return self.ans

    def findPath(self, root):
        if root is None:
            return 0
        leftSum = self.findPath(root.left)
        rightSum = self.findPath(root.right)
        res = root.val
        if leftSum > 0:
            res += leftSum
        if rightSum > 0:
            res += rightSum
        self.ans = max(res, self.ans)
        if max(leftSum, rightSum) > 0:
            return max(leftSum, rightSum) + root.val
        else:
            return root.val



if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = TreeNode(-10), TreeNode(9), TreeNode(20)
    node4, node5 = TreeNode(15), TreeNode(7)
    node1.left, node1.right = node2, node3
    node3.left, node3.right = node4, node5
    print(solution.maxPathSum(node1))