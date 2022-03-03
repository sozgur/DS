class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Tree:
    def __init__(self, root = None):
        self.root = root


    def sumValues(self):
        total = 0
        if self.root is None:
            return 0
        stack = [self.root]
   
        while len(stack) > 0:
            node = stack.pop()
            total += node.val
            for c in node.children:
                stack.append(c)

        return total

    def countEvens(self):
        total = 0
        if self.root is None:
            return 0
        stack = [self.root]
   
        while len(stack) > 0:
            node = stack.pop()
            if(node.val%2==0):
                total += 1
            for c in node.children:
                stack.append(c)

        return total


    def numGreater(self, lowerBound):
        total = 0
        if self.root is None:
            return 0
        stack = [self.root]
   
        while len(stack) > 0:
            node = stack.pop()
            if(node.val<lowerBound):
                total += 1
            for c in node.children:
                stack.append(c)

        return total



node1 = Node(1,[])
node2 = Node(2,[])
node3 = Node(3,[])
node4 = Node(4,[])
node1.children = [node2, node3]
node3.children = [node4]
tree = Tree(node1)
print(tree.sumValues()) #10
print(tree.countEvens()) #2
print(tree.numGreater(5))
