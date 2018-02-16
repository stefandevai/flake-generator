#!/bin/python

import math
import pygame as pg
from pygame.locals import *
from pygame import gfxdraw


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_COLOR = (52, 9, 38)

FLAKE_COLOR = (255, 195, 31)
CONSTANT = 1.0/(1.0 + ((1.0 + math.sqrt(5))/2.0))

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

            if inv == True:
                cx = self.center[0] + self.radius*math.cos(math.radians(self.angle_base*i + ROTATION))
                cy = self.center[1] + self.radius*math.sin(math.radians(self.angle_base*i + ROTATION))
            else:
                cx = self.center[0] + self.radius*math.cos(math.radians(self.angle_base*i + ROTATION))
                cy = self.center[1] - self.radius*math.sin(math.radians(self.angle_base*i + ROTATION))

            coords.append((cx, cy))

        pg.gfxdraw.aapolygon(win, coords, FLAKE_COLOR)
        pg.gfxdraw.filled_polygon(win, coords, FLAKE_COLOR)

class Flake:
    def __init__(self, nv, rd, ct):
        self.num_vertices = nv
        self.radius = rd
        self.center = ct
        self.angle_base = 360/self.num_vertices

    def __draw__(self, steps, rd, ct, inv):
        if steps <= 0:
            pass
        elif steps == 1:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.draw(self.screen_ref, inv)
        else:
            self.__draw__(steps-1, rd*CONSTANT, ct, not inv)
            for i in range(0, self.num_vertices):

                if inv == True:
                    cx = ct[0] + rd*math.cos(math.radians((self.angle_base)*i + ROTATION)) - rd*CONSTANT*math.cos(math.radians((self.angle_base)*i + ROTATION))
                    cy = ct[1] + rd*math.sin(math.radians((self.angle_base)*i + ROTATION)) - rd*CONSTANT*math.sin(math.radians((self.angle_base)*i + ROTATION))
                else:
                    cx = ct[0] + rd*math.cos(math.radians((self.angle_base)*i + ROTATION)) - rd*CONSTANT*math.cos(math.radians((self.angle_base)*i + ROTATION))
                    cy = ct[1] + rd*math.sin(math.radians((self.angle_base)*i - ROTATION)) + rd*CONSTANT*math.sin(math.radians((self.angle_base)*i + ROTATION))

                self.__draw__(steps-1, rd*CONSTANT, (cx, cy), inv)

    def draw(self, st, win):
        self.steps = st
        self.screen_ref = win
        self.__draw__(self.steps, self.radius, self.center, False)

def main():
    pg.init()
    pg.display.set_caption('n-flakes')
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR)

    center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    nflake = Flake(5, 300, center)
    nflake.draw(5, screen)

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

