import pygame
import os

pygame.init()
pygame.display.set_caption("Flickering Test")

WIN_WIDTH = 800
WIN_HEIGHT = 600
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

Astroid_image = pygame.transform.scale(pygame.image.load(os.path.join("../Assets","Astroid_3.png")),(50,50))
Astroid_shadow = pygame.transform.scale(pygame.image.load(os.path.join("../Assets","Astroid_3_hitted.png")),(50,50))
Astroid_list = [Astroid_image,Astroid_shadow]
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("../Assets","space.png")),(WIN_WIDTH,WIN_HEIGHT))

def main():
    clock = pygame.time.Clock()
    FPS = 60
    frame_count = 0
    frame_limit = 10
    change_limit = 10
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(SPACE,(0,0))
        if frame_count < frame_limit:
            WIN.blit(Astroid_list[0],(0,0))
            frame_count +=1
        elif frame_count == frame_limit:
            Astroid_list[0],Astroid_list[1] = Astroid_list[1],Astroid_list[0]
            WIN.blit(Astroid_list[0],(0,0))
            frame_count = 1
            change_limit -= 1

        if change_limit == 0:
            run = False
            pygame.time.delay(2000)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
