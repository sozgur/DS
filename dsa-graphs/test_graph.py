import imp
import unittest
from graph import Graph 
from graph import Node

class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.a = Node('A', set())
        self.b = Node('B', set())
        self.c = Node('C', set())
        self.graph = Graph()  

    def tearDown(self):
        del self.graph
        

    def test_add_vertex(self):
        self.graph.add_vertex(self.a)
        self.assertTrue(self.graph.has(self.a))

    def test_add_vertices(self):
        self.graph.add_vertices([self.b, self.c])
        self.assertTrue(self.graph.has(self.b))
        self.assertTrue(self.graph.has(self.c))
        self.assertFalse(self.graph.has(self.a))

    def test_add_edge(self):
        self.graph.add_vertices([self.a, self.b, self.c])
        self.graph.add_edge(self.a, self.b)
        self.graph.add_edge(self.a, self.c)
        self.assertTrue(self.b in self.a.adjacent)
        self.assertTrue(self.c in self.a.adjacent)
        self.assertTrue(self.a in self.c.adjacent)

    def test_remove_edge(self):
        self.graph.add_vertices([self.a, self.b, self.c])
        self.graph.add_edge(self.a, self.b)
        self.graph.add_edge(self.a, self.c)
        self.graph.remove_edge(self.a, self.b)
        self.graph.remove_edge(self.a, self.c)
        self.assertFalse(self.b in self.a.adjacent)
        self.assertFalse(self.c in self.a.adjacent)
        self.assertFalse(self.a in self.c.adjacent)


    def test_remove_vertex(self):
        self.graph.add_vertices([self.a, self.b, self.c])
        self.graph.add_edge(self.a, self.b)
        self.graph.add_edge(self.a, self.c)
        self.graph.add_edge(self.b, self.c)
        self.graph.remove_vertex(self.a)
        self.assertFalse(self.graph.has(self.a))
        self.assertFalse(self.a in self.b.adjacent)
        self.assertFalse(self.a in self.c.adjacent)

    
    def test_depth_first_search(self):
        S = Node('S', set())
        P = Node('P', set())
        U = Node('U', set())
        X = Node('X', set())
        Q = Node('Q', set())
        Y = Node('Y', set())
        V = Node('V', set())
        R = Node('R', set())
        W = Node('W', set())
        T = Node('T', set())
        self.graph.add_vertices([S,P,U,X,Q,Y,V,R,W,T])
       
        self.graph.add_edge(S, P)
        self.graph.add_edge(S, U)
        self.graph.add_edge(P, X)
        self.graph.add_edge(U, X)
        self.graph.add_edge(P, Q)
        self.graph.add_edge(U, V)
        self.graph.add_edge(X, Q)
        self.graph.add_edge(X, Y)
        self.graph.add_edge(X, V)
        self.graph.add_edge(Q, R)
        self.graph.add_edge(Y, R)
        self.graph.add_edge(Y, W)
        self.graph.add_edge(V, W)
        self.graph.add_edge(R, T)
        self.graph.add_edge(W, T)

        self.assertCountEqual(self.graph.depth_first_search(S), ["S", "U", "V", "W", "T", "R", "Q", "Y", "X", "P"])

    def test_breadth_first_search(self):
        S = Node('S', set())
        P = Node('P', set())
        U = Node('U', set())
        X = Node('X', set())
        Q = Node('Q', set())
        Y = Node('Y', set())
        V = Node('V', set())
        R = Node('R', set())
        W = Node('W', set())
        T = Node('T', set())
        self.graph.add_vertices([S,P,U,X,Q,Y,V,R,W,T])
       
        self.graph.add_edge(S, P)
        self.graph.add_edge(S, U)
        self.graph.add_edge(P, X)
        self.graph.add_edge(U, X)
        self.graph.add_edge(P, Q)
        self.graph.add_edge(U, V)
        self.graph.add_edge(X, Q)
        self.graph.add_edge(X, Y)
        self.graph.add_edge(X, V)
        self.graph.add_edge(Q, R)
        self.graph.add_edge(Y, R)
        self.graph.add_edge(Y, W)
        self.graph.add_edge(V, W)
        self.graph.add_edge(R, T)
        self.graph.add_edge(W, T)

        self.assertCountEqual(self.graph.breadth_first_search(S), ["S", "P", "U", "X", "Q", "V", "Y", "R", "W", "T"])
         
    def test_shortest_path(self):
        S = Node('S', set())
        P = Node('P', set())
        C = Node('C', set())
        A = Node('A', set())
        O = Node('O', set())
        Y = Node('Y', set())
        R = Node('R', set())
        T = Node('T', set())
        self.graph.add_vertices([S,P,C,A,O,Y,R,T])

        self.graph.add_edge(S, R)
        self.graph.add_edge(S, T)
        self.graph.add_edge(S, O)
        self.graph.add_edge(P, R)
        self.graph.add_edge(P, C)
        self.graph.add_edge(O, C)
        self.graph.add_edge(A, C)
        self.graph.add_edge(A, Y)
        self.graph.add_edge(Y, T)

        self.assertEqual(self.graph.shortest_path(S, C),["S", "O", "C"])