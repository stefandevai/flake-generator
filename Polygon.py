import math
import pygame as pg
from pygame import gfxdraw

FLAKE_COLOR = (255, 195, 31)
ROTATION = 90

class Polygon:
    def __init__(self, nv, rd, ct):
        self.num_vertices = nv
        self.radius = rd
        self.center = ct
        self.angle_base = 360/self.num_vertices

    def draw(self, win, inv):
        coords = []
        for i in range(0, self.num_vertices):
            cx = round(self.center[0] + self.radius*math.cos(math.radians(self.angle_base*i + ROTATION)))
            cy = round(self.center[1] - inv*self.radius*math.sin(math.radians(self.angle_base*i + ROTATION)))
            coords.append((cx, cy))

        pg.gfxdraw.aapolygon(win, coords, FLAKE_COLOR)
        pg.gfxdraw.filled_polygon(win, coords, FLAKE_COLOR)
