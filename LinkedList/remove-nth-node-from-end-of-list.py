# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# case 1
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        front, back = head, head

        for i in range(n):
            front = front.next

        while front is not None:
            front = front.next
            back = back.next

        removeNode = head
        if removeNode.next is None or removeNode is back:
            head = back.next
        else:
            while removeNode.next is not back:
                removeNode = removeNode.next
            removeNode.next = back.next

        return head

# case 2. two pointer
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
