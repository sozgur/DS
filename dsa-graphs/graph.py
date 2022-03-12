import queue


class Node:
    def __init__(self, val, adjacent=set()):
        self.val = val
        self.adjacent = adjacent

class Graph:
    def __init__(self):
        self.nodes = set()

    # this function accepts a Node instance and adds it to the nodes property on the graph
    def add_vertex(self, node):
        self.nodes.add(node)    

    # this function accepts an list of Node instances and adds them to the nodes property on the graph
    def add_vertices(self, node_list):
        for node in node_list:
            self.nodes.add(node)

    # this function check node if in graph
    # return true/false
    def has(self, node):
        return node in self.nodes 

    # this function accepts two vertices and updates their adjacent values to include the other vertex
    def add_edge(self, v1, v2):
        # check vertices if in graph
        if not self.has(v1) and not self.has(v2):
            return
        
        v1.adjacent.add(v2)
        v2.adjacent.add(v1)

    
    # this function accepts two vertices and updates their adjacent values to remove the other vertex
    def remove_edge(self, v1, v2):
        # check vertices if in graph
        if not self.has(v1) and not self.has(v2):
            return
        
        if v2 in v1.adjacent:
            v1.adjacent.remove(v2)

        if v1 in v2.adjacent:
            v2.adjacent.remove(v1)

    # this function accepts a vertex and removes it from the nodes property, 
    # it also updates any adjacency lists that include that vertex
    def remove_vertex(self, vertex):
        if not self.has(vertex):
            return
       
        for node in self.nodes:
            # print(adj_node.adjacent)
            if vertex in node.adjacent:
                node.adjacent.remove(vertex)

        self.nodes.remove(vertex)

    # this function returns an array of Node values using DFS 
    def depth_first_search(self, start):
        stack = [start]
        result = []
        seen = set()
        seen.add(start)

        while stack:
            node = stack.pop()
            result.append(node.val)
   
            for adj in node.adjacent:
                if adj not in seen:
                    stack.append(adj)
                    seen.add(adj)

        return result

    # this function returns an array of Node values using BFS
    def breadth_first_search(self, start):
        queue = [start]
        result = []
        seen = set()
        seen.add(start)

        while queue:
            node = queue.pop(0)
            result.append(node.val)

            for adj in node.adjacent:
                if adj not in seen:
                    queue.append(adj)
                    seen.add(adj)

        return result

    def shortest_path(self, start, end):
        queue = [start]
        visited = set()
        visited.add(start)
        predecessors = {}
        path = []

        while queue:
            currentVertex = queue.pop(0)

            if currentVertex.val == end.val:
                stop = predecessors[end.val]
                while stop:
                    path.append(stop)
                    stop = predecessors.get(stop)

                path.insert(0, end.val)
                path.reverse()
                return path

            
            for vertex in currentVertex.adjacent:
                if vertex not in visited:
                    queue.append(vertex)
                    predecessors[vertex.val] = currentVertex.val
                    visited.add(vertex)


S = Node('S', set())
P = Node('P', set())
C = Node('C', set())
A = Node('A', set())
O = Node('O', set())
Y = Node('Y', set())
R = Node('R', set())
T = Node('T', set())
graph = Graph()
graph.add_vertices([S,P,C,A,O,Y,R,T])
graph.add_edge(S, R)
graph.add_edge(S, T)
graph.add_edge(S, O)
graph.add_edge(P, R)
graph.add_edge(P, C)
graph.add_edge(O, C)
graph.add_edge(A, C)
graph.add_edge(A, Y)
graph.add_edge(Y, T)

graph.shortest_path(S, C)