import unittest

from client_python.DiGraph import DiGraph
from client_python.play_game import playgame


class MyTestCase(unittest.TestCase):








    # game =playgame()
    # game.start_game()

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
        game1=playgame(g)

        a1 =game1.shortest_path(0, 1)
        b1 = (1.35, [0, 1])
        self.assertEqual(a1, b1)

        myx = game1.centerPoint()
        self.assertEqual(0, myx[0])

        t1=(0,0,0)
        t2=(0,2,0)
        self.assertEqual(game1.find_distance(t1,t2),2)


if __name__ == '__main__':
    main = unittest.main()
