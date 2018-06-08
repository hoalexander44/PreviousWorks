'''
Created on May 30, 2018

@author: mma_v
'''
from Drawable import Drawable
import pygame as pg
class snowflake(Drawable):

    def __init__(self, x, y, color, width, height, maximum):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color
        self.__max = maximum

    def updateY(self, surface):
        x,y = super().getLoc()
        a,b = x,(y+0.5)
        if b < self.__max:
            super().setLoc((a,b))
        x,y = super().getLoc()
        pg.draw.line(surface,(255, 255, 255), (x-5,y), (x+5, y))
        pg.draw.line(surface,(255, 255, 255), (x,y-5), (x, y+5))
        pg.draw.line(surface,(255, 255, 255), (x-5,y-5), (x+5, y+5))
        pg.draw.line(surface,(255, 255, 255), (x-5,y+5), (x+5, y-5))
##    def __init__(self, x):
##        super().__init__(x, 0)
##    def updateY(self):
##        x,y = super().getLoc()
##    def draw(self, surface):
##        pg.draw.line(surface,(255, 255, 255), (self.__x-5,self.__y), (self.__x+5, self.__y))
##        pg.draw.line(surface,(255, 255, 255), (self.__x,self.__y-5), (self.__x, self.__y+5))
##        pg.draw.line(surface,(255, 255, 255), (self.__x-5,self.__y-5), (self.__x+5, self.__y+5))
##        pg.draw.line(surface,(255, 255, 255), (self.__x-5,self.__y+5), (self.__x+5, self.__y-5))
        