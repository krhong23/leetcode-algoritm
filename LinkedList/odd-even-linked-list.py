'''
problem

Given the head of a singly linked list,
group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        node = head
        odd = None
        even = None
        while node is not None:
            if count % 2 == 0:
                odd = self._addNode(odd, node)
                print('odd', count, node)
            else:
                even = self._addNode(even, node)
                print('even', count, node)
            node = node.next
            count += 1
        print('ODD', odd)
        print('EVEN', even)
        result = None
        while odd is not None:

        odd.next = even
        return odd

    def _addNode(self, nodes, node):
        if nodes is None:
            nodes = node
        else:
            nodes.next = node
        return nodes
