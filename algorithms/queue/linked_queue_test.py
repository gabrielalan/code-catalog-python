import unittest

from linked_queue import LinkedQueue

class TestSquareRootMethods(unittest.TestCase):

	def setUp(self):
		self.queue = LinkedQueue()

	def test_empty(self):
		self.assertTrue(self.queue.empty())

	def test_enqueue(self):
		i1 = self.queue.enqueue(1)

		self.assertEqual(self.queue.tail, i1)

	def test_dequeue(self):
		i1 = self.queue.enqueue(1)
		i2 = self.queue.enqueue(2)
		i3 = self.queue.enqueue(3)

		self.assertEqual(self.queue.head, i1)
		self.assertEqual(self.queue.tail, i3)

		self.assertEqual(self.queue.dequeue(), i1)
		self.assertEqual(self.queue.head, i2)
		self.assertEqual(self.queue.tail, i3)

if __name__ == '__main__':
	unittest.main()