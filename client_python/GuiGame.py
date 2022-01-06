from types import SimpleNamespace

from pygame.examples.headless_no_windows_needed import screen

from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *

from client_python.Pokemon import Pokemon
from client_python.student_code import scale, min_x, max_x, max_y, min_y, graph, radius, FONT, my_scale, agent

WIDTH, HEIGHT = 1080, 720

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (250, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
radius = 15



class GuiGame:
    def __init__(self):
        self.screen = display.set_mode((WIDTH,HEIGHT),depth=32,flags=RESIZABLE)

    def scale(data, min_screen, max_screen, min_data, max_data):

        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(data, x=False, y=False):
        if x:
            return scale(data, 50, screen.get_width() - 50, min_x, max_x)
        if y:
            return scale(data, 50, screen.get_height() - 50, min_y, max_y)

    def drow_node(self):
        for n in graph.Nodes:
            x = my_scale(n.pos.x, x=True)
            y = my_scale(n.pos.y, y=True)

            # its just to get a nice antialiased circle
            gfxdraw.filled_circle(screen, int(x), int(y),
                                  radius, Color(64, 80, 174))
            gfxdraw.aacircle(screen, int(x), int(y),
                             radius, Color(255, 255, 255))

            # draw the node id
            id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)

    def draw_edges(self):
        for e in graph.Edges:
            # find the edge nodes
            src = next(n for n in graph.Nodes if n.id == e.src)
            dest = next(n for n in graph.Nodes if n.id == e.dest)

            # scaled positions
            src_x = my_scale(src.pos.x, x=True)
            src_y = my_scale(src.pos.y, y=True)
            dest_x = my_scale(dest.pos.x, x=True)
            dest_y = my_scale(dest.pos.y, y=True)

            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126),
                             (src_x, src_y), (dest_x, dest_y))

    def draw_agent(self):
        pygame.draw.circle(screen, Color(122, 61, 23),
                           (int(agent.pos.x), int(agent.pos.y)), 10)

   # def draw_pokemon(self):



