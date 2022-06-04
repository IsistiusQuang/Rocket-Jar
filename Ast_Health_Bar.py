import pygame

from Base_Class import Base_obj


GREEN = [0,255,0]
BLACK = [0,0,0]

class Ast_Hlth_Bar():
    hlth_bar_width = 40
    hlth_bar_height = 4
    def __init__(self,ast_x,ast_y,ast_width,ast_health):
        self.inner = Base_obj(ast_x - (self.hlth_bar_width-ast_width)/2 , ast_y - self.hlth_bar_height - 5 , self.hlth_bar_width , self.hlth_bar_height )
        self.outer = Base_obj(self.inner.obj.x - 1,self.inner.obj.y - 1 , self.inner.width + 2 , self.inner.height + 2 )
        self.current_ast_x = ast_x
        self.current_ast_y = ast_y
        self.color = GREEN[:]
        self.health = ast_health

    def move(self,new_ast_x,new_ast_y):
        self.inner.obj.x += (new_ast_x - self.current_ast_x)
        self.outer.obj.x += (new_ast_x - self.current_ast_x)

        self.inner.obj.y += (new_ast_y - self.current_ast_y)
        self.outer.obj.y += (new_ast_y - self.current_ast_y)

        self.current_ast_x = new_ast_x
        self.current_ast_y = new_ast_y

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.inner.obj,0,2)
        pygame.draw.rect(surface,BLACK,self.outer.obj,1,2)

    def shiftin_color(self):
        if self.color[0] + 255/self.health*2 <= 255:
            self.color[0] += 255/self.health*2

        elif self.color[1] - 255/self.health*2 >= 0:
            self.color[1] -= 255/self.health*2
        # self.color[0] == 255 - (255%(255/self.health*2)) and

    def decreasin_length(self):
        if self.inner.obj.w - self.inner.width/self.health >= 0:
            self.inner.obj.w -= self.inner.width/self.health
            self.shiftin_color()

