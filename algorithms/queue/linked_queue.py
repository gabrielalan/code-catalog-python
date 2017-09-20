"""
Queue implementation with Linked List
"""

from ..linked_list.doubly_linked import DoublyLinkedList

class LinkedQueue(DoublyLinkedList):
	def __init__(self):
		DoublyLinkedList.__init__(self)

	def enqueue(self, data):
		return DoublyLinkedList.append(self, data)

	def dequeue(self):
		return DoublyLinkedList.shift(self)