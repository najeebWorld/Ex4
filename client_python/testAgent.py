import unittest

from client_python.Agent import Agent
from client_python.Pokemon import Pokemon


class MyTestCase(unittest.TestCase):


    def test_something(self):
        g = (1, 2, 3)
        a1 = Agent(0, 0, 1, 2, 3, g)

        self.assertEqual(a1.getId(),0)
        self.assertEquals(a1.getSrc(),1)
        self.assertEquals(a1.getDest(), 2)
        self.assertEquals(a1.getSpeed(), 3)
        self.assertEquals(a1.getPos(), g)

        a1.setSrc(2)
        a1.setDest(3)

        g=(2,3,4)
        a1.setPos(g)
        p =Pokemon(1,3,g)
        a1.setPok(p)
        self.assertEquals(a1.getSrc(), 2)
        self.assertEquals(a1.getDest(), 3)
        self.assertEquals(a1.getPos(), g)
        self.assertEquals(a1.getPok(), p)



if __name__ == '__main__':
    unittest.main()
