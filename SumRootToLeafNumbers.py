#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : SumRootToLeafNumbers.py
# @Time    : 2018-09-23 23:08
# @Author  : zhang bo
# @Note    : sum-root-to-leaf-numbers
"""
"""
题目描述：Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
    Find the total sum of all root-to-leaf numbers.
思路：先序遍历，依次保存遍历过的路径，然后计算SUM
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res_paths = []  # 记录所有的路径
        curr_paths = []  # 当前路径
        self.findPath(root, res_paths, curr_paths)
        print(res_paths)
        return self.getSum(res_paths)

    def findPath(self, root, res_paths, curr_paths):
        curr_paths.append(root.val)
        is_leaf = root.left is None and root.right is None  # 判断是否是叶子节点
        if is_leaf:
            res_paths.append(curr_paths[:])  # 添加当前的路径
        if root.left:
            self.findPath(root.left, res_paths, curr_paths)
        if root.right:
            self.findPath(root.right, res_paths, curr_paths)
        curr_paths.pop()

    def getSum(self, res_paths):
        res = 0
        for path in res_paths:
            ans = 0
            for i in range(len(path)):
                ans = (ans*10 + path[i])
            res += ans
        return res

if __name__ == '__main__':
    solution = Solution()
    node1, node2, node3 = TreeNode(4), TreeNode(9), TreeNode(0)
    node4, node5 = TreeNode(5), TreeNode(1)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    print(solution.sumNumbers(node1))