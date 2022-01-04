import unittest


from Node import Node

class MyTestCase(unittest.TestCase):

    def test_something(self):
        n1 = Node((1, 2, 3), 1)
        n2 = Node((3, 5, 6), 2)
        self.assertEqual(1,n1.getId())
        self.assertEqual(3, n2.getX())
        self.assertEqual(2, n1.getY())








if __name__ == '__main__':
    unittest.main()
