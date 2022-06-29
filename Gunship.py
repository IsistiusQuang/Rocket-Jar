import pygame
import os

from Backdrop import WIN_WIDTH , WIN_HEIGHT
from Target import Prize
from Base_Class import Base_obj
from Vertical_Gunship import Vertical_GS
from Horizontal_Gunship import Horizontal_GS


class Gunship(Base_obj):
    score = 0
    mov_vel = 5
    bul_vel = 10
    # __init__ is the attributes method for python class
    # like c++ constructor
    # this method is called whenever an obj of this class is instantiated

    def __init__(self,x,y,name,file_name):
        Base_obj.__init__(self,x,y,40,40)
        self.name = str(name)
        self.file_name = str(file_name)
        self.bullet_list = []

        self.border = self.gunship_border()
        self.image = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load(
                os.path.join('Assets',self.file_name)), (self.width,self.height)), self.rotate )


class V_GS(Gunship,Vertical_GS):
    pass

class H_GS(Gunship,Horizontal_GS):
    pass

def make_GS(x,y,name,file,facing):
    if facing == "vertical":
        return V_GS(x,y,name,file)
    elif facing == "horizontal":
        return H_GS(x,y,name,file)


YELLOW_SPACESHIP = make_GS(10,Prize.y - 40 - 10,"YELLOW","spaceship_yellow.png","horizontal")
RED_SPACESHIP = make_GS(Prize.x + Prize.width + 10,WIN_HEIGHT - 40 - 10,"RED","spaceship_red.png","vertical")


