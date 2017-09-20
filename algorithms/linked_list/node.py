'''
Linked List Node reference
'''
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def setNext(self, node):
        self.next = node

    def setPrevious(self, node):
        self.previous = node

    def eraseLinks(self):
        self.previous = None
        self.next = None