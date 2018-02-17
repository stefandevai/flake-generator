#!/bin/python

import pygame as pg
from pygame.locals import *

from Flake import *

class FlakeGenerator:
    def __init__(self):
        self.SCREEN_COLOR = (39, 42, 49)

    def __ask(self, question, default = False):
        response = False
        answered = False

        while answered == False:
            answer = input(question + ' (yes/no) ')
            if answer == '':
                response = default
                answered = True
            else:
                if answer == 'yes' or answer == 'y' or answer == 'Y':
                    response = True
                    answered = True
                elif answer == 'no' or answer == 'n' or answer == 'N':
                    answered = True
                else:
                    print('Please answer with \'yes\' or \'no\'')
        return response

    def input_generation(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.vertices = int(input("Vertices: "))
        self.iterations = int(input("Iterations: "))
        self.colorful = self.__ask('Colorful mode?')
        self.outlined = self.__ask('Outlined mode?')

        pg.init()
        pg.display.set_caption('n-flakes')
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill(self.SCREEN_COLOR)

        self.center = (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2)
        self.nflake = Flake(self.vertices, 250, self.center)
        self.nflake.colorful = self.colorful
        self.nflake.outlined = self.outlined
        self.nflake.draw(self.iterations, self.screen)
        pg.display.flip()

    def demo_generation(self):
        self.colorful = self.__ask('Colorful mode?')
        self.outlined = self.__ask('Outlined mode?')
        self.SCREEN_WIDTH = 760
        self.SCREEN_HEIGHT = 530

        pg.init()
        pg.display.set_caption('n-flakes')
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill(self.SCREEN_COLOR)

        its = 4
        rad = 100
        pos = (150, 150)
        delay = 0

        flake3 = Flake(3, rad, (pos[0], pos[1]))
        flake3.colorful = self.colorful
        flake3.outlined = self.outlined
        flake3.draw(its, self.screen)
        pg.display.flip()
        pg.time.delay(delay)

        flake4 = Flake(4, rad, (pos[0] + rad*2 + 30, pos[1]))
        flake4.colorful = self.colorful
        flake4.outlined = self.outlined
        flake4.draw(its, self.screen)
        pg.display.flip()
        pg.time.delay(delay)

        flake5 = Flake(5, rad, (pos[0] + rad*4 + 60, pos[1]))
        flake5.colorful = self.colorful
        flake5.outlined = self.outlined
        flake5.draw(its, self.screen)
        pg.display.flip()
        pg.time.delay(delay)

        flake6 = Flake(6, rad, (pos[0], pos[1] + rad*2 + 30))
        flake6.colorful = self.colorful
        flake6.outlined = self.outlined
        flake6.draw(its, self.screen)
        pg.display.flip()
        pg.time.delay(delay)

        flake7 = Flake(8, rad, (pos[0] + rad*2 + 30, pos[1] + rad*2 + 30))
        flake7.colorful = self.colorful
        flake7.outlined = self.outlined
        flake7.draw(its, self.screen)
        pg.display.flip()
        pg.time.delay(delay)

        flake12 = Flake(12, rad, (pos[0] + rad*4 + 60, pos[1] + rad*2 + 30))
        flake12.colorful = self.colorful
        flake12.outlined = self.outlined
        flake12.draw(its, self.screen)
        pg.display.flip()


    def interactive_generation(self):
        header_string = '\n||||||||||||||||||||||||||||||||||||||||||||||||||\n||||    N - F L A K E    G E N E R A T O R    ||||\n||||||||||||||||||||||||||||||||||||||||||||||||||\n'
        sierpinski_string = '\n               /\\\n              /\/\\\n             /\  /\\\n            /\/\/\/\\\n           /\      /\\\n          /\/\    /\/\\\n         /\  /\  /\  /\\\n        /\/\/\/\/\/\/\/\\\n       /\              /\\\n      /\/\            /\/\\\n     /\  /\          /\  /\\\n    /\/\/\/\        /\/\/\/\\\n   /\      /\      /\      /\\\n  /\/\    /\/\    /\/\    /\/\\\n /\  /\  /\  /\  /\  /\  /\  /\\\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\\n'
        welcome_string = ("\nWelcome to n-flake generator developed by Stefan Devai\n"
                          "Visit the repo in: https://github.com/stefandevai/n-flakes\n")
        menu_string = ("\nOPTIONS:\n1 - Interactive generation\n"
                       "2 - Run demo\n"
                       "3 - Exit\n")

        print(header_string, sierpinski_string, welcome_string, menu_string)

        self.option = -1
        answered = False
        while answered == False:
            self.option = int(input('Select option: '))
            if self.option >= 1 and self.option <= 3:
                answered = True
            else:
                print('\nERROR: Invalid option')
                print(menu_string)

        if self.option == 3:
            pass
        else:
            if self.option == 1:
                self.input_generation()
            else:
                self.demo_generation()


    def update(self):
        self.running = True
        while self.running == True:
            for e in pg.event.get():
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        self.running = False
                    else:
                        if self.option == 1:
                            if e.key == K_LEFT:
                                if self.vertices > 3:
                                    self.vertices -= 1
                                    self.nflake = Flake(self.vertices, 250, self.center)
                            elif e.key == K_RIGHT:
                                if self.vertices < 20:
                                    self.vertices += 1
                                    self.nflake = Flake(self.vertices, 250, self.center)
                            elif e.key == K_DOWN:
                                if self.iterations > 1:
                                    self.iterations -= 1
                            elif e.key == K_UP:
                                if self.iterations < 7:
                                    self.iterations += 1
                            elif e.key == K_c:
                                self.colorful = not self.colorful
                            elif e.key == K_o:
                                self.outlined = not self.outlined
                elif e.type == QUIT:
                    self.running = False

            if self.option == 1:
                self.screen.fill(self.SCREEN_COLOR)
                self.nflake.outlined = self.outlined
                self.nflake.colorful = self.colorful
                self.nflake.draw(self.iterations, self.screen)
                pg.display.flip()

        pg.quit()

def main():
    generator = FlakeGenerator()
    generator.interactive_generation()
    generator.update()

if __name__ == '__main__':
    main()

