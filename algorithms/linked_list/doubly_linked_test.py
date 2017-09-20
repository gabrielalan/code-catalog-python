import unittest

from doubly_linked import DoublyLinkedList
from node import LinkedListNode

class TestLinkedList(unittest.TestCase):

	def setUp(self):
		self.list = DoublyLinkedList()

	def test_node(self):
		node = LinkedListNode(1)
		stepNode = LinkedListNode(2)

		node.setNext(stepNode)
		node.setPrevious(stepNode)

		self.assertEqual(node.data, 1)
		self.assertEqual(node.next, stepNode)
		self.assertEqual(node.previous, stepNode)

	def test_list_initialization(self):
		self.assertEqual(self.list.head, None)
		self.assertEqual(self.list.tail, None)

	def test_list_insertion(self):
		n1 = self.list.append(1)
		n2 = self.list.append(2)
		n3 = self.list.append(3)
		n0 = self.list.prepend(0)

		self.assertIsInstance(n1, LinkedListNode)
		self.assertEqual(n0, self.list.head)
		self.assertEqual(n2.previous, n1)
		self.assertEqual(n2.next, n3)
		self.assertEqual(n3, self.list.tail)

		n05 = self.list.addBefore(n1, 0.5)
		n15 = self.list.addAfter(n1, 1.5)

		self.assertEqual(n0.next, n05)
		self.assertEqual(n2.previous, n15)

	def test_list_find(self):
		n1 = self.list.append(1)
		n2 = self.list.append(2)
		n3 = self.list.append(3)

		found = self.list.find(lambda data: data == 2)
		not_found = self.list.find(lambda data: data == 999)

		self.assertEqual(found, n2)
		self.assertEqual(not_found, None)

	def test_list_to_array(self):
		n1 = self.list.append(1)
		n2 = self.list.append(2)
		n3 = self.list.append(3)

		array = self.list.to_array()

		self.assertIsInstance(array, list)
		self.assertEqual(len(array), 3)

	def test_list_item_remove(self):
		n1 = self.list.append(1)
		n2 = self.list.append(2)
		n3 = self.list.append(3)

		self.list.remove(n2)

		self.assertEqual(n1.next, n3)
		self.assertEqual(n3.previous, n1)
		self.assertEqual(n2.next, None)
		self.assertEqual(n2.previous, None)

		n3_instance = self.list.pop()

		self.assertEqual(n3_instance, n3)
		self.assertEqual(self.list.head, n1)
		self.assertEqual(self.list.tail, n1)
		self.assertEqual(n1.next, None)
		self.assertEqual(n1.previous, None)

		self.list.addAfter(n1, n2)
		self.list.shift()

		self.assertEqual(self.list.head, n2)
		self.assertEqual(self.list.tail, n2)
		self.assertEqual(n2.next, None)
		self.assertEqual(n2.previous, None)

	def test_list_clear(self):
		self.list.clear()

		self.assertEqual(self.list.head, None)
		self.assertEqual(self.list.tail, None)

		n1 = self.list.append(1)
		n2 = self.list.append(2)

		self.list.clear()

		self.assertEqual(self.list.head, None)
		self.assertEqual(self.list.tail, None)

if __name__ == '__main__':
	unittest.main()