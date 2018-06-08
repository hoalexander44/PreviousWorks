import pygame
from abc import ABCMeta

class Drawable(metaclass = ABCMeta):
	def draw(self,surface):
		pass
	
	@classmethod
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y
		
	def getLoc(self):
		return (self.__x, self.__y)
	
	def setLoc(self,p):
		self.__x = p[0]
		self.__y = p[1]
	

