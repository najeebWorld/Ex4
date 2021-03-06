import cmath
import string
from queue import PriorityQueue
from types import SimpleNamespace
from typing import cast
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
import pygame_widgets
from pygame_widgets.button import Button
import math
import time


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
        self.graph = g
        self.pokD = dict()
        self.agD = dict()
        self.client = Client()


    def start_game(self) -> None:

        """
        we will start the client and get the graph.
        we will find the center of teh graph and tell the server to start the agents on the center node.
        we will start the client
        while the client is running
            we will clear pokD
            we will run the gui
            we will reload the pokemons and agents from the server
            we will call the function attach_pokemon_gui
            we will loop through the agents and tell them to change there dest
            and we will print the client info
        """

        # default port
        PORT = 6666
        # server host (default localhost 127.0.0.1)
        HOST = '127.0.0.1'





        # client = Client()
        self.client.start_connection(HOST, PORT)
        self.create_graph()

        nc = self.centerPoint()
        c_id = nc[0]
        print(nc)
        print(c_id)
        center_text = "{\"id\":" + str(c_id) + "}"
        self.client.add_agent(center_text)
        self.client.add_agent(center_text)
        self.client.add_agent(center_text)
        self.client.add_agent(center_text)

        self.client.start()
        while self.client.is_running() == 'true':
            self.pokD.clear()
            self.run_Gui()
            self.add_agents()
            self.add_pokemons()

            self.attach_pokemon_agent()
            for agent in self.agD:
                a1 = self.agD[agent]

                src1 = a1.getSrc()
                dest1 = a1.getDest()
                id = a1.getId()
                t1=(src1,dest1)
                e = self.graph.edgeD.get(t1)
                if e==None:
                    print("not an edge")
                self.client.choose_next_edge('{"agent_id":' + str(id) + ', "next_node_id":' + str(dest1) + '}')
                ttl = self.client.time_to_end()
                print(ttl, self.client.get_info())





    def create_graph(self):

        """
        this function takes the json string and makes the objects Node and Edge that represent the graph
        and then adds the nodes and edges to the graph dictionaries of nodeD and edgeD
        """

        try:
            g = json.loads(self.client.get_graph())
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
        """
        this function takes the json string and makes the object Pokemon
        and then adds the Pokemon to the dictionary pokD
        """

        try:
            poke = json.loads(self.client.get_pokemons())
            outer = poke['Pokemons']
            for a in outer:
                inner = a['Pokemon']
                # print(inner)
                n = (inner['pos'])
                n: cast(string, n)  # cast it to string
                m = n.split(',')  # spliting to nodes
                pos = (float(m[0]), float(m[1]), float(m[2]))
                p1 = Pokemon(inner["type"], inner["value"], pos)
                self.pokD[pos] = p1
        except Exception as e:
            print(e)

    def add_agents(self):
        """
        this function takes the json string and makes the object Agent
        and then adds the Agent to the dictionary agD
        """
        try:
            ag = json.loads(self.client.get_agents())
            outer = ag['Agents']
            for a in outer:
                inner = a['Agent']
                n = (inner['pos'])
                n: cast(string, n)  # cast it to string
                m = n.split(',')  # spliting to nodes
                pos = (float(m[0]), float(m[1]), float(m[2]))
                id = inner['id']
                v = inner['value']
                s = inner['src']
                d = inner['dest']
                sp = inner['speed']
                a1 = Agent(id, v, s, d, sp, pos)
                self.agD[inner['id']] = a1
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

    def find_distance(self, t1, t2) -> float:
        # finds the distance between 2 points in a 2D surfice
        x = t1[0] - t2[0]
        y = t1[1] - t2[1]
        ans = math.sqrt(x * x + y * y)
        return ans


    def find_correct_edge(self, p: Pokemon) -> Edges:
        """
        finds the edge that the pokemon is on
        we will go through the edges in the graph till we find the correct one
        we will calculate the distance from the ends of the edge =d1
        we wll calculate the distance from the pokemon to each edge =d2+d3
        if d1+eps>d2+d3>d1-eps than this is the correct edge we just need to check if this the correct type
        we will do that by seeing if the dest-src had the same sign as the pokemon, if theye do they are a match
        other wise the edge from dest to src is the correct edge
        once we find the correct edge we will add the edge to the pokemon
        """

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
                    if (n2-n1 > 0 and p.getType() > 0) or (n2 - n1 < 0 and p.getType() < 0):
                        found = True
                        p.setEdge(e1)
                    else:
                        s = (n2, n1)
                        if self.graph.edgeD.get(s) != None:
                            found = True
                            p.setEdge(self.graph.edgeD.get(s))

    def attach_pokemon_agent(self):
        """"
        we will put all of the Agents into a list and do the same for the pokemons
        we use 2 loops to try to connect the agents to the pokemons as best as possible.
        the outer loop will go through the list of agents, the inner loop will gp through the list of pokemons
        we will use digasktra to find the shortset path from where the agent is to the src of the edge that the pokemon is on
        than we will take the distance between them and divide by the agents speed and than we will divide by the pokemons value,
        all this will give us a small number we will find the lowest number and the agent will be paired with that pokemon.
        this way the agent will go the pokemon that is relatively closest but that will also make the agents speed get higher faster.
        we will take the list from the dijsktra and by the size of it we will decide what the dest of the agent should be.
        than we will remove the pokemon from the list so that we don't have 2 agents going after the same pokemon

        """
        p = []
        a = []
        for aa in self.agD:
            a1 = self.agD.get(aa)
            # l = a1.getList()
            # if a1.getList() == None:  # isn't chasing a pokemon
            a.append(a1)

        for pp in self.pokD:
            p1 = self.pokD.get(pp)
            self.find_correct_edge(p1)
            p.append(p1)


        for j in range(0,len(a)):
            spot = -1
            short1 = float("inf")
            for i in range(0, len(p)):
                d = self.shortest_path(a[j].getSrc(), p[i].getEdge().getsrc())
                time = d[0]/a[j].getSpeed()
                time = time/ p[i].getValue()
                if time < short1:
                    short1 = time
                    spot = i
                    l = d[1]

            if spot >= 0 and spot < len(p):
                if len(l) == 0:
                    a[j].setDest(p[spot].getEdge().getdest())
                elif len(l) == 1 :
                    a[j].setDest(p[spot].getEdge().getdest())
                elif len(l) == 2:
                    a[j].setDest(l[1])
                else:
                    a[j].setDest(l[1])
                a[j].setPok(p[spot])
                del p[spot]











    def run_Gui(self):
        """"
        this function will run the GUI
        we will make simple objects for the nodes, edges,agents and pokemons
        we will find the min and max x and y in the graph to make  a scalar for all the objects
        we created in event for the end of the game that will stop it if you prees the x to close the window
        and there is a button to press to end the game.
        on the top of the of the GUI there is a counter for the mover and grade, and a count down for the time
        we will plot all the objects on the graph than we will show it.


        """
        # init pygame
        WIDTH, HEIGHT = 1080, 720

        screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        clock = pygame.time.Clock()
        pygame.font.init()

        pokemons = self.client.get_pokemons()
        pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))


        graph_json = self.client.get_graph()

        FONT = pygame.font.SysFont('Arial', 20, bold=True)
        # load the json string into SimpleNamespace Object

        graph = json.loads(graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

        for n in graph.Nodes:
            x, y, _ = n.pos.split(',')
            n.pos = SimpleNamespace(x=float(x), y=float(y))

        # get data proportions
        min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
        min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
        max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
        max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y

        radius = 15

        # button = Button(color=(0, 0, 0), rect=pygame.Rect((10, 10), (100, 50)))

        MOVE_FONT = pygame.font.SysFont('comicsans', 20)
        radius = 15
        """
        The code below should be improved significantly:
        The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
        """

        # while client.is_running() == 'true':
        pokemons = json.loads(self.client.get_pokemons(),
                              object_hook=lambda d: SimpleNamespace(**d)).Pokemons
        pokemons = [p.Pokemon for p in pokemons]
        for p in pokemons:
            x, y, _ = p.pos.split(',')
            p.pos = SimpleNamespace(x=self.my_scale(float(x), screen, min_x, max_x, min_y, max_y, x=True),
                                    y=self.my_scale(float(y), screen, min_x, max_x, min_y, max_y, y=True))
            agents = json.loads(self.client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
            agents = [agent.Agent for agent in agents]
        for a in agents:
            x, y, _ = a.pos.split(',')
            a.pos = SimpleNamespace(x=self.my_scale(float(x), screen, min_x, max_x, min_y, max_y, x=True),
                                    y=self.my_scale(float(y), screen, min_x, max_x, min_y, max_y, y=True))
        # check events


        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        stopButton = Button(
            screen, 0, 0, 100, 40, text="press to stop",
            fontSize=20, margin=5,
            inactiveColour=(255,0 ,0 ),
            pressedColour=(0,0, 255), radius=0,
            onClick=lambda: self.client.stop()
        )

        # refresh surface
        screen.fill(Color(0, 0, 0))


        # add moves, time and score to screen

        longString = self.client.get_info().split(",")
        timeToLive = self.client.time_to_end()
        score = longString[3].split(":")[1]
        moves = longString[2].split(":")[1]

        pygame.font.init()
        font = pygame.font.SysFont("Arial", 20)

        textTime = font.render("time left: " + str(timeToLive),True,(255,255,255))
        screen.blit(textTime, (120,0))

        textScore = font.render("score: " + str(score), True, (255, 255, 255))
        screen.blit(textScore, (400, 0))

        textMoves = font.render("move: " + str(moves), True, (255, 255, 255))
        screen.blit(textMoves, (600, 0))



        # draw nodes
        for n in graph.Nodes:
            x = self.my_scale(n.pos.x, screen, min_x, max_x, min_y, max_y, x=True)
            y = self.my_scale(n.pos.y, screen, min_x, max_x, min_y, max_y, y=True)

            # its just to get a nice antialiased circle
            gfxdraw.filled_circle(screen, int(x), int(y), radius, Color(64, 80, 174))
            gfxdraw.aacircle(screen, int(x), int(y), radius, Color(255, 255, 255))

            # draw the node id
            id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)

            # draw edges
        for e in graph.Edges:
            # find the edge nodes
            src = next(n for n in graph.Nodes if n.id == e.src)
            dest = next(n for n in graph.Nodes if n.id == e.dest)

            # scaled positions
            src_x = self.my_scale(src.pos.x, screen, min_x, max_x, min_y, max_y, x=True)
            src_y = self.my_scale(src.pos.y, screen, min_x, max_x, min_y, max_y, y=True)
            dest_x = self.my_scale(dest.pos.x, screen, min_x, max_x, min_y, max_y, x=True)
            dest_y = self.my_scale(dest.pos.y, screen, min_x, max_x, min_y, max_y, y=True)

            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y))



            # draw agents
        for agent in agents:
            pygame.draw.circle(screen, Color(122, 61, 23), (int(agent.pos.x), int(agent.pos.y)), 10)
        # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
        for p in pokemons:
            if (p.type == 1):
                pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)
            else:
                pygame.draw.circle(screen, Color(255, 0, 255), (int(p.pos.x), int(p.pos.y)), 10)

            # update screen changes
        pygame_widgets.update(events)
        display.update()
        display.flip()
        # refresh rate
        clock.tick(10)
        self.client.move()

        # game over:


    def scale(self,data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimentions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

        # decorate scale with the correct values

    def my_scale(self,data,screen, min_x, max_x, min_y, max_y, x=False, y=False):
        """
        gets a value and returns the changed value from the scaler
        """
        if x:
            return self.scale(data, 50, screen.get_width() - 50, min_x, max_x)
        if y:
            return self.scale(data, 50, screen.get_height() - 50, min_y, max_y)




