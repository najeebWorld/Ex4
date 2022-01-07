import unittest

from client_python.Edges import Edges
from client_python.Node import Node
from client_python.Pokemon import Pokemon


class MyTestCase(unittest.TestCase):
    def test_something(self):
        g = (1, 2, 3)
        p = Pokemon(1, 3, g)
        self.assertEqual(p.getType(), 1)
        self.assertEqual(p.getValue(), 3)
        self.assertEqual(p.getPos(), g)
        g1 = (1, 1, 2)
        g2 = (2, 2, 1)
        n1 = Node(1, g1)
        n2 = (2, g2)
        e = Edges(n1, n2, 3)
        p.setEdge(e)
        self.assertEqual(p.getEdge(),e)


if __name__ == '__main__':
    unittest.main()
