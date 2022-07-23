import pygame
import os

from Backdrop import WIN_WIDTH , WIN_HEIGHT

pygame.display.init()

class Target:
    health = 3
    width = 50
    height = 40
    x = 60
    y = WIN_HEIGHT - height - 60

    frame_count = 0
    frame_limit = 5
    flicker_count = 0
    flicker_limit = 7

    def __init__(self):
        self.image = self.make_image('Winner_Award.png',self.width,self.height)
        self.shadow_image = self.make_image('Winner_Award_hitted.png',self.width,self.height)
        self.game_over_image  = self.make_image('White_splatter.png', self.width+70 , self.height+70 )

        self.obj = pygame.Rect(self.x,self.y,self.width,self.height)

    def make_image(self,name,width,height):
        return pygame.transform.scale(
            pygame.image.load(os.path.join('Assets',name)).convert_alpha(),(width,height))

    def init_flicker(self):
        self.flicker_count = 0
        self.flicker_count += 1
        self.frame_count = 0

    def cycle_flicker(self):
        self.flicker_count += 1
        self.frame_count = 0

    def handle(self):
        if self.flicker_count != 0:
            self.frame_count += 1
            if self.frame_count == self.frame_limit:
                self.cycle_flicker()
                self.image , self.shadow_image = self.shadow_image, self.image

            if self.flicker_count > self.flicker_limit:
                self.image = self.make_image('Winner_Award.png',self.width,self.height)
                self.shadow_image = self.make_image('Winner_Award_hitted.png',self.width,self.height)

Prize = Target()
