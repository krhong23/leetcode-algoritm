'''
problem
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB

        while a is not None:
            while b is not None:
                if a is b:
                    return a
                b = b.next
            a = a.next
            b = headB

        return None


class TwoPointerSolution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        a = headA
        b = headB

        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next

        return a
