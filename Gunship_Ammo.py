import pygame

from Base_Class import Base_obj


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,50,50)
YELLOW = (255,255,0)
GREY = [175,175,175]

class Ammo(Base_obj):
    def __init__(self,x,y,width,height,color):
        Base_obj.__init__(self,x,y,width,height)
        self.color = color


class Magazine(Base_obj):
    frame_count = 0
    frame_limit = 120
    capacity = 6

    def __init__(self,x,y,color):
        super().__init__(x,y,30,60)
        self.color = color
        self.bullet_dict = {}
        self.make_bullet_dict()
        self.iterator = self.yield_val(self.bullet_dict.keys())
        self.key_index = next(self.iterator)
        self.val_index = None
        self.reload_sp_iterator = None
        self.next_reload_frame = None

    def draw(self,WIN):
        pygame.draw.rect(WIN,GREY,self.obj,0,2)
        pygame.draw.rect(WIN,BLACK,self.obj,1,2)
        for bul in self.bullet_dict.values():
            pygame.draw.rect(WIN,bul.color,bul.obj,0,2)
            pygame.draw.rect(WIN,BLACK,bul.obj,1,2)

    def make_ammo_height(self):
        return (self.height - 3 * (self.capacity + 1))/self.capacity

    def frame_counter(self):
        self.frame_count += 1
        return self.frame_count == self.frame_limit

    def make_bullet_dict(self):
        current_y = self.y + 3
        for i in range(0,self.capacity):
            self.bullet_dict[i] = Ammo(self.x + 3 , current_y , self.width - 6 , self.make_ammo_height(),self.color)
            current_y += self.make_ammo_height() + 3

    def yield_val(self,objs):
        for val in objs:
            yield val

    def make_changes(self):
        try:
            self.bullet_dict[self.key_index].color = WHITE
            self.key_index = next(self.iterator)

        except StopIteration:
            self.frame_count += 1
            self.iterator = self.yield_val(self.bullet_dict.keys())
            self.key_index = next(self.iterator)
            self.val_index = self.yield_val(list(self.bullet_dict.values())[::-1])
            self.reload_sp_iterator = self.yield_val([i for i in range(self.frame_limit//self.capacity,self.frame_limit+1,self.frame_limit//self.capacity)])
            self.next_reload_frame = next(self.reload_sp_iterator)


