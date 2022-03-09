class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

   # insert(val): insert a new node into the BST with value val.
   # Returns the tree. Uses iteration.
    def insert(self, val):
        newNode = Node(val)

        if self.root is None:
            self.root = newNode
            return self.root
        else:
            node = self.root
            while True:
                if node.val > newNode.val:
                    if node.left is None:
                        node.left = newNode
                        return self.root
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = newNode
                        return self.root
                    else:
                        node = node.right   
        
        

   # insert_recursively(val): insert a new node into the BST with value val.
   # Returns the tree. Uses recursion.
    def insert_recursively(self, val):
        def helperInsert(node, newNode):

            if node.val > newNode.val:
                if node.left is None:
                    node.left = newNode
                else:
                    helperInsert(node.left, newNode)
            else:
                if node.right is None:
                    node.right = newNode
                else:
                    helperInsert(node.right, newNode)     

        newNode = Node(val)

        if self.root is None:
            self.root = newNode
        else:
            helperInsert(self.root, newNode)
        
        return self.root

    #find(val): find a node into the BST with value.
    #Return the node if found, otherwise return None
    def find(self, val):
        if self.root is None:
            return
        currentNode = self.root
        while currentNode:
            if currentNode.val == val:
                return currentNode
            elif currentNode.val > val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

    #find_recursively(val): find a node int the BST with value
    #Return the node if found, otherwise return None
    def find_recursively(self, value):
        def helper_find(node, value):
            if node is None:
                return
            if node.val == value:
                return node
            elif node.val > value:
                return helper_find(node.left, value)
            else:
                return helper_find(node.right, value)

        return helper_find(self.root, value)

    def dfs_pre_order(self):
        result = []

        def helper_pre_order(node, result):
            if node is None:
                return
            
            result.append(node.val)
            helper_pre_order(node.left, result)
            helper_pre_order(node.right, result)

        helper_pre_order(self.root, result)
        return result

    def dfs_in_order(self):
        result = []

        def helper_in_order(node, result):
            if node is None:
                return
            
            helper_in_order(node.left, result)
            result.append(node.val)
            helper_in_order(node.right, result)

        helper_in_order(self.root, result)
        return result

    def dfs_post_order(self):
        result = []

        def helper_post_order(node, result):
            if node is None:
                return
            
            helper_post_order(node.left, result)
            helper_post_order(node.right, result)
            result.append(node.val)

        helper_post_order(self.root, result)
        return result

    def bfs(self):
        result = []
        if self.root is None:
            return result

        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left: 
                queue.append(node.left) 
            if node.right: 
                queue.append(node.right)

        return result

    # remove(val) Removes a node in the BST with the value.
    # Returns the removed node
    def remove(self, val):
        node = self.find(val)

        if node is None:
            return

        def helper_remove(node, parent=None, side=None):
            if node.left:
                node.val = node.left.val
                helper_remove(node.left, parent=node, side="left")
            elif node.right:
                node.val = node.right.val
                helper_remove(node.right, parent=node, side="right")
            else:
                if parent:
                    if side == "left":
                        parent.left = None 
                    else:
                        parent.right = None
                else:
                    self.root = None


        helper_remove(node)
        return self.root

    # returns true if the tree is balanced, otherwise returns false.
    def isBalanced(self):
        if self.root is None:
            return True 

        def helperHeight(node, height=0):
            if node is None:
                return 0

            left_height = helperHeight(node.left, height)
            right_height = helperHeight(node.right, height)

            return max(left_height, right_height) + 1
            
        left_height = helperHeight(self.root.left)
        right_height = helperHeight(self.root.right)

        return abs(left_height - right_height) < 2


    def find_second_highest(self, node=None):
        if self.root is None or (self.root.left is None and self.root.right is None):
            return

        if node is None:
            node = self.root

        while node:
            if node.left and node.right is None:
                return self.find_second_highest(node.left)
            elif node.right and (node.right.right is None and node.right.left is None):
                return node.val
            
            node = node.right

binarySearchTree = BinarySearchTree()
binarySearchTree.insert(15)
binarySearchTree.insert(12)
binarySearchTree.insert(11)
binarySearchTree.insert(14)
binarySearchTree.insert(13)

r=binarySearchTree.find_second_highest()
r
        
    


        
