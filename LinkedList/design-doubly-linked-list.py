# problem: Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
class Node(object):

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def _addSize(self, val):
        self.size += val

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size or self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self._addSize(1)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        curr = self.head
        size = self.size
        if curr is None:
            self.addAtHead(val)
        else:
            while curr.next:
                curr = curr.next

            node = Node(val)
            node.prev = curr
            curr.next = node
            self._addSize(1)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head

            for i in range(index - 1):
                curr = curr.next

            node = Node(val)
            node.prev = curr
            node.next = curr.next
            curr.next = node
            self._addSize(1)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            node = curr.next
            curr.next = node.next
            if node.next is not None:
                node.next.prev = curr
        self._addSize(-1)
