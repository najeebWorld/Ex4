import unittest

from Edges import Edges
from Node import Node

class MyTestCase(unittest.TestCase):




    def test_something(self):

        e1 = Edges(3, 5, 3.25)
        e2 = Edges(2, 4, 6.542)
        self.assertEqual(3, e1.getsrc())
        self.assertEqual(5, e1.getdest())
        self.assertEqual(6.542, e2.getweight())
        e1.setweight(5.36)
        self.assertEqual(5.36,e1.getweight())
        


if __name__ == '__main__':
    unittest.main()
