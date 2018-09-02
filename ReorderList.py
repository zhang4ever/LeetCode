<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReorderList.py
# @Time    : 2018-09-02 09:27
# @Author  : zhang bo
# @Note    : Reorder List
"""
"""
题目描述：Given a singly linked list L:L0->L1->...->Ln-1->Ln,  reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
    You may not modify the values in the list's nodes, only nodes itself may be changed.
示例：Given 1->2->3->4, reorder it to 1->4->2->3.
思路：先找到链表的中间节点，然后依次将链表划分成两段，再讲第二段反转，再依次合并
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        if head is None:
            return
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        p = self.FindMiddleNode(head)  # 中间点
        prev = p
        pp = p.next  # 第二段
        pp = self.ReverseList(pp)  # 反转第二段
        prev.next = pp

        p = head
        pp = prev.next
        while p != prev:
            prev.next = pp.next
            pp.next = p.next
            p.next = pp
            p = pp.next
            pp = prev.next

    # 找到中间节点
    def FindMiddleNode(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def ReverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            reversedNode = self.ReverseList(head.next)
            head.next.next = head
            head.next = None
            return reversedNode

    def printList(self, head):
        while head:
            print(head.val, end='->')
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node1, node2 = ListNode(1), ListNode(2)
    node3, node4 = ListNode(3), ListNode(4)
    node5 = ListNode(5)
    node1.next, node2.next = node2, node3
    node3.next, node4.next = node4, node5
    solution.reorderList(node1)
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File    : ReorderList.py
# @Time    : 2018-09-02 09:27
# @Author  : zhang bo
# @Note    : Reorder List
"""
"""
题目描述：Given a singly linked list L:L0->L1->...->Ln-1->Ln,  reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
    You may not modify the values in the list's nodes, only nodes itself may be changed.
示例：Given 1->2->3->4, reorder it to 1->4->2->3.
思路：先找到链表的中间节点，然后依次将链表划分成两段，再讲第二段反转，再依次合并
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        if head is None:
            return
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        p = self.FindMiddleNode(head)  # 中间点
        prev = p
        pp = p.next  # 第二段
        pp = self.ReverseList(pp)  # 反转第二段
        prev.next = pp

        p = head
        pp = prev.next
        while p != prev:
            prev.next = pp.next
            pp.next = p.next
            p.next = pp
            p = pp.next
            pp = prev.next

    # 找到中间节点
    def FindMiddleNode(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def ReverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            reversedNode = self.ReverseList(head.next)
            head.next.next = head
            head.next = None
            return reversedNode

    def printList(self, head):
        while head:
            print(head.val, end='->')
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    node1, node2 = ListNode(1), ListNode(2)
    node3, node4 = ListNode(3), ListNode(4)
    node5 = ListNode(5)
    node1.next, node2.next = node2, node3
    node3.next, node4.next = node4, node5
    solution.reorderList(node1)
>>>>>>> fe274beb9cba3472edb39762a6c5dde1cb5aa71c
    solution.printList(node1)