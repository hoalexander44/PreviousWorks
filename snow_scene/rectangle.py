'''
Created on May 30, 2018

@author: mma_v
'''
from Drawable import Drawable 
import pygame

class rectangle(Drawable):

    '''
    classdocs
    '''


    def __init__(self, x, y, color, width, height):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self, surface):
        x,y = super().getLoc()
        pygame.draw.rect(surface, self.__color, [x, y,self.__width,self.__height])
        