import unittest
from LinearSearch import linear_search

class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        haystack_test = [1, 27, 4, 2, 4, 2, 7]
        self.assertTrue(linear_search(haystack_test, 27))
        self.assertFalse(linear_search(haystack_test, 99))

if __name__ == '__main__':
    unittest.main() 
