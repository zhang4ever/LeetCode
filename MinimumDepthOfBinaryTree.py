
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : MinimumDepthOfBinaryTree.py
# @Time    : 2018-09-01 22:20
# @Author  : zhang bo
# @Note    : 二叉树的最小深度
"""
'''
题目描述：Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
示例：Given binary tree [3,9,20,null,null,15,7],return its minimum depth = 2.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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
        else:  # 左右子树都有，取最小
            return 1 + min(self.dfs(root.left), self.dfs(root.right))

