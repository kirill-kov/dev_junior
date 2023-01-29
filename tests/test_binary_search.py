import unittest

from algorithms.binary_search import binary_search, binary_search_recursive


class TestBinarySearch(unittest.TestCase):
    def setUp(self) -> None:
        self.sort_array = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12]

    def test_binary_search(self):
        self.assertEqual(binary_search(1, self.sort_array), 0)
        self.assertEqual(binary_search(2, self.sort_array), 1)
        self.assertEqual(binary_search(0, self.sort_array), -1)

    def test_binary_search_recursive(self):
        self.assertEqual(binary_search_recursive(1, self.sort_array, 0, len(self.sort_array)), 0)
        self.assertEqual(binary_search_recursive(2, self.sort_array, 0, len(self.sort_array)), 1)
        self.assertEqual(binary_search_recursive(0, self.sort_array, 0, len(self.sort_array)), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
