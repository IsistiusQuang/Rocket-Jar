import pygame
import os
from random import randint , choice

from Backdrop import WIN_WIDTH , WIN_HEIGHT
from Base_Class import Base_obj
from Ast_Health_Bar import Ast_Hlth_Bar
from Ast_Hitted import Astr_shadow , flickering

ran_list = [-3.0,-2.0,2.0,3.0]
#ran_list = [-1.0,1.0]
def Alter_range():
    return choice(ran_list)


class Astroid_class(Base_obj):
    astr_health = 6
    astroid_stage = 0
    move_count = 0
    move_limit = 3 # test figure = 15
    current_alter_x = -2
    current_alter_y = 2
    flickered = flickering

    def __init__(self,name,x,y,width,height):
        self.image = self.make_image(name,width,height)
        self.shadow = Astr_shadow(self.image,self.make_image(name[:-4]+"_hitted" + name[-4:],width,height))
        Base_obj.__init__(self,x+width,y-height,width,height)
        self.current_x = self.x
        self.current_y = self.y
        self.health_bar = Ast_Hlth_Bar(self.x,self.y,self.width,self.astr_health)
        self.current_x_limit = []
        self.current_y_limit = []
        self.checkpoints = []
        self.previous_vel = [0,0]
        self.delay_frame = choice([0,20,40,60])
        self.frame_count = 0
        self.frame_limit = self.delay_frame + (self.height//self.current_alter_y)


    def make_image(self,name,width,height):
        return pygame.transform.scale(
            pygame.image.load(os.path.join('Assets',name)),(width,height))


    def make_vel(self):
        self.current_alter_x = Alter_range()
        self.current_alter_y = Alter_range()


    def make_frame_limit(self):
        self.frame_count = 0
        self.frame_limit = randint(30,50)
        #print(f"Frame limits: {self.frame_limit}")


    def make_border_limit(self):
        self.move_count = 0
        #self.move_limit = 3

        self.current_x_limit.clear()
        self.current_y_limit.clear()

        current_border = self.checkpoints[-1]
        self.current_x_limit.extend([current_border.low_x,current_border.high_x])
        self.current_y_limit.extend([current_border.low_y,current_border.high_y])

        del self.checkpoints[-1]

    def spawn_delay(self):
        if self.previous_vel.count(0) > 0:
            if self.frame_count < self.delay_frame :
                #print(f"Current frame: {self.frame_count} \t Delay frame: {self.delay_frame}")
                self.frame_count += 1
                return True
            elif self.frame_count >= self.delay_frame:
                if self.frame_count >= self.frame_limit:
                    self.frame_limit = 0
                    self.frame_count = 0
                    return False
                elif self.frame_count < self.frame_limit:
                    self.frame_count += 1
                    self.current_x += self.current_alter_x
                    self.obj.x = self.current_x
                    self.current_y += self.current_alter_y
                    self.obj.y = self.current_y
                    return True
        elif self.previous_vel.count(0) == 0:
            return False


    def checking_previous_move(self):
        self.make_vel()
        if self.previous_vel[0] == -self.current_alter_x and self.previous_vel[1] == -self.current_alter_y :
            new_ran = ran_list[:]
            if randint(0,1) == 0:
                new_ran.remove(self.current_alter_x)
                self.current_alter_x = choice(new_ran)
                self.current_alter_y = choice(ran_list)
            else:
                new_ran.remove(self.current_alter_y)
                self.current_alter_x = choice(ran_list)
                self.current_alter_y = choice(new_ran)

        self.previous_vel.clear()
        self.previous_vel.append(self.current_alter_x)
        self.previous_vel.append(self.current_alter_y)


    def move(self):
        #print(f"x1 : {self.obj.x} \t y1 : {self.obj.y}")
        #print(f"current alter x = {self.current_alter_x}\tcurrent alter y = {self.current_alter_y}")
        self.flickered()
        self.frame_count += 1
        if self.obj.x + self.width + self.current_alter_x > self.current_x_limit[1] or self.obj.x + self.current_alter_x < self.current_x_limit[0] :
            self.current_alter_x = - self.current_alter_x
            self.current_x += self.current_alter_x
            self.obj.x = self.current_x
        else:
            self.current_x += self.current_alter_x
            self.obj.x = self.current_x

        if self.obj.y + self.current_alter_y < self.current_y_limit[0] or self.obj.y + self.height + self.current_alter_y > self.current_y_limit[1] :
            self.current_alter_y = - self.current_alter_y
            self.current_y += self.current_alter_y
            self.obj.y = self.current_y
        else:
            self.current_y += self.current_alter_y
            self.obj.y = self.current_y
        self.health_bar.move(self.obj.x,self.obj.y)
        #print(f"x2 : {self.obj.x} \t y2 : {self.obj.y}")
        #print(f"current alter x = {self.current_alter_x}\tcurrent alter y = {self.current_alter_y}")

    def to_checkpoint(self):
        self.move_count = self.move_limit
        #self.move_limit = 0
        self.frame_count = 0
        objective = self.checkpoints[-1]
        self.frame_limit = randint(80,100)
        if self.obj.x + self.width > objective.high_x and self.obj.y < objective.low_y:
            self.current_alter_x = round((objective.high_x + 1 - self.obj.x - self.width) / self.frame_limit,3) - 0.1
            self.current_alter_y = round((objective.low_y + 1 - self.obj.y) / self.frame_limit,3) + 0.1

        elif self.obj.x + self.width > objective.high_x:
            self.current_alter_x = round((objective.high_x + 1 - self.obj.x - self.width) / self.frame_limit ,3) - 0.1
            new_ran = [i for i in ran_list if i > 0]
            self.current_alter_y = choice(new_ran)

        elif self.obj.y < objective.low_y:
            self.current_alter_y = round((objective.low_y + 1 - self.obj.y) / self.frame_limit ,3) + 0.1
            new_ran = [i for i in ran_list if i < 0]
            self.current_alter_x = choice(new_ran)
            #print(f"Current Alter x = {self.current_alter_x}")
            #print(f"Current Alter y = {self.current_alter_y}")

        #print(f"Frane limits for going to checkpoint: {self.frame_limit}")


