import pygame
import os

from Backdrop import WIN_WIDTH , WIN_HEIGHT
from Target import Prize
from Checkpoints import Gunship_Border
from Base_Class import Base_obj


class Gunship(Base_obj):
    score = 0
    mov_vel = 5
    bul_vel = 3
    bullets_limit = 3
    # __init__ is the attributes method for python class
    # like c++ constructor
    # this method is called whenever an obj of this class is instantiated

    def __init__(self,x,y,name,file_name,facing):
        Base_obj.__init__(self,x,y,40,40)
        self.name = str(name)
        self.file_name = str(file_name)
        self.facing = str(facing)
        self.border = Gunship_Border(self.facing)
        self.bullet_list = []
        self.image = None
        self.making_image()


    def making_image(self):
        Rotate = int()
        if self.facing == "Horizontal":
            Rotate = 90
        elif self.facing == "Vertical":
            Rotate = 180
        Image = pygame.image.load(os.path.join('Assets',self.file_name))
        Scale = pygame.transform.scale(Image,(self.width,self.height))
        Orientation = pygame.transform.rotate(Scale,Rotate)
        self.image = Orientation


    def movement(self,keys_pressed):
        if self.facing == "Horizontal":
            if keys_pressed[pygame.K_w] and self.y - self.mov_vel > 0:
                self.y -= self.mov_vel
            if keys_pressed[pygame.K_s] and self.y + self.mov_vel + self.width < Prize.y - 10:
                self.y += self.mov_vel

        elif self.facing == "Vertical":
            if keys_pressed[pygame.K_LEFT] and self.x - self.mov_vel > Prize.x + Prize.width + 10:
                self.x -= self.mov_vel
            if keys_pressed[pygame.K_RIGHT] and self.x + self.mov_vel + self.width < WIN_WIDTH :
                self.x += self.mov_vel


    def bullet(self,event_key,sound):
        # handling bullet
        if self.facing == "Vertical" and event_key == pygame.K_RCTRL and len(self.bullet_list) < self.bullets_limit:
            sound.play()
            bullet = pygame.Rect(
                self.x + round(self.width/2,3) - 2 , self.y , 4,10)
            self.bullet_list.append(bullet)

        if self.facing == "Horizontal" and event_key == pygame.K_LCTRL and len(self.bullet_list) < self.bullets_limit:
            sound.play()
            bullet = pygame.Rect(
                self.x + self.width,self.y + round(self.height/2,3) - 2,10,4)
            self.bullet_list.append(bullet)

    def handle_bullet(self):
        for bullet in self.bullet_list:
            if self.facing == "Horizontal":
                bullet.x += self.bul_vel
                if bullet.x >= WIN_WIDTH:
                    self.bullet_list.remove(bullet)
                    break

            elif self.facing == "Vertical":
                bullet.y -= self.bul_vel
                if bullet.y + bullet.width <= 0:
                    self.bullet_list.remove(bullet)
                    break


YELLOW_SPACESHIP = Gunship(10,Prize.y - 40 - 10,"YELLOW","spaceship_yellow.png",'Horizontal')
RED_SPACESHIP = Gunship(Prize.x + Prize.width + 10,WIN_HEIGHT - 40 - 10,"RED","spaceship_red.png",'Vertical')




