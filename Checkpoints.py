
from Backdrop import WIN_WIDTH,WIN_HEIGHT
from Target import Prize
from Base_Class import Base_obj


Prize_H_Rect = Prize.x + Prize.width
Prize_V_Rect = Prize.y + Prize.height

class Astroid_Checkpoint:
    def __init__(self,a,b,c,d):
        self.low_x = a
        self.low_y = b
        self.high_x = c
        self.high_y = d


class Gunship_Border(Base_obj):
    def __init__(self,facing):
        self.border = None
        if facing == "Vertical":
            x = Prize_H_Rect + 10
            y = Prize_V_Rect
            width = WIN_WIDTH - x
            height = 5
            Base_obj.__init__(self,x,y,width,height)


        elif facing == "Horizontal":
            x = 10 + 40 + 10
            y = 0
            width = 5
            height = Prize.y - 10
            Base_obj.__init__(self,x,y,width,height)


Checkpoint_1 = Astroid_Checkpoint( 65 , 0 , WIN_WIDTH , Prize_V_Rect )
Checkpoint_2 = Astroid_Checkpoint( 65 , round((Prize_V_Rect)/2,3),round((WIN_WIDTH + 65)/2,3) , Prize_V_Rect )
Checkpoint_3 = Astroid_Checkpoint( Prize.x , Prize.y , Prize_H_Rect , Prize_V_Rect )

for c in [Checkpoint_1,Checkpoint_2,Checkpoint_3]:
    print(f"low_x = {c.low_x} \t low_y = {c.low_y} \t high_x = {c.high_x} \t high_y = {c.high_y}")
