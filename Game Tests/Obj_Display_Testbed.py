import pygame
import os
pygame.display.init()

from random import randint,choice

WIN = pygame.display.set_mode((700,700))

WHITE = [255,255,255]
BLACK = [10.5,0.0,0]
RED = [255,50,50]
YELLOW = [255,255,0]
GREEN = [0,255,0]
GREY = [175,175,175]

class Base_obj:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obj = pygame.Rect(self.x,self.y,self.width,self.height)


class Cosmic(Base_obj):
    vel = 1
    def __init__(self,file_name,x,y,width = 50,height = 50):
         Base_obj.__init__(self,x,y,width,height)
         self.image = pygame.transform.scale(pygame.image.load(
            os.path.join('../Assets',file_name)).convert_alpha() , (self.width,self.height))

    def draw(self,win):
        win.blit(self.image,(self.x,self.y))

objs_name = []
for i in range(1,8):
    objs_name.append(f"Rock{i}.png")

Rock_objs = []
for x_coord in range(0,len(objs_name)):
    Rock_objs.append(Cosmic(objs_name[x_coord],x_coord*50,0))


def draw_surface():
    WIN.fill(WHITE)
    for rock in Rock_objs:
        rock.draw(WIN)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    FPS = 60

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_surface()
    pygame.quit()

if __name__ == "__main__":
    main()
