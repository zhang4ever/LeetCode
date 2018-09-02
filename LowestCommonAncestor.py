#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : LowestCommonAncestor.py
# @Time    : 2017-08-17 22:40
# @Author  : zhang bo
# @Note    : 
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
       
        """
        if root is None or p is None or q is None:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root