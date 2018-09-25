#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : PathSum.py
# @Time    : 2018-09-24 16:47
# @Author  : zhang bo
# @Note    : Path Sum
"""
"""
题目描述：Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all 
    the values along the path equals the given sum.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, expected):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return 0
        res_paths = []  # 记录所有的路径
        curr_paths = []  # 当前路径
        self.findPath(root, expected, res_paths, curr_paths)
        return True if expected in res_paths else False

    # 递归实现，返回路径的和==给定值的结果。
    def findPath(self, root, expected, res_paths, curr_paths):
        curr_paths.append(root.val)
        is_leaf = root.left is None and root.right is None
        if expected == sum(curr_paths) and is_leaf:
            res_paths.append(sum(curr_paths))
        if root.left:
            self.findPath(root.left, expected, res_paths, curr_paths)
        if root.right:
            self.findPath(root.right, expected, res_paths, curr_paths)
        curr_paths.pop()

if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = TreeNode(5),TreeNode(4), TreeNode(8)
    node4, node5, node6 = TreeNode(11), TreeNode(13), TreeNode(4)
    node7, node8, node9 = TreeNode(7), TreeNode(2), TreeNode(1)
    node1.left, node1.right = node2, node3
    node2.left = node4
    node3.left, node3.right = node5, node6
    node4.left, node4.right = node7, node8
    node6.right = node9
    print(solution.hasPathSum(node1, expected=22))
