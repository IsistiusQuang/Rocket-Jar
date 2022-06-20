import pygame
import os

pygame.init()
pygame.display.set_caption("Flickering Test")

WIN_WIDTH = 800
WIN_HEIGHT = 600
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

name = "Astroid_3.png"
Astroid_image = pygame.transform.scale(pygame.image.load(os.path.join("../Assets","Astroid_3.png")),(50,50))
Astroid_shadow = pygame.transform.scale(pygame.image.load(os.path.join("../Assets",name[:-4]+"_hitted"+name[-4:])),(50,50))
Astroid_list = [Astroid_image,Astroid_shadow]
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("../Assets","space.png")),(WIN_WIDTH,WIN_HEIGHT))


class Flashing:
    def __init__(self):
        self.frame_count = 0
        self.frame_limit = 60
        self.change_limit = 4

    def draw_surface(self):
        WIN.blit(SPACE,(0,0))

        if self.change_limit != 0:
            if self.frame_count < self.frame_limit:
                WIN.blit(Astroid_list[0],(0,0))
                self.frame_count +=1
            elif self.frame_count == self.frame_limit:
                Astroid_list[0],Astroid_list[1] = Astroid_list[1],Astroid_list[0]
                WIN.blit(Astroid_list[0],(0,0))
                self.frame_count = 1
                self.change_limit -= 1
        else:
            pygame.time.delay(2000)
        pygame.display.update()
F1 = Flashing()

def main():
    clock = pygame.time.Clock()
    FPS = 60

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        F1.draw_surface()

    pygame.quit()


if __name__ == "__main__":
    main()
