#!/bin/python

import pygame as pg
from pygame.locals import *

from Polygon import *
from Flake import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_COLOR = (52, 9, 38)

def main():
    vertices = int(input("Vertices: "))
    iterations = int(input("Iterations: "))

    pg.init()
    pg.display.set_caption('n-flakes')
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR)

    center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    nflake = Flake(vertices, 300, center)
    nflake.draw(iterations, screen)
    pg.display.flip()

    running = True
    while running == True:
        for e in pg.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    running = False
            elif e.type == QUIT:
                running = False

        # pg.display.flip()

    pg.quit()

if __name__ == '__main__':
    main()

