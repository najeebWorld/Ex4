import cmath
import json
import string
from typing import List, cast

from queue import PriorityQueue
import random
from random import uniform
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from DiGraph import DiGraph
# from src import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
from client_python import Node, Pokemon, Edges
from client_python.Agent import Agent
from client_python.GraphInterface import GraphInterface
from client_python import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        if g == None:
            g = DiGraph()
        self.graph = g
        self.pokD = dict()
        self.agD = dict()

    def get_graph(self) -> GraphInterface:
        """
        returns the graph
        the run time is O(1)
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
            Loads a graph from a json file.
            we will check if the nodes in the json have a pos,
            if they do we will create  the nodes with the id and pos,
            if they don't have a pos we will make a pos with random number between 0 and 1.
            then we will add the edges
            the run time is O(|v|+|e|) v=vertexes, e=edges .
            @param file_name: The path to the json file
            @returns True if the loading was successful, False o.w.
        """

        try:
            f = open(file_name)
            data = json.load(f)
            n = data["Nodes"]
            pos1 = False
            for keys in n:
                if "pos" in keys:
                    n = (keys["pos"])
                    n: cast(string, n)  # cast it to string
                    m = n.split(',')  # spliting to nodes
                    pos = (float(m[0]), float(m[1]), float(m[2]))
                    self.graph.add_node(keys["id"], pos)
                else:
                    self.graph.add_node(keys["id"])
            for j in data["Edges"]:
                self.graph.add_edge(j["src"], j["dest"], j["w"])
            return True
        except Exception as e:
            print(e)
            return False

        # raise NotImplementedError

    def save_to_json(self, file_name: str) -> bool:

        """
        Saves the graph in JSON format to a file
        the run time is O(|v|+|e|) v=vertexes, e=edges .
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """

        dict = {"Nodes": [], "Edges": []}
        n = self.graph.nodeD
        for no in n:
            id = n[no].getId()
            if n[no].getPos() != None:
                x = str(n[no].getX())
                c1 = str(",")
                y = str(n[no].getY())
                z = str(n[no].getZ())
                pos = x + c1 + y + c1 + z
                dict['Nodes'].append({'id': id, 'pos': pos})
            else:
                dict['Nodes'].append({'id': id})
        e = self.graph.edgeD
        for ed in e:
            dict['Edges'].append({'src': e[ed].getsrc(), 'dest': e[ed].getdest(), 'w': e[ed].getweight()})

        try:
            with open(file_name, 'w') as f:
                json.dump(dict, indent=2, fp=f)
            return True
        except Exception as e:
            print(e)
            return False

        # raise NotImplementedError

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

        # raise NotImplementedError

    def TSP(self, node_lst: List[int]) -> (List[int], float):

        """
           Finds the shortest path that visits all the nodes in the list
           we will make a copy of the list.
           we will create 2 dictionaries, 1 for the length the other for the list.
           we will run dijesktra on all the nodes in the list.
           each time we run dijesktra we will get a tuple with 2 dictionaries
           we will enter these dictionaries into the dictionaries we created.
           we will create a variable small and liist.
           while the length of the copied list is bigger then 0
           we will find the shortest distance between the last node in the liist and the nodes that we havent visted yet.
           if liist is empty we will check from te first node in the copied list to all othres.
           as we find the shortest path we will update the liist to have the full path and update small to be the length of the path.
           and we will make sure to remove from the copied list all the nodes we have beeen to.
           we will then return the list and the length of the list
           the run time is O(k^2*|v|^2) v=vertexes k=size of the list of nodes

          :param node_lst: A list of nodes id's
          :return: A list of the nodes id's in the path, and the overall distance



        """
        if len(node_lst) == 0:
            return (float("inf"), [])

        n_list = []
        for i in node_lst:
            n_list.append(i)

        n = self.graph.nodeD.keys()
        for x in n_list:
            if x not in n:
                return (float("inf"), [])

        if len(node_lst) == 1:
            return (0, node_lst)

        dubD = dict()
        listD = dict()
        for n in node_lst:
            pair = self.dijasktra(n)
            d = pair[0]
            dubD[n] = d
            l = pair[1]
            listD[n] = l

        liist = []
        # small = float("inf")
        small = 0

        first = n_list[0]
        n_list.remove(first)
        while len(n_list) > 0:
            smaller = float("inf")
            for x in range(0, len(n_list)):

                tup1 = (first, n_list[x])
                if dubD[first][tup1] < smaller:
                    smaller = dubD[first][tup1]
                    tup2 = tup1

            small = small + smaller
            addlist = listD[first][tup2]
            for x in addlist:
                if len(liist) == 0:
                    liist.append(x)
                else:
                    if liist[len(liist) - 1] != x:
                        liist.append(x)

            for a in liist:
                if a in n_list:
                    n_list.remove(a)

            first = liist[len(liist) - 1]

        return (liist, small)

    def centerPoint(self) -> (int, float):

        """
            Finds the node that has the shortest distance to it's farthest node.
            we will run dijesktra for each node.
            we will find the longest path in each dictionary and add it to a new dictionary.
            that holds the node and the distance.
            we will go through the dictionary and find the the smallest value.
            and return the key and value
            the run time is O(|v|^3) v=vertexes
           :return: The nodes id, min-maximum distance
       """

        x = self.isConnected()
        if x == False:
            ans = (None, float("inf"))
            return ans
        short_long = dict()

        for key in self.graph.nodeD:
            big = 0.0
            a = self.graph.nodeD[key].getId()
            pair = self.dijasktra(a)
            for x in pair[0]:
                d = pair[0].get(x)
                # print(d)
                if d > big:
                    big = d

            short_long[a] = big
        small = (None, float("inf"))
        for key in short_long:
            if short_long[key] < small[1]:
                small = (key, short_long[key])

        return small

    def plot_graph(self) -> None:
        """
        Plots the graph.
        we will make a list of th x,y coordinates and the id of the nodes.
        we will make a list of the x,y coordinates if both edges of the edges.
        if the graph has more then 1000 nodes or more than 2000 edges we will print the nodes and the id,
        and then print the edges.
        else we will print the nodes the edges and then the keys
        the run time is O(|v|+|e|) v=vertexes, e=edges

        @return: None
        """
        n = self.graph.nodeD
        e = self.graph.edgeD

        listx = []
        listy = []
        listid = []
        a = 0
        b = 1
        for cor in n:

            if n[cor].getPos() == None:
                list1 = [random.uniform(a, b) for x in range(3)]
                p = (list1[0], list1[1], list1[2])
                n[cor].setPos(p)
                listx.append(list1[0])
                listy.append(list1[1])
                listid.append(n[cor].getId())
            else:
                listx.append(n[cor].getX())
                if n[cor].getX() > b:
                    b = n[cor].getX()
                    if n[cor].getX() < a:
                        a = n[cor].getX()
                listy.append(n[cor].getY())
                if n[cor].getY() < a:
                    a = n[cor].getY()
                listid.append(n[cor].getId())
        # print(listx ,listy , listid)
        listx1 = []
        listx2 = []
        listy1 = []
        listy2 = []
        for cor in e:
            src = e[cor].getsrc()
            dest = e[cor].getdest()
            listx1.append(n[src].getX())
            listy1.append(n[src].getY())
            listx2.append(n[dest].getX())
            listy2.append(n[dest].getY())

        lennode = len(listx)
        lenedge = len(listx1)

        figure(figsize=(10, 7))
        plt.rcParams['axes.facecolor'] = 'gray'

        if (lennode > 1000 or lenedge > 2000):
            for i in range(0, lennode):
                plt.plot(listx[i], listy[i], markersize=10, marker="o", color="blue")
                plt.text(listx[i], listy[i], listid[i], color='red', fontsize=16, fontstyle="normal")
            for i in range(0, lenedge):
                plt.annotate("", xy=(listx1[i], listy1[i]), xytext=(listx2[i], listy2[i]),
                             arrowprops=dict(arrowstyle="<-", edgecolor="yellow", lw=1.5))
        else:
            for i in range(0, lennode):
                plt.plot(listx[i], listy[i], markersize=10, marker="o", color="blue")
            for i in range(0, lenedge):
                plt.annotate("", xy=(listx1[i], listy1[i]), xytext=(listx2[i], listy2[i]),
                             arrowprops=dict(arrowstyle="<-", edgecolor="yellow", lw=1.5))
            for i in range(0, lennode):
                plt.text(listx[i], listy[i], listid[i], color='red', fontsize=16, fontstyle="normal")

        plt.show()

        # raise NotImplementedError

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

    def isConnected(self) -> bool:

        """
        we will check if you can get from every Vertex to Every Vertex
        if the graph has no nodes by default it is connected
        if the graph has fewer edges than vertexes it can not be connected
        if neither of the if give us an answer
        we will start by marking each vertex as not seen
        we will create a list and add the first vertex to it
        while the list isnt empty
        we will take out the first value from the list
        we will mark the vertex as seen and iterate through the vertexes edges and add the edges dest to the list
        after we will iterate through the Vertexes and make sure that all the Vertexes have been seen
        if we find a vertex that hasn't been seen the graph isn't connected
        if all the vertexes have been seen we will flip the graph
        and repeat on the flipped graph

        the running time is O(|v|+|e|) v=vertex e=edge
        """

        if self.graph.v_size() == 0:
            return True
        if self.graph.e_size() < self.graph.v_size():
            return False
        for key in self.graph.nodeD:
            self.graph.nodeD[key].settag(0)

        l = []
        n1 = list(self.graph.nodeD.values())[0]  # get first value
        l.append(n1)
        while len(l) > 0:
            n2 = l[0]
            l.remove(n2)
            n2.settag(1)
            for k in self.graph.nodeD.get(n2.getId()).out1:
                e = self.graph.nodeD.get(n2.getId()).out1[k]  # other side of edge int
                n3 = self.graph.nodeD.get(k)
                if n3.gettag() != 1:
                    if n3 not in l:
                        l.append(n3)

        for key in self.graph.nodeD:
            if self.graph.nodeD[key].gettag() == 0:
                return False

        g = self.get_graph()
        graphflip = self.flipGraph(g)

        for key in graphflip.nodeD:
            graphflip.nodeD[key].settag(0)
        l = []
        n1 = list(graphflip.nodeD.values())[0]  # get first value
        l.append(n1)
        while len(l) > 0:
            n2 = l[0]
            l.remove(n2)
            n2.settag(1)
            for k in graphflip.nodeD.get(n2.getId()).out1:
                e = graphflip.nodeD.get(n2.getId()).out1[k]  # other side of edge int
                n3 = graphflip.nodeD.get(k)
                if n3.gettag() != 1:
                    if n3 not in l:
                        l.append(n3)
        for key in graphflip.nodeD:
            if graphflip.nodeD[key].gettag() == 0:
                return False

        return True

    def flipGraph(self, graph: DiGraph) -> DiGraph:

        """
        we will start by creating a new graph
        we will copy the vertexes from the given graph to our new graph
        we will copy the edges from the given graph to our new graph
        BUT we will switch the src and dest
        run time O(|v|+|e|) v=vertexes, e=edges
        """

        gr = DiGraph()
        for k in graph.nodeD:
            id = graph.nodeD[k].getId()
            gr.add_node(id)
        for k in graph.edgeD:
            e = graph.edgeD[k]
            s = e.getsrc()
            d = e.getdest()
            w = e.getweight()
            gr.add_edge(d, s, w)
        return gr

    def find_distance(self, t1: tuple, t2: tuple) -> float:
        return (cmath.sqrt((t1[0] - t2[0]) * (t1[0] - t2[0]) + (t1[1] - t2[1]) * (t1[1] - t2[1])))

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
        eps = 0.0001
        for e in self.graph.edgeD:
            if found == False:
                e1 = self.graph.edgeD.get(e)
                n1 = e1.src
                n2 = e1.dest
                d1 = self.distance(n1.pos, n2.pos)
                d2 = self.distancen(n1.pos, p.pos)
                d3 = self.distance(p.pos, n2.pos)
                if (d2 + d3 < d1 + eps) and (d2 + d3 > d1 - eps):
                    if (n1.id - n2.id > 0 and p.type > 0) or (n1.id - n2.id < 0 and p.type < 0):
                        found = True
                        p.setEdge(e1)
                    else:
                        s = (n2.id, n1.id)
                        if self.graph.edgeD.get(s) != None:
                            found = True
                            p.setEdge(self.graph.edgeD.get(s))

    def attach_pokemon_agent(self):
        p = []
        a = []
        for aa in self.agD:
            a1 = self.agD.get(aa);
            if a1.closest == None:
                self.find_closest_node(a1)
            if a1.getList == None:  # isn't chasing a pokemon
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
                d = self.shortest_path(a[j].closest.id, p[i].edge.src)
                if d[0] < short1:
                    short1 = d[0]
                    spot = j
                    l = d[1]
            if spot >= 0 and spot < len(a):
                l.append(p[spot].edge.dest)
                a[spot].setList(l)
                a.remove(spot)



