import math
import pygame as pg
from pygame import gfxdraw

ROTATION = 90

class Polygon:
    DEFAULT_COLOR = (255, 195, 31)

    def __init__(self, nv, rd, ct):
        self.num_vertices = nv
        self.radius = rd
        self.center = ct
        self.angle_base = 360/self.num_vertices

        self.color = self.DEFAULT_COLOR
        self.fill = True

    def draw(self, win, inv, col=(0,0,0)):
        coords = []
        for i in range(0, self.num_vertices):
            cx = round(self.center[0] + self.radius*math.cos(math.radians(self.angle_base*i + ROTATION)))
            cy = round(self.center[1] - inv*self.radius*math.sin(math.radians(self.angle_base*i + ROTATION)))
            coords.append((cx, cy))

        pg.gfxdraw.aapolygon(win, coords, self.color)
        if self.fill == True:
            pg.gfxdraw.filled_polygon(win, coords, self.color)

