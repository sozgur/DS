import unittest
from bubble_sort import bubble_sort, swap


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

    def test_bubble_sort_function(self):
        self.assertEqual(bubble_sort(self.arr), [1,2,3,5])
        self.assertEqual(bubble_sort(self.nums), [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342])
