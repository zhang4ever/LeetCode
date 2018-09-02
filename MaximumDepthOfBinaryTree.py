#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MaximumDepthOfBinaryTree.py
# @Time    : 2018-09-01 22:35
# @Author  : zhang bo
# @Note    : Maximum Depth Of Binary Tree
"""
"""
题目描述：Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
示例：Given binary tree [3,9,20,null,null,15,7], return its depth = 3.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):

        if not root:
            return 0
        return self.dfs(root)

    def dfs(self, root):
        if not root.left and not root.right:  # 只有一个root节点
            return 1
        elif not root.right:  # 只有左子树
            return 1 + self.dfs(root.left)
        elif not root.left:  # 只有右子树
            return 1 + self.dfs(root.right)
        else:
            return 1 + max(self.dfs(root.left), self.dfs(root.right))
