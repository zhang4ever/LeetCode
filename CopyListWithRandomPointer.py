#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : CopyListWithRandomPointer.py
# @Time    : 2018-09-02 15:01
# @Author  : zhang bo
# @Note    : Copy List with Random Pointer
"""
"""
题目描述：A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
思路：复杂链表的复制
"""

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return
        # step1:复制每个节点的值，并将其加在当前节点的后面
        p = head
        while p:
            cloned = RandomListNode(None)
            cloned.label = p.label
            cloned.random = None
            cloned.next = p.next
            # 将当前节点与复制的节点连接起来
            p.next = cloned
            p = cloned.next

        # step2: 重新设置random指针
        p = head
        while p:
            cloned = p.next  # 当前节点的复制节点
            if p.random:
                cloned.random = p.random.next
            p = cloned.next

        # step3: 拆除原本的节点
        p = head
        if p:  # 初始化复制后的head
            cloned_head = cloned = p.next  # cloned_head和cloned分别用来返回结果和当前操作节点
            p.next = cloned.next
            p = p.next
        while p:
            cloned.next = p.next
            cloned = cloned.next
            p.next = cloned.next
            p = p.next
        return cloned_head


if __name__ == '__main__':
    solution = Solution()
    head = RandomListNode('A')
    node1 = RandomListNode('B')
    node2 = RandomListNode('C')
    node3 = RandomListNode('D')
    node4 = RandomListNode('E')
    head.next = node1
    head.random = node2
    node1.next = node2
    node1.random = node4
    node2.next = node3
    node3.next = node4
    node3.random = node1
    cloned = solution.copyRandomList(head)
    print(cloned.label)
    print(cloned.next.label)
    print(cloned.next.next.label)
    print(cloned.next.next.next.label)
    print(cloned.random.label)
    print(cloned.next.random.label)
