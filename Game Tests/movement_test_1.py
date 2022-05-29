import pygame


myobj = pygame.Rect(0,0,100,100)
objx = 0

WIN = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
FPS = 60
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    a = 10
    for i in range(0,1):
        objx += 0.8
        myobj.x = objx
        print(f"In game: {myobj.x}")
        pygame.time.delay(1000)

print(f"Out game: {myobj.x}")
