#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ConvertSortedArrayToBinarySearchTree.py
# @Time    : 2018-09-02 18:24
# @Author  : zhang bo
# @Note    : Convert Sorted Array to Binary Search Tree
"""
"""
题目描述：Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
示例：Given the sorted array: [-10,-3,0,5,9],One possible answer is: [0,-3,9,-10,null,5]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        return self.dfs(nums)

    def dfs(self, nums):
        if len(nums) <= 0:
            return
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums[:mid])
        root.right = self.dfs(nums[mid+1:])
        return root

    def printTree(self, root):
        print(root.val)
        if root.left:
            self.printTree(root.left)
        if root.right:
            self.printTree(root.right)

if __name__ == '__main__':
    solution = Solution()
    nums = [-10, -3, 0, 5, 9]
    root = solution.sortedArrayToBST(nums)
    solution.printTree(root)