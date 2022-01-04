import unittest
import random

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_something(self):

        myalgo = GraphAlgo()
        myalgo.load_from_json("my graph1.json")



        # load and save
        myalgo.load_from_json("100new.json")
        myalgo.save_to_json("100copy.json")
        my_algo_new =GraphAlgo()
        my_algo_new.load_from_json("100copy.json")
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


        # shortest path
        lenn =len(myalgo.graph.nodeD)
        liist=random.sample(range(0, lenn), 2)
        print(liist)
        x= myalgo.shortest_path(liist[0], liist[1])
        print(x)


        # self.assertAlmostEqual(x[0],9)
        # self.assertEqual(x[1], [])


        # center
        ans=myalgo.centerPoint()
        print(ans)
        # self.assertEqual(ans[0],4)
        # self.assertAlmostEqual(ans[1],2)


        # tsp
        lenn =len(myalgo.graph.nodeD)
        liist=random.sample(range(0, lenn),20)
        print(liist)
        ans =myalgo.TSP([64,68,8])
        print("ans:" ,ans)



        # a1= len(ans[0]) >= len(liist)
        # self.assertTrue(a1)


        g = DiGraph()
        for x in range (0,50):
            g.add_node(x)
        for x in range (0,100):
            list1=random.sample(range(0, 50),30)
            g.add_edge(list1[0],list1[1],list1[2])

        newalgo=GraphAlgo(g)


        # plot
        newalgo.plot_graph()






if __name__ == '__main__':
    unittest.main()
