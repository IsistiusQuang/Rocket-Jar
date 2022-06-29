import pygame
import pygame.gfxdraw

WIN = pygame.display.set_mode((500,500))

WHITE = [255,255,255]
BLACK = [10.5,0.0,0]
RED = [255,50,50]
YELLOW = [255,255,0]
GREEN = [0,255,0]
LI_GREY = [175,175,175]

class Base_obj:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obj = pygame.Rect((self.x,self.y),(self.width,self.height))

class Ammo(Base_obj):
    def __init__(self,x,y,width,height):
        Base_obj.__init__(self,x,y,width,height)
        self.color = YELLOW


class Magazine(Base_obj):
    frame_count = 0
    frame_limit = 90
    def __init__(self,capa,rld_sp):
        super().__init__(100,100,30,60)
        self.capacity = capa
        self.reload_speed = rld_sp
        self.bullet_dict = {}
        self.make_bullet_dict()
        self.iterator = self.bul_index()

    def draw(self):
        pygame.draw.rect(WIN,LI_GREY,self.obj,0,2)
        pygame.draw.rect(WIN,BLACK,self.obj,1,2)
        for bul in self.bullet_dict.values():
            pygame.draw.rect(WIN,bul.color,bul.obj,0,3)
            pygame.draw.rect(WIN,BLACK,bul.obj,1,3)

    def make_ammo_height(self):
        return (self.height - 3 * (self.capacity + 1))/self.capacity

    def make_bullet_dict(self):
        current_y = self.y + 3
        for i in range(0,self.capacity):
            self.bullet_dict[i] = Ammo(self.x + 3 , current_y , self.width - 6 , self.make_ammo_height())
            current_y += self.make_ammo_height() + 3

    def bul_index(self):
        for index in self.bullet_dict.keys():
            yield index

    def make_changes(self):
        try:
            current_index = next(self.iterator)
            self.bullet_dict[current_index].color = RED

        except StopIteration:
            if self.frame_counter():
                self.frame_count = 0
                self.iterator = self.bul_index()
                for obj in self.bullet_dict.values():
                    obj.color = YELLOW

Mag = Magazine(5,10)
n = 0


def draw_surface():
    WIN.fill(LI_GREY)
    Mag.draw()
    #pygame.gfxdraw.hline(WIN,50,100,50,BLACK)
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
