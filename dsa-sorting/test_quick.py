import unittest
from quick import swap, pivot, quick_sort


class TestCaseBubbleSort(unittest.TestCase):

    def setUp(self):
        self.arr = [2,3,5,1]
        self.nums = [
            4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34,
            23, 2, 453, 546, 75, 67, 4342, 32
        ]

    def test_swap_function(self):
        swap(self.arr, 1,2)
        self.assertEqual(self.arr, [2,5,3,1])

    def test_pivot_function(self):
        self.assertEqual(pivot(self.arr, 0, len(self.arr)-1), 1)

    def test_quick_sort_function(self):
        self.assertEqual(quick_sort(self.arr), [1,2,3,5])
        self.assertEqual(quick_sort(self.nums), [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342])
