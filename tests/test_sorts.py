import unittest

from algorithms.bubble_sort import bubble_sort
from algorithms.exchange_sort import exchange_sort_v1, exchange_sort_v2
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort


class TestSortsAlg(unittest.TestCase):

    def setUp(self) -> None:
        self.unsort_array = [12, 4, 1, 11, 7, 2, 9, 8, 5, 3]
        self.sort_array = sorted(self.unsort_array)  # [1, 2, 3, 4, 5, 7, 8, 9, 11, 12]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.unsort_array), self.sort_array)

    def test_exchange_sort(self):
        self.assertEqual(exchange_sort_v1(self.unsort_array), self.sort_array)
        self.assertEqual(exchange_sort_v2(self.unsort_array), self.sort_array)

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.unsort_array), self.sort_array)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.unsort_array), self.sort_array)


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
