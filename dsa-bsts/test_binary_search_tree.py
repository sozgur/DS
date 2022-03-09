import unittest
from binary_search_tree import BinarySearchTree


class BinarySearchTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.binarySearchTree = BinarySearchTree()

    #inserts a node at the correct position
    def test_insert_function(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(20)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.binarySearchTree.insert(16)
        self.binarySearchTree.insert(25)
        self.assertEqual(self.binarySearchTree.root.val, 15)
        self.assertEqual(self.binarySearchTree.root.left.val, 14)
        self.assertEqual(self.binarySearchTree.root.left.left.val, 13)
        self.assertEqual(self.binarySearchTree.root.right.left.val, 16)

    #inserts a node at the correct position
    def test_recursively_insert_function(self):
        self.binarySearchTree.insert_recursively(15)
        self.binarySearchTree.insert_recursively(20)
        self.binarySearchTree.insert_recursively(14)
        self.binarySearchTree.insert_recursively(13)
        self.binarySearchTree.insert_recursively(16)
        self.binarySearchTree.insert_recursively(25)
        self.assertEqual(self.binarySearchTree.root.val, 15)
        self.assertEqual(self.binarySearchTree.root.left.val, 14)
        self.assertEqual(self.binarySearchTree.root.left.left.val, 13)
        self.assertEqual(self.binarySearchTree.root.right.left.val, 16)

    #find a node with value
    def test_find_function(self):
        self.binarySearchTree.insert_recursively(15)
        self.binarySearchTree.insert_recursively(20)
        self.binarySearchTree.insert_recursively(14)
        self.binarySearchTree.insert_recursively(13)
        self.binarySearchTree.insert_recursively(16)
        self.binarySearchTree.insert_recursively(25)
        self.assertEqual(self.binarySearchTree.find(16).val, 16)
        self.assertEqual(self.binarySearchTree.find(25).val, 25)
        self.assertEqual(self.binarySearchTree.find(20).val, 20)
        self.assertEqual(self.binarySearchTree.find(17), None)


    #find a node with value
    def test_find_recursively_function(self):
        self.binarySearchTree.insert_recursively(15)
        self.binarySearchTree.insert_recursively(20)
        self.binarySearchTree.insert_recursively(14)
        self.binarySearchTree.insert_recursively(13)
        self.binarySearchTree.insert_recursively(16)
        self.binarySearchTree.insert_recursively(25)
        self.assertEqual(self.binarySearchTree.find_recursively(16).val, 16)
        self.assertEqual(self.binarySearchTree.find_recursively(25).val, 25)
        self.assertEqual(self.binarySearchTree.find_recursively(20).val, 20)
        self.assertEqual(self.binarySearchTree.find_recursively(17), None)

    #the function search using pre-order depth frst search return and array contaning each node's value.
    def test_function_dfs_pre_order(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(20)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.binarySearchTree.insert(16)
        self.binarySearchTree.insert(25)
        self.assertEqual(self.binarySearchTree.dfs_pre_order(), [15,14,13,20,16,25])

    #the function search using in-order depth frst search return and array contaning each node's value.
    def test_function_dfs_in_order(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(20)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.binarySearchTree.insert(16)
        self.binarySearchTree.insert(25)
        self.assertEqual(self.binarySearchTree.dfs_in_order(), [13,14,15,16,20,25])

    #the function search using post-order deap frst search return and array contaning each node's value.
    def test_function_dfs_post_order(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(20)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.binarySearchTree.insert(16)
        self.binarySearchTree.insert(25)
        self.assertEqual(self.binarySearchTree.dfs_post_order(), [13,14,16,25,20,15])
    
    # the function should search through each node in the binary search tree using breadth first search 
    # and return an array containing each node’s value.
    def test_bfs(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(20)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.binarySearchTree.insert(16)
        self.binarySearchTree.insert(25)
        self.assertEqual(self.binarySearchTree.bfs(), [15,14,20,13,16,25])

    # the function should remove node from binary search tree
    # return the node removed
    def test_remove_function(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(12)
        self.binarySearchTree.insert(20)
        self.binarySearchTree.insert(11)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.binarySearchTree.insert(17)
        self.binarySearchTree.insert(25)
        self.binarySearchTree.insert(16)
        self.binarySearchTree.insert(18)
        self.binarySearchTree.insert(24)
        self.binarySearchTree.insert(30)

        self.binarySearchTree.remove(20)
        
        self.assertEqual(self.binarySearchTree.root.left.val, 12)
        self.assertEqual(self.binarySearchTree.root.right.val, 17)
        self.assertEqual(self.binarySearchTree.root.right.left.val, 16)
        self.assertEqual(self.binarySearchTree.root.right.left.right.val, 18)
        self.assertIsNone(self.binarySearchTree.root.right.left.left)
        
    def test_remove_with_only_one_node(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.remove(15)
        self.assertIsNone(self.binarySearchTree.root)

    def test_isBalanced_function_with_false_case(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(12)
        self.binarySearchTree.insert(20)
        self.binarySearchTree.insert(11)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.assertFalse(self.binarySearchTree.isBalanced())

    def test_isBalanced_function_with_true_case(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(20)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.binarySearchTree.insert(16)
        self.binarySearchTree.insert(25)
        self.assertTrue(self.binarySearchTree.isBalanced())


    def test_find_second_largest(self):
        self.binarySearchTree.insert(15)
        self.binarySearchTree.insert(12)
        self.binarySearchTree.insert(11)
        self.binarySearchTree.insert(14)
        self.binarySearchTree.insert(13)
        self.assertEqual(self.binarySearchTree.find_second_highest(), 14)


