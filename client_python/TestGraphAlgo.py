import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_something(self):


        # creatring graph
        print("\n \n testting")
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

        # creating algo
        myalgo =GraphAlgo(g)
        myalgo.save_to_json("myjson4node1.json")


        # # loading garphs
        algo0 = GraphAlgo()
        algo0.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A0.json")
        algo1 = GraphAlgo()
        algo1.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A1.json")
        algo2 = GraphAlgo()
        algo2.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A2.json")
        algo3 = GraphAlgo()
        algo3.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A3.json")
        algo4 = GraphAlgo()
        algo4.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A4.json")
        algo5 = GraphAlgo()
        algo5.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A5.json")
        algo6 = GraphAlgo()
        algo6.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\T0.json")
        algo7 = GraphAlgo()
        algo7.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\my graph1.json")

        # test for load and save

        algo6.save_to_json("T0copy.json")


        myalgo.save_to_json("myjson4node.json")
        my_algo_new = GraphAlgo()
        my_algo_new.load_from_json("myjson4node.json")
        ans = True
        for n in myalgo.graph.nodeD:
            if myalgo.graph.nodeD[n].getId() != my_algo_new.graph.nodeD[n].getId():
                ans = False
            if myalgo.graph.nodeD[n].getX() != my_algo_new.graph.nodeD[n].getX():
                ans = False
            if myalgo.graph.nodeD[n].getY() != my_algo_new.graph.nodeD[n].getY():
                ans = False
            if myalgo.graph.nodeD[n].getZ() != my_algo_new.graph.nodeD[n].getZ():
                ans = False
        self.assertTrue(ans)
        for e in myalgo.graph.edgeD:
            if myalgo.graph.edgeD[e].getsrc() != my_algo_new.graph.edgeD[e].getsrc():
                ans = False
            if myalgo.graph.edgeD[e].getdest() != my_algo_new.graph.edgeD[e].getdest():
                ans = False
            if myalgo.graph.edgeD[e].getweight() != my_algo_new.graph.edgeD[e].getweight():
                ans = False

        self.assertTrue(ans)


        # test for tsp
        l=[]
        for n in g.nodeD:
            l.append(g.nodeD[n].getId())
        #print(l)

        x =myalgo.TSP(l)
        #print("tsp:", x )
        t1 = x[1] < 10
        self.assertTrue(t1)





        # testing dijsktra
        # x =myalgo.dijasktra(0)
        # print(x[0])
        # print(x[1])
        #
        #testing shortest path
        a1 = myalgo.shortest_path(0, 1)
        b1 = (1.35, [0, 1])
        self.assertEqual(a1, b1)
        a2 = myalgo.shortest_path(0, 2)
        b2 = (2.5854, [0, 1, 2])
        self.assertEqual(a2, b2)
        a3 = myalgo.shortest_path(0, 3)
        b3 = (1.89, [0, 1, 3])
        self.assertAlmostEqual(a3[0], b3[0])
        self.assertEqual(a3[1], b3[1])
        a4 = myalgo.shortest_path(1, 3)
        b4 = (0.54, [1, 3])
        self.assertEquals(a4[0], b4[0])
        self.assertEquals(a4[1], b4[1])


        # testing is conneted
        y=myalgo.isConnected()
        #print(y)
        self.assertTrue(y)
        g.remove_edge(3, 0)
        y = myalgo.isConnected()
        # print(y)
        self.assertFalse(y)


        # testing center
        g.add_edge(3, 0, 2.5)
        myx = myalgo.centerPoint()
        #print("center:" ,myx)
        self.assertEqual(0,myx[0])
        x0 = algo0.centerPoint()
        #print("center:", x0)
        self.assertEqual(7 , x0[0])
        x1 = algo1.centerPoint()
        #print("center:", x1)
        self.assertEqual(8, x1[0])
        x2 = algo2.centerPoint()
        #print("center:", x2)
        self.assertEqual(0, x2[0])
        x3 = algo3.centerPoint()
        #print("center:", x3)
        self.assertEqual(2, x3[0])
        x4 = algo4.centerPoint()
        #print("center:", x4)
        self.assertEqual(6, x4[0])
        x5 = algo5.centerPoint()
        #print("center:", x5)
        self.assertEqual(40, x5[0])


        algo10 =GraphAlgo()
        algo10.load_from_json("mixedgraph.json")
        algo10.plot_graph()
        algo10.save_to_json("mixedgraph_copy.json")


        # test plot

        # myalgo.plot_graph()
        # algo0.plot_graph()
        # algo1.plot_graph()
        # algo2.plot_graph()
        # algo3.plot_graph()
        # algo4.plot_graph()
        # algo5.plot_graph()
        # algo6.plot_graph()
        # algo7.plot_graph()
if __name__ == '__main__':
    unittest.main()
