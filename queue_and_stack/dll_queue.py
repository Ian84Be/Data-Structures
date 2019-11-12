import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(None)

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        value = self.storage.remove_from_head()
        return value

    def len(self):
        return self.storage.length
