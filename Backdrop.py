import pygame
import os

from Base_Class import Base_obj

WIN_WIDTH , WIN_HEIGHT = 800,650

class Backdrop(Base_obj):
    def __init__(self,name,x,y,width,height):
        self.name = str(name)
        self.image = None
        Base_obj.__init__(self,x,y,width,height)
        self.make_image()

    def make_image(self):
        self.image = pygame.transform.scale( pygame.image.load(
            os.path.join( 'Assets' , self.name )) , ( self.width , self.height ))

SPACE = Backdrop('space.png',0,0,WIN_WIDTH,WIN_HEIGHT)


