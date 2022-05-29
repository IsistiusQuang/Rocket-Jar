import pygame
import os

from Backdrop import WIN_WIDTH , WIN_HEIGHT


class Target:
    def __init__(self,name,width,height):
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets',str(name))),(width,height))
        self.game_over_image  = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets','White_splatter.png')),(width+50,height+50))
        self.width = width
        self.height = height
        self.x = 60
        self.y = WIN_HEIGHT - self.height - 60
        self.health = 3

        self.obj = pygame.Rect(self.x,self.y,self.width,self.height)

    def sound_effect(self):
        pass


Prize = Target('Winner_Award.png',50,40)
