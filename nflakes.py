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

def main():
    pg.init()
    pg.display.set_caption('n-flakes')
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR)

    pentaflake = Polygon(5, 200, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    running = True
    while running == True:
        for e in pg.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    running = False
            elif e.type == QUIT:
                running = False

        pentaflake.draw(screen)
        # pg.draw.polygon(screen, FLAKE_COLOR, [(152,215), (200,250), (247, 215), (229, 159), (170, 159)], 0)
        # draw_polygon(5, 50, (400, 400))

        pg.display.flip()

    pg.quit()

if __name__ == '__main__':
    main()

