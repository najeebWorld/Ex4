import unittest

from DiGraph import DiGraph
from Node import Node
from Edges import Edges

class MyTestCase(unittest.TestCase):

    def test_something(self):

        g = DiGraph()
        g.add_node(0, (0, 0, 0))
        g.add_node(1, (1.5, -2.6, 0))
        g.add_node(2, (3.251, 5.987, 0))
        g.add_node(3, (-3.25, 5.25, 0))
        g.add_edge(0, 1, 1.35)
        g.add_edge(0, 2, 5.624)
        g.add_edge(0, 3, 2.45)
        g.add_edge(1, 2, 1.2354)
        g.add_edge(1, 3, 0.54)
        g.add_edge(2, 3, 3.657)
        g.add_edge(3, 0, 2.5)
        g.add_edge(2, 1, 2.5)






        dict1 = dict()
        dict1[0] = Node(0, 0, 0, 0)
        dict1[1] = Node(1.5, -2.6, 0, 1)
        dict1[2] = Node(3.251, 5.987, 0, 2)
        dict1[3] = Node(-3.25, 5.25, 0, 3)


        # test if return the nodes dictionary
        dTest1 = g.get_all_v()
        a0=True
        for x in dTest1:
            if dict1[x]==None:
                a0 = False
        self.assertTrue(a0)

        # test if return the edges_in dictionary for node x
        din = dict()
        din[3] = 2.5
        dTest2 = g.all_in_edges_of_node(0)
        a0 = True
        for x in dTest2:
            print(x)
            if din[x] == None:
                a0 = False
        self.assertTrue(a0)

        # test if return the edges_out dictionary for node x
        dout = dict()
        dout[0] = 2.5
        dTest3 = g.all_out_edges_of_node(3)
        a0 = True
        for x in dTest3:
            print(x)
            if dout[x] == None:
                a0 = False
        self.assertTrue(a0)







        # check the amount of nodes in the graph
        self.assertEqual(4, g.v_size())

        # check the amount of edges in the graph
        self.assertEqual(8, g.e_size())

        # check if the mc is correct
        self.assertEqual(12, g.get_mc())

        # check if the first node was added
        a1 = False
        if 0 in g.nodeD:
            a1 = True
        self.assertTrue(a1)



        # check if the first edge was added
        s1 = (0, 1)
        a3 = False
        if s1 in g.edgeD:
            a3 = True
        self.assertTrue(a3)
        


        # check if edge is removed
        a3 = g.remove_edge(0, 1)
        self.assertTrue(a3)




        # check if node is removed
        a4 = g.remove_node(2)
        self.assertEquals(3, g.e_size())  # make sure the edges were removed
        self.assertTrue(a4)



        # check repr of graph
        print(g)


if __name__ == '__main__':
    unittest.main()
