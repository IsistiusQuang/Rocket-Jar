import pygame

class Base_obj:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obj = pygame.Rect(self.x,self.y,self.width,self.height)
