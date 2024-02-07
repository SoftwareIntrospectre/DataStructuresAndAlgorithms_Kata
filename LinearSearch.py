'''
    Practice Linear Search in Python. Learn the gist in JavaScript from course, but translate it into Python
'''
from typing import List
import unittest

def linear_search(haystack: List[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            print(f"Needle: {needle} is in Haystack: {haystack}. True")
            return True

    print(f"Needle: {needle} is NOT in Haystack: {haystack}. False")
    return False

class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        haystack_test = [1, 27, 4, 2, 4, 2, 7]
        self.assertTrue(linear_search(haystack_test, 27))
        self.assertFalse(linear_search(haystack_test, 99))

if __name__ == '__main__':
    unittest.main()
