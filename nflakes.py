#!/bin/python

import math
import pygame as pg
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (100, 100, 100)

FLAKE_COLOR = (255, 150, 70)

class Polygon:
    def __init__(self, nv, rd, ct):
        self.num_vertices = nv
        self.radius = rd
        self.center = ct
        self.angle_base = 360/self.num_vertices

    def draw(self, win):
        coords = []
        for i in range(0, self.num_vertices):
            cx = round(self.center[0] + self.radius*math.cos(math.radians(self.angle_base*i + 90)))
            cy = round(self.center[1] - self.radius*math.sin(math.radians(self.angle_base*i + 90)))
            coords.append((cx, cy))

        pg.draw.polygon(win, FLAKE_COLOR, coords, 0)

class Flake:
    def __init__(self, nv, rd, ct):
        self.polygons = [Polygon(nv, rd, ct)]
        self.num_vertices = nv
        self.radius = rd
        self.center = ct
        gr = (1.0 + math.sqrt(5))/2.0
        self.constant = 1.0/(1.0 + gr)

    def draw(self, win, steps):
            self.polygons[0].draw(win)
            # rd = self.radius*self.constant
            for i in range(1, steps):
                for num in range(0, self.num_vertices**i):
                    polygon_base = self.polygons[0]
                    self.polygons.append(Polygon(self.num_vertices, polygon_base.radius*self.constant, (200, 400)))
                    self.polygons[0+1].draw(win)

def main():
    pg.init()
    pg.display.set_caption('n-flakes')
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR)

    flake = Flake(5, 200, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    running = True
    while running == True:
        for e in pg.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    running = False
            elif e.type == QUIT:
                running = False

        flake.draw(screen, 0)
        pg.display.flip()

    pg.quit()

if __name__ == '__main__':
    main()

