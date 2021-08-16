# problem : Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        reverse = self._reverseList(slow)

        while reverse is not None:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next

        return True

    def _reverseList(self, head):
        reverse = None
        while head:
            current = head
            head = head.next
            current.next = reverse
            reverse = current
        return reverse
