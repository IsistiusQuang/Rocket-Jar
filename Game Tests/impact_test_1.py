import pygame
import os

from random import randint

RED = (255,0.0,0.0)
YELLOW = (255,255,0.0)
WIN_WIDTH = 800
WIN_HEIGHT = 650
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

TARGET_HIT = pygame.USEREVENT + 1

# class Astroid:
#     move_vel = 10
#     def __init__(self,name):
#         self.name = name
#         self.x = 740
#         self.y = 600.0
#         self.width = 60
#         self.height = 40
#         self.image = pygame.transform.scale(
#             pygame.image.load(os.path.join(
#                 '..\\Assets',str(name))),
#             (self.width,self.height))
#         self.obj = pygame.Rect(self.x,self.y,self.width,self.height)



# class Target:
#     def __init__(self,name,width,height):
#         self.width = width
#         self.height = height
#         self.x = 10
#         self.y = WIN_HEIGHT - self.height - 10
#         self.__health = 10
#         self.image = pygame.transform.scale(
#             pygame.image.load(os.path.join(
#                 '..\\Assets',str(name))),
#             (width,height))
#         self.obj = pygame.Rect(self.x,self.y,self.width,self.height)



# Prize = Target('Winner_Award.png',50,40)
# Ast_1 = Astroid('Astroid_1.png')
# Ast_2 = Astroid('Astroid_2.png')
# Astroid_list = [Ast_1,Ast_2]

# def target_hit(astroid_list,target):
#     for astroid in astroid_list:
#         if astroid.obj.colliderect(target.obj):
#             astroid_list.remove(astroid)
#             print(f"\t\t\t {astroid.name}: HIT!!!")
#             pygame.event.post(pygame.event.Event(TARGET_HIT))
#             break
#         else:
#             WIN.blit(astroid.image,(astroid.x,astroid.y))
#             astroid.x -= astroid.move_vel
#             astroid.obj.x -= astroid.move_vel
#             pygame.display.update()

image = pygame.transform.scale(
            pygame.image.load(os.path.join('../Assets','White_splatter.png')),(100,90))
prize = pygame.transform.scale(
            pygame.image.load(os.path.join('../Assets','Winner_Award.png')),(50,40))
space = pygame.transform.scale(
            pygame.image.load(os.path.join('../Assets','space.png')),(WIN_WIDTH,WIN_HEIGHT))
def main():
    clock = pygame.time.Clock()
    FPS = 60
    run = True
    while run:
        clock.tick(FPS)
        previous_height = 0.0
        previous_width = 0.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == TARGET_HIT:
                run = False


        if run == False:
            break
        WIN.fill((255,255,255))
        WIN.blit(space,(0,0))
        WIN.blit(image,(60,580))
        WIN.blit(prize,(0,70))
        #WIN.blit(Prize.image,(Prize.x,Prize.y))
        #target_hit(Astroid_list,Prize)
        pygame.display.update()



    pygame.quit()



if __name__ == "__main__":
    main()
