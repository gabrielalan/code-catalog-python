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

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def find(self, compare):
		node = None
		current = self.head

		while not node:
			if compare(current.data):
				return current

			if not current.next:
				return None

			current = current.next;

	def remove(self, node):
		if not isinstance(node, LinkedListNode):
			raise ValueError("Invalid node: You need to provide a valid node to remove. You can use .find() method")

		next = node.next;
		previous = node.previous;

		if not next and not previous and (node == self.head or node == self.tail):
			return self.clear()

		if node == self.head:
			self.head = node.next
			self.head.setPrevious(None)
		elif node == self.tail:
			self.tail = node.previous
			self.head.setNext(None)
		else:
			previous.setNext(next)
			next.setPrevious(previous)

		node.eraseLinks()

		return node

	def shift(self):
		if not self.head:
			return None

		if self.tail == self.head:
			return self.clear()

		node = self.head
		self.head = node.next
		self.head.setPrevious(None)

		node.eraseLinks()

		return node

	def pop(self):
		if not self.tail:
			return None

		if self.tail == self.head:
			return self.clear()

		node = self.tail
		self.tail = node.previous
		self.tail.setNext(None)

		node.eraseLinks()

		return node

	def clear(self):
		node = None

		if self.head and self.tail == self.head:
			node = self.head
			node.eraseLinks()

		self.head = None
		self.tail = None

		return node

	def verifyNodes(self, anchor, data):
		node = LinkedListNode(data) if not isinstance(data, LinkedListNode) else data

		if not isinstance(anchor, LinkedListNode):
			raise ValueError("Invalid anchor node: You need to provide a valid node as anchor. You can use .find() method")

		return node
	
	def addAfter(self, anchor, data):
		node = self.verifyNodes(anchor, data)

		node.setPrevious(anchor)
		
		if anchor == self.tail:
			self.tail = node
		else:
			node.setNext(anchor.next)
			anchor.next.setPrevious(node)

		anchor.setNext(node)

		return node

	def addBefore(self, anchor, data):
		node = self.verifyNodes(anchor, data)

		node.setNext(anchor)

		if anchor == self.head:
			self.head = node
		else:
			node.setPrevious(anchor.previous)
			anchor.previous.setNext(node)

		anchor.setPrevious(node)

		return node

	def prepend(self, data):
		node = LinkedListNode(data) if not isinstance(data, LinkedListNode) else data

		if not self.head:
			self.head = self.tail = node;
		else:
			self.head.setPrevious(node)
			node.setNext(self.head)
			self.head = node

		return node

	def append(self, data):
		node = LinkedListNode(data) if not isinstance(data, LinkedListNode) else data

		if not self.tail:
			self.head = self.tail = node
		else:
			self.tail.setNext(node)
			node.setPrevious(self.tail)
			self.tail = node

		return node