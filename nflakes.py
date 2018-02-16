#!/bin/python

import math
import pygame as pg
from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_COLOR = (100, 100, 100)

FLAKE_COLOR = (255, 150, 70)
CONSTANT = 1.0/(1.0 + ((1.0 + math.sqrt(5))/2.0))

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
        self.num_vertices = nv
        self.radius = rd
        self.center = ct
        self.angle_base = 360/self.num_vertices

    def __draw__(self, steps, rd, ct):
        if steps <= 0:
            pass
        elif steps == 1:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.draw(self.screen_ref)
        else:
            for i in range(0, self.num_vertices):
                cx = round(ct[0] + rd*math.cos(math.radians((self.angle_base)*i + 90)) - rd*CONSTANT*math.cos(math.radians((self.angle_base)*i + 90)))
                cy = round(ct[1] - rd*math.sin(math.radians((self.angle_base)*i + 90)) + rd*CONSTANT*math.sin(math.radians((self.angle_base)*i + 90)))
                self.__draw__(steps-1, rd*CONSTANT, (cx, cy))

    def draw(self, st, win):
        self.steps = st
        self.screen_ref = win
        self.__draw__(self.steps, self.radius, self.center)

def main():
    pg.init()
    pg.display.set_caption('n-flakes')
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR)

    center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    nflake = Flake(5, 300, center)
    nflake.draw(4, screen)

    running = True
    while running == True:
        for e in pg.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    running = False
            elif e.type == QUIT:
                running = False

        pg.display.flip()

    pg.quit()

if __name__ == '__main__':
    main()

