
from Backdrop import WIN_WIDTH,WIN_HEIGHT
from Target import Prize
from Gunship import YELLOW_SPACESHIP , RED_SPACESHIP


class Astroid_Checkpoint:
    def __init__(self,a,b,c,d):
        self.low_x = a
        self.low_y = b
        self.high_x = c
        self.high_y = d


class Gunship_Border:
    def __init__(self,gunship):
        self.border = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        if gunship.facing == "Vertical":
            self.x = Prize.x + Prize.width + 10
            self.y = Prize.y + Prize.height
            self.width = WIN_WIDTH - self.x
            self.height = 5
            self.border = ( self.x , self.y , self.width , self.height )

        elif gunship.facing == "Horizontal":
            self.x = gunship.x + gunship.height + 10
            self.y = 0
            self.width = 5
            self.height = Prize.y - 10
            self.border = ( self.x , self.y , self.width , self.height )


Vertical = Gunship_Border(RED_SPACESHIP)
Horizontal = Gunship_Border(YELLOW_SPACESHIP)

Checkpoint_1 = Astroid_Checkpoint(Horizontal.x + Horizontal.width , Horizontal.y , WIN_WIDTH , Vertical.y  )
Checkpoint_2 = Astroid_Checkpoint(Horizontal.x + Horizontal.width , round((Vertical.y)/2,3),round((WIN_WIDTH + Horizontal.x)/2,3) , Vertical.y )
Checkpoint_3 = Astroid_Checkpoint( Prize.x , Prize.y , Prize.x + Prize.width , Prize.y + Prize.height )

for c in [Checkpoint_1,Checkpoint_2,Checkpoint_3]:
    print(f"low_x = {c.low_x} \t low_y = {c.low_y} \t high_x = {c.high_x} \t high_y = {c.high_y}")
