# problem: Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size or self.head is None:
            return -1

        current = self.head
        for i in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        current = self.head
        if current is None:
            self.head = Node(val)
        else:
            while current.next is not None:
                current = current.next
            current.next = Node(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            node = Node(val)
            node.next = current.next
            current.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        current = self.head
        if index == 0:
            self.head = current.next
        else:
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1
