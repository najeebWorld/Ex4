import cmath
import string
from queue import PriorityQueue
from typing import cast
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
import math

from client_python.DiGraph import DiGraph
from client_python.GraphInterface import GraphInterface
from client_python import client
from client_python.Agent import Agent
from client_python.Pokemon import Pokemon
from client_python.Node import Node
from client_python.Edges import Edges



class playgame:


    def __init__(self, g: DiGraph = None):
        if g == None:
            g = DiGraph()
        print("first")
        self.graph = g
        self.pokD = dict()
        self.agD = dict()
        self.client = Client()


    def start_game(self) -> None :
        # default port
        PORT = 6666
        # server host (default localhost 127.0.0.1)
        HOST = '127.0.0.1'


        #client = Client()
        self.client.start_connection(HOST, PORT)
        self.create_graph()
        self.client.add_agent("{\"id\":0}")
        # client.add_agent("{\"id\":1}")
        # client.add_agent("{\"id\":2}")
        # client.add_agent("{\"id\":3}")

        self.client.start()
        # self.create_graph()
        while self.client.is_running() == 'true':
        #if  self.client.is_running() == 'true':
            self.add_agents()
            self.add_pokemons()
            # for p in self.pokD:
            self.attach_pokemon_agent()
            print("attached all")
            for agent in self.agD:
                a1 = self.agD[agent]
                src1 = a1.getSrc()
                l = a1.getList()
                l0=l[0]
                if a1.getSrc() == l0:
                    id = a1.getId()
                    d=l[1]
                    self.client.choose_next_edge('{"agent_id":' + str(id) + ', "next_node_id":' + str(d) + '}')
                    ttl = self.client.time_to_end()
                    print(ttl, self.client.get_info())
            self.client.move()


    def create_graph(self):
        try:
            g=json.loads(self.client.get_graph())
            n = g["Nodes"]
            for keys in n:
                n = (keys["pos"])
                n: cast(string, n)  # cast it to string
                m = n.split(',')  # spliting to nodes
                pos = (float(m[0]), float(m[1]), float(m[2]))
                self.graph.add_node(keys["id"], pos)
            for j in g["Edges"]:
                self.graph.add_edge(j["src"], j["dest"], j["w"])

        except Exception as e:
            print(e)


    def add_pokemons(self):
        try:
            poke = json.loads(self.client.get_pokemons())
            outer = poke['Pokemons']
            for a in outer:
                inner = a['Pokemon']
                print(inner)
                n = (inner['pos'])
                n: cast(string, n)  # cast it to string
                m = n.split(',')  # spliting to nodes
                pos = (float(m[0]), float(m[1]), float(m[2]))
                p1 = Pokemon(inner["type"], inner["value"], pos)
                self.pokD[pos] = p1
                print("added po")

            print(a)
        except Exception as e:
            print(e)

    def add_agents(self):
        try:
            ag =json.loads(self.client.get_agents())
            outer =ag['Agents']
            for a in outer:
                inner =a['Agent']
                print(inner)
                n = (inner['pos'])
                n: cast(string, n)  # cast it to string
                m = n.split(',')  # spliting to nodes
                pos = (float(m[0]), float(m[1]), float(m[2]))
                id=inner['id']
                v=inner['value']
                s=inner['src']
                d=inner['dest']
                sp=inner['speed']
                a1 = Agent(id,v,s,d,sp,pos)
                self.agD[inner['id']] = a1
                print("added agent to d")
        except Exception as e:
            print(e)



    def shortest_path(self, id1: int, id2: int) -> (float, list):

        """
             Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
             we will check if id1 and id2 are in the graph.
             if they arent in the graph we will return (inf,[])
             we will checkif they are the same, if they are we will return (0,[id1])
             if they are in the graph we will run dijsktra
             dijsktra will return a tuple with 2 dictionarys
             we will accesses the dictionary and get the values that we need.
             we will put them in a tuple and return them
             the run time is O(|v|^2) v=vertexes
             @param id1: The start node id
             @param id2: The end node id
             @return: The distance of the path, a list of the nodes ids that the path goes through
             """

        n = self.graph.nodeD.keys()

        if id1 not in n:
            return (float("inf"), [])
        if id2 not in n:
            return (float("inf"), [])
        if id1 == id2:
            return (0, [id1])
        x = self.dijasktra(id1)
        l = (id1, id2)
        if x[0].get(l) == float("inf"):
            ans = (x[0].get(l), [])
            return ans
        ans = (x[0].get(l), x[1].get(l))
        return ans


    def dijasktra(self, src: int) -> tuple:

        """"
        dijasktra algorithm
        an algorithm to find the shortest distance and path from 1 node to all other nodes in the graph
        we implemented this algorithm with a priority queue
        to reed more about this algorithm https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        the run time of this function is O(|v|^2+|e|)= O(|v|^2) v=vertexes, e=edges .
        """

        q = PriorityQueue(maxsize=10000000000)
        mapd = dict()
        mapl = dict()
        l = []
        n = self.graph.get_all_v()
        for key in n:
            n1 = n[key]
            l2 = []
            l2.append(src)
            l2.append(n1.getId())
            l1 = (src, n1.getId())
            mapd[l1] = float("inf")
            mapl[l1] = l2
            l.append(key)

        l1 = (src, src)
        mapd[l1] = 0.0

        q.put((0.0, src))
        empt = q.empty()
        while (empt == False):
            peek1 = q.queue[0]
            peek = peek1[1]
            for k in self.graph.nodeD.get(peek).out1:
                e = self.graph.nodeD.get(peek).out1[k]
                if k in l:
                    l2 = (src, k)
                    if mapd.get(l2) == float("inf"):
                        l3 = (src, peek)
                        d = mapd[l3] + e
                        mapd[l2] = d
                        q.put((d, k))
                        l5 = []
                        l6 = mapl[l3]
                        for i in range(len(l6)):
                            if l6[i] not in l5:
                                l5.append(l6[i])
                        l5.append(k)
                        mapl[l2] = l5
                    else:
                        l3 = (src, peek)
                        if mapd[l2] > mapd[l3] + e:
                            d = mapd[l3] + e
                            mapd[l2] = d
                            q.put((d, k))
                            l5 = []
                            l6 = mapl[l3]
                            for i in range(len(l6)):
                                if l6[i] not in l5:
                                    l5.append(l6[i])
                            l5.append(k)
                            mapl[l2] = l5
            y = q.get(0)
            empt = q.empty()
            n1 = self.graph.nodeD.get(peek)
            if peek in l:
                l.remove(peek)

        return (mapd, mapl)





    def find_distance(self, t1, t2) -> float:
        x=t1[0] - t2[0]
        y=t1[1] - t2[1]
        ans=math.sqrt(x*x+y*y)
        # (cmath.sqrt((t1[0] - t2[0]) * (t1[0] - t2[0]) + (t1[1] - t2[1]) * (t1[1] - t2[1])))
        return ans

    def find_closest_node(self, a: Agent) -> Node:
        sd = float("inf")
        close = None;
        for n in self.graph.nodeD:
            d1 = self.find_distance(self.graph.nodeD.grtpos(), a.getLoction())
            if d1 < sd:
                sd = d1
                close = self.graph.nodeD.get(n)
        a.setClosest(close)

    def find_correct_edge(self, p: Pokemon) -> Edges:
        found = False
        eps = 0.00001
        for e in self.graph.edgeD:
            if found == False:
                e1 = self.graph.edgeD.get(e)
                n1 = e1.getsrc()
                n2 = e1.getdest()
                t1 = self.graph.nodeD.get(n1).getPos()
                t2 = self.graph.nodeD.get(n2).getPos()
                t3 = p.getPos()
                d1 = self.find_distance(t1, t2)
                d2 = self.find_distance(t1, t3)
                d3 = self.find_distance(t3, t2)
                if (d2 + d3 < d1 + eps) and (d2 + d3 > d1 - eps):
                    if (n1 - n2 > 0 and p.getType() > 0) or (n1 - n2 < 0 and p.getType() < 0):
                        found = True
                        p.setEdge(e1)
                    else:
                        s = (n2, n1)
                        if self.graph.edgeD.get(s) != None:
                            found = True
                            p.setEdge(self.graph.edgeD.get(s))

    def attach_pokemon_agent(self):
        p = []
        a = []
        for aa in self.agD:
            a1 = self.agD.get(aa);
            l=a1.getList()
            if a1.getList() == None:  # isn't chasing a pokemon
                a.append(a1)

        for pp in self.pokD:
            p1 = self.pokD.get(pp)
            self.find_correct_edge(p1)
            p.append(p1)

        short1 = float("inf")
        l = []
        for i in range(0, len(p)):
            spot = -1
            for j in range(0, len(a)):
                # ghj=a[j].getSrc()
                # b=p[i]
                # bn=p[i].getEdge()
                # bnm=p[i].getEdge().getsrc()
                d = self.shortest_path(a[j].getSrc(), p[i].getEdge().getsrc())
                if d[0] < short1:
                    short1 = d[0]
                    spot = j
                    l = d[1]
            if spot >= 0 and spot < len(a):
                l.append(p[spot].getEdge().getdest())
                a[spot].setList(l)
                del a[spot]

    # if __name__ == '__main__':
    #     start_game()