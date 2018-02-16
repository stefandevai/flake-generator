import math
import pygame as pg
from pygame import gfxdraw

class Polygon:
    ROTATION = 90

    def __init__(self, nv, rd, ct):
        self.num_vertices = nv
        self.radius = rd
        self.center = ct
        self.angle_base = 360/self.num_vertices
        self.fill = True

    def draw(self, win, inv, col=(0,0,0)):
        coords = []
        for i in range(0, self.num_vertices):
            cx = round(self.center[0] + self.radius*math.cos(math.radians(self.angle_base*i + self.ROTATION)))
            cy = round(self.center[1] - inv*self.radius*math.sin(math.radians(self.angle_base*i + self.ROTATION)))
            coords.append((cx, cy))

        pg.gfxdraw.aapolygon(win, coords, self.color)
        if self.fill == True:
            pg.gfxdraw.filled_polygon(win, coords, self.color)

class Flake:
    ROTATION = 90
    # COLORS = [(252, 224, 146), (252, 183, 150), (179, 135, 120), (148, 116, 107), (91, 78, 83), (57, 56, 69), (47, 50, 65)]
    COLORS = [(243, 239, 219), (236, 221, 205), (189, 205, 171), (120, 203, 188), (103, 153, 162), (78, 107, 119)]

    def __init__(self, nv, rd, ct):
        self.num_vertices = nv
        self.radius = rd
        self.center = ct
        self.angle_base = 360/self.num_vertices
        self.colorful = False
        self.outlined = False

    def draw(self, st, win):
        self.steps = st
        self.screen_ref = win
        self.__get_scale_factor()

        # If there are too few flakes to make a polygon, or if it's a pseudo circle
        if self.num_vertices < 3 or self.num_vertices > 20:
            pass
        # Handle the hexaflake
        elif self.num_vertices == 6:
            self.__draw_hexaflake(self.steps, self.radius, self.center)
        # Handle the pentaflake
        elif self.num_vertices == 5:
            self.__draw_pentaflake(self.steps, self.radius, self.center, 1)
        # Handle Vicsek fractal
        elif self.num_vertices == 4:
            self.scale_factor = 1 / 3
            self.__draw_vicsek(self.steps, self.radius, self.center)
        else:
            self.__draw_nflake(self.steps, self.radius, self.center)

    def __get_scale_factor(self):
        aux = 0
        for i in range(0, self.num_vertices//4):
            aux += math.cos(2*math.pi*(i+1) / self.num_vertices)
        self.scale_factor = 1 / (2*(1 + aux))

    def __draw_hexaflake(self, steps, rd, ct):
        if steps <= 0:
            pass
        elif steps == 1:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.color = self.COLORS[steps-1]
            if self.outlined == True:
                poly.fill = False

            poly.draw(self.screen_ref, 1)
        else:
            if self.colorful == True:
                poly = Polygon(self.num_vertices, rd, ct)
                poly.color = self.COLORS[steps-1]
                if self.outlined == True:
                    poly.fill = False

                poly.draw(self.screen_ref, 1)

            self.__draw_hexaflake(steps-1, rd*self.scale_factor, ct)
            for i in range(0, self.num_vertices):
                cx = ct[0] + rd*math.cos(math.radians((self.angle_base)*i + self.ROTATION)) - rd*self.scale_factor*math.cos(math.radians((self.angle_base)*i + self.ROTATION))
                cy = ct[1] + rd*math.sin(math.radians((self.angle_base)*i - self.ROTATION)) + rd*self.scale_factor*math.sin(math.radians((self.angle_base)*i + self.ROTATION))
                self.__draw_hexaflake(steps-1, rd*self.scale_factor, (cx, cy))

    def __draw_pentaflake(self, steps, rd, ct, inv):
        if steps <= 0:
            pass
        elif steps == 1:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.color = self.COLORS[steps-1]
            if self.outlined == True:
                poly.fill = False

            poly.draw(self.screen_ref, inv)
        else:
            if self.colorful == True:
                poly = Polygon(self.num_vertices, rd, ct)
                poly.color = self.COLORS[steps-1]
                if self.outlined == True:
                    poly.fill = False

                poly.draw(self.screen_ref, inv)

            self.__draw_pentaflake(steps-1, rd*self.scale_factor, ct, -inv)
            for i in range(0, self.num_vertices):
                cx = ct[0] + rd*math.cos(math.radians((self.angle_base)*i + self.ROTATION)) - rd*self.scale_factor*math.cos(math.radians((self.angle_base)*i + self.ROTATION))
                cy = ct[1] + rd*math.sin(math.radians((self.angle_base)*i - inv*self.ROTATION)) + inv*rd*self.scale_factor*math.sin(math.radians((self.angle_base)*i + self.ROTATION))
                self.__draw_pentaflake(steps-1, rd*self.scale_factor, (cx, cy), inv)

    def __draw_vicsek(self, steps, rd, ct):
        if steps <= 0:
            pass
        elif steps == 1:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.color = self.COLORS[steps-1]
            if self.outlined == True:
                poly.fill = False

            poly.draw(self.screen_ref, 1)
        else:
            if self.colorful == True:
                poly = Polygon(self.num_vertices, rd, ct)
                poly.color = self.COLORS[steps-1]
                if self.outlined == True:
                    poly.fill = False

                poly.draw(self.screen_ref, 1)

            self.__draw_vicsek(steps-1, rd*self.scale_factor, ct)
            for i in range(0, self.num_vertices):
                cx = ct[0] + rd*math.cos(math.radians((self.angle_base)*i + self.ROTATION)) - rd*self.scale_factor*math.cos(math.radians((self.angle_base)*i + self.ROTATION))
                cy = ct[1] + rd*math.sin(math.radians((self.angle_base)*i - self.ROTATION)) + rd*self.scale_factor*math.sin(math.radians((self.angle_base)*i + self.ROTATION))
                self.__draw_vicsek(steps-1, rd*self.scale_factor, (cx, cy))

    def __draw_nflake(self, steps, rd, ct):
        if steps <= 0:
            pass
        elif steps == 1:
            poly = Polygon(self.num_vertices, rd, ct)
            poly.color = self.COLORS[steps-1]
            if self.outlined == True:
                poly.fill = False

            poly.draw(self.screen_ref, 1)
        else:
            if self.colorful == True:
                poly = Polygon(self.num_vertices, rd, ct)
                poly.color = self.COLORS[steps-1]
                if self.outlined == True:
                    poly.fill = False

                poly.draw(self.screen_ref, 1)

            for i in range(0, self.num_vertices):
                cx = ct[0] + rd*math.cos(math.radians((self.angle_base)*i + self.ROTATION)) - rd*self.scale_factor*math.cos(math.radians((self.angle_base)*i + self.ROTATION))
                cy = ct[1] + rd*math.sin(math.radians((self.angle_base)*i - self.ROTATION)) + rd*self.scale_factor*math.sin(math.radians((self.angle_base)*i + self.ROTATION))
                self.__draw_nflake(steps-1, rd*self.scale_factor, (cx, cy))

