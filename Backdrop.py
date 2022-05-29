import pygame
import os

WIN_WIDTH , WIN_HEIGHT = 800,650

class Backdrop:
    def __init__(self,x,y,width,height):
        self.image = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obj = pygame.Rect(x,y,width,height)

    def make_image(self,name):
        self.image = pygame.transform.scale( pygame.image.load(
            os.path.join( 'Assets' , str( name ))) , ( self.width , self.height ))

SPACE = Backdrop(0,0,WIN_WIDTH,WIN_HEIGHT)
SPACE.make_image('space.png')

