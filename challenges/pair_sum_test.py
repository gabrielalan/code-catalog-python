import unittest

from pair_sum import has_pair_with_sum

class TestBalancedParentheses(unittest.TestCase):

    def test_correct_values(self):
        self.assertTrue(has_pair_with_sum([1, 2, 3, 4, 5], 9))
        self.assertTrue(has_pair_with_sum([1, 2, 3, 4, 4], 8))
        self.assertTrue(has_pair_with_sum([1, 2, 3, 4, 99], 100))

    def test_wrong_values(self):
        self.assertFalse(has_pair_with_sum([1, 2, 3, 4, 5], 57))
        self.assertFalse(has_pair_with_sum([1, 2, 3, 4, 4], 15))
        self.assertFalse(has_pair_with_sum([1, 2, 3, 4, 99], 38))

if __name__ == '__main__':
    unittest.main()