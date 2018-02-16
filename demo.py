#!/bin/python

import pygame as pg
from pygame.locals import *

from Polygon import *
from Flake import *

SCREEN_WIDTH = 760
SCREEN_HEIGHT = 530
SCREEN_COLOR = (31, 27, 27)

def main():
    # First ask user for input
    # vertices = int(input("Vertices: "))
    # iterations = int(input("Iterations: "))

    pg.init()
    pg.display.set_caption('n-flakes')
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR)

    # center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # nflake = Flake(vertices, 100, center)
    # nflake.colorful = True
    # nflake.outlined = True
    # nflake.draw(iterations, screen)

    its = 4
    rad = 100
    pos = (150, 150)
    col = False
    out = False

    flake3 = Flake(3, rad, (pos[0], pos[1]))
    flake3.colorful = col
    flake3.outlined = out
    flake3.draw(its+2, screen)

    flake4 = Flake(4, rad, (pos[0] + rad*2 + 30, pos[1]))
    flake4.colorful = col
    flake4.outlined = out
    flake4.draw(its+1, screen)

    flake5 = Flake(5, rad, (pos[0] + rad*4 + 60, pos[1]))
    flake5.colorful = col
    flake5.outlined = out
    flake5.draw(its, screen)

    flake6 = Flake(6, rad, (pos[0], pos[1] + rad*2 + 30))
    flake6.colorful = col
    flake6.outlined = out
    flake6.draw(its, screen)

    flake7 = Flake(8, rad, (pos[0] + rad*2 + 30, pos[1] + rad*2 + 30))
    flake7.colorful = col
    flake7.outlined = out
    flake7.draw(its, screen)

    flake12 = Flake(12, rad, (pos[0] + rad*4 + 60, pos[1] + rad*2 + 30))
    flake12.colorful = col
    flake12.outlined = out
    flake12.draw(its, screen)

    pg.display.flip()

    running = True
    while running == True:
        for e in pg.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    running = False
            elif e.type == QUIT:
                running = False

    pg.quit()

if __name__ == '__main__':
    main()

