'''
Created on May 30, 2018

@author: mma_v
'''
import pygame
from rectangle import rectangle
from snowflake import snowflake
pygame.init()
width = 600
height = 400
surface = pygame.display.set_mode((width, height))
surface.fill((0,0,255))
import random
if __name__ == '__main__':
    toggle = True
    things = []
    ground = rectangle(0,250,(0,255,0),600,150)
    things.append(ground)
    while True:
        surface.fill((0,0,255))
        ground.draw(surface)
        if toggle == True:
            max = random.randint(250,400)
            num = random.randint(0,600)
            a = snowflake(num,0,(255,0,0),600,150,max)
            things.append(a)
            for i in range (1,len(things)):
                things[i].updateY(surface)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if toggle == True:
                        toggle = False
                    else:
                        toggle = True
        
    
