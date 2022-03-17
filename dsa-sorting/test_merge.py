import unittest
from merge import merge, merge_sort

class TestMergeFunctions(unittest.TestCase):
    def setUp(self):
        self.nums = [
            4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2,
            453, 546, 75, 67, 4342, 32
        ]

        self.arr1 = [-2,-1,0,4,5,6]
        self.arr2 = [-3,-2,-1,2,3,5,7,8]

    def test_merge_function(self):
        self.assertEqual(merge(self.arr1, self.arr2), [-3,-2,-2,-1,-1,0,2,3,4,5,5,6,7,8])

    def test_merge_sort_function(self):
        self.assertEqual(merge_sort(self.nums), [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342])