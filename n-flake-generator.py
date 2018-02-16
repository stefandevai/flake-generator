#!/bin/python

import pygame as pg
from pygame.locals import *

from Flake import *

def generate_flakes(screen, col = False, out = False):
    its = 4
    rad = 100
    pos = (150, 150)
    delay = 0

    flake3 = Flake(3, rad, (pos[0], pos[1]))
    flake3.colorful = col
    flake3.outlined = out
    flake3.draw(its, screen)
    pg.display.flip()
    pg.time.delay(delay)

    flake4 = Flake(4, rad, (pos[0] + rad*2 + 30, pos[1]))
    flake4.colorful = col
    flake4.outlined = out
    flake4.draw(its, screen)
    pg.display.flip()
    pg.time.delay(delay)

    flake5 = Flake(5, rad, (pos[0] + rad*4 + 60, pos[1]))
    flake5.colorful = col
    flake5.outlined = out
    flake5.draw(its, screen)
    pg.display.flip()
    pg.time.delay(delay)

    flake6 = Flake(6, rad, (pos[0], pos[1] + rad*2 + 30))
    flake6.colorful = col
    flake6.outlined = out
    flake6.draw(its, screen)
    pg.display.flip()
    pg.time.delay(delay)

    flake7 = Flake(8, rad, (pos[0] + rad*2 + 30, pos[1] + rad*2 + 30))
    flake7.colorful = col
    flake7.outlined = out
    flake7.draw(its, screen)
    pg.display.flip()
    pg.time.delay(delay)

    flake12 = Flake(12, rad, (pos[0] + rad*4 + 60, pos[1] + rad*2 + 30))
    flake12.colorful = col
    flake12.outlined = out
    flake12.draw(its, screen)

def main():
    header_string = '\n||||||||||||||||||||||||||||||||||||||||||||||||||\n||||    N - F L A K E    G E N E R A T O R    ||||\n||||||||||||||||||||||||||||||||||||||||||||||||||\n'
    fractal_string = '\n               /\\\n              /\/\\\n             /\  /\\\n            /\/\/\/\\\n           /\      /\\\n          /\/\    /\/\\\n         /\  /\  /\  /\\\n        /\/\/\/\/\/\/\/\\\n       /\              /\\\n      /\/\            /\/\\\n     /\  /\          /\  /\\\n    /\/\/\/\        /\/\/\/\\\n   /\      /\      /\      /\\\n  /\/\    /\/\    /\/\    /\/\\\n /\  /\  /\  /\  /\  /\  /\  /\\\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\\n'
    welcome_string = ("\nWelcome to n-flake generator developed by Stefan Devai\n"
                      "Visit the repo in: https://github.com/stefandevai/n-flakes\n")
    menu_string = ("\nOPTIONS:\n1 - Input vertices and iterations\n"
                   "2 - Run demo\n"
                   "3 - Exit\n")

    print(header_string, fractal_string, welcome_string, menu_string)

    option = -1
    running = False
    while running == False:
        option = int(input('Select option: '))
        if option == 1:
            running = True
        elif option == 2:
            running = True
        elif option == 3:
            running = True
        else:
            print('\nERROR: Invalid option')
            print(menu_string)

    if option == 3:
        pass
    else:
        colorful = False
        outline = False

        running = False
        while running == False:
            answer = input('Colorful mode? (yes/no) ')

            if answer == 'yes' or answer == 'y' or answer == 'Y':
                colorful = True
                running = True
            elif answer == 'no' or answer == 'n' or answer == 'N':
                running = True
            else:
                print('Please answer with \'yes\' or \'no\'')

        running = False
        while running == False:
            answer = input('Outline mode? (yes/no) ')

            if answer == 'yes' or answer == 'y' or answer == 'Y':
                outline = True
                running = True
            elif answer == 'no' or answer == 'n' or answer == 'N':
                running = True
            else:
                print('Please answer with \'yes\' or \'no\'')

        # SCREEN_COLOR = (31, 27, 27)
        SCREEN_COLOR = (39, 42, 49)

        if option == 1:
            SCREEN_WIDTH = 800
            SCREEN_HEIGHT = 600
            vertices = int(input("Vertices: "))
            iterations = int(input("Iterations: "))
        else:
            SCREEN_WIDTH = 760
            SCREEN_HEIGHT = 530

        pg.init()
        pg.display.set_caption('n-flakes')
        screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(SCREEN_COLOR)

        if option == 1:
            center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            nflake = Flake(vertices, 250, center)
            nflake.colorful = colorful
            nflake.outlined = outline
            nflake.draw(iterations, screen)
        else:
            generate_flakes(screen, colorful, outline)

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

