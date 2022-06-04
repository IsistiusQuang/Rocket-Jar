import pygame

WIN = pygame.display.set_mode((500,500))

WHITE = [255,255,255]
BLACK = [10.5,0.0,0]
RED = [255,50,50]
YELLOW = [255,255,0]
GREEN = [0,255,0]

# Declare new obj here
class Base_obj:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obj = pygame.Rect((self.x,self.y),(self.width,self.height))

class Ast_Hlth_Bar():
    hlth_width = 60
    hlth_height = 5
    frame_count = 0

    def __init__(self,ast_x,ast_y,ast_width,ast_health):
        self.inner = Base_obj(ast_x - (self.hlth_width-ast_width)/2 , ast_y - self.hlth_height - 10 , self.hlth_width , self.hlth_height )
        self.outer = Base_obj(self.inner.obj.x - 1 , self.inner.obj.y - 1 , self.inner.obj.width + 2 , self.inner.obj.height + 2 )
        self.color = GREEN[:]
        self.health = ast_health

    def draw(self):
        pygame.draw.rect(WIN,self.color,self.inner.obj,0,2)
        pygame.draw.rect(WIN,BLACK,self.outer.obj,1,2)

    def shiftin_color(self):
        if self.color[0] + 255/5 <= 255 :
            self.color[0] += 255/5

        if self.color[0] >= 255/10*9 and self.color[1] - 255/5 >= 0:
            self.color[1] -= 255/5

    def decreasing_length(self):
        self.frame_count += 1
        if self.frame_count == 60:
            self.frame_count = 0
            if self.inner.obj.w - self.inner.width/self.health >= 0:
                self.inner.obj.w -= self.inner.width/self.health
                self.shiftin_color()

H1 = Ast_Hlth_Bar(100,100,120,10)


def draw_surface():
    # draw obj here
    WIN.fill(WHITE)
    H1.draw()
    #H1.shiftin_color()
    H1.decreasing_length()
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
