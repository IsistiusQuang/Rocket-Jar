import pygame
from random import randint

from Backdrop import WIN_WIDTH , WIN_HEIGHT
from Astroid import Astroid_class
from Checkpoints import Checkpoint_1, Checkpoint_2 ,Checkpoint_3


ASTROID_NAMES = ['Astroid_1.png','Astroid_2.png','Astroid_3.png']
Plausible_sizes = []
Min_width , Min_height = 40,60
Max_width , Max_height = 80,120
for i in range(0,4):
    Plausible_sizes.append((
        Min_width + i*(Max_width - Min_width )//4,
        Min_height + i*(Max_height - Min_height)//4  ))

def Starting_positions(obj_width):
    return {randint(WIN_WIDTH - 160,WIN_WIDTH - obj_width - 1):0 , WIN_WIDTH - obj_width : randint(1,130)}


class Astroid_limits:
    def __init__(self):
        self.Astroid_list = []
        self.wave = 1
        self.wave_count = 0
        self.astroid_num = 1

    def fill_list(self):
        while len(self.Astroid_list) < self.astroid_num :
            position_pair = randint(0,1)
            size_pair = randint(0,3)
            current_position = Starting_positions(Plausible_sizes[size_pair][0])
            self.Astroid_list.append( Astroid_class ( ASTROID_NAMES[randint(0,2)],
                    list(current_position.keys())[position_pair] ,
                    list(current_position.values())[position_pair] ,
                    Plausible_sizes[size_pair][0] ,
                    Plausible_sizes[size_pair][1]  ) )

    def fill_in_checkpoints(self,checkpoint_list):
        for obj in self.Astroid_list:
            obj.checkpoints = checkpoint_list[:]
            obj.make_border_limit()

    def next_wave(self):
        if self.wave_count < self.wave:
            self.wave_count += 1
            self.fill_list()
            self.fill_in_checkpoints([Checkpoint_3,Checkpoint_2,Checkpoint_1])
            self.astroid_num += 2

Astroids = Astroid_limits()
Astroids.next_wave()


#current_border = [Checkpoint_3,Checkpoint_2,Checkpoint_1][1]
#print(f"low_x = {current_border.low_x} \t low_y = {current_border.low_y} \t high_x = {current_border.high_x} \t high_y = {current_border.high_y} ")



