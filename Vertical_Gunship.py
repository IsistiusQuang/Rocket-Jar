import pygame

from Backdrop import WIN_WIDTH , WIN_HEIGHT
from Target import Prize
from Base_Class import Base_obj
from Gunship_Ammo import Magazine

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,50,50)
YELLOW = (255,255,0)

Prize_H_Rect = Prize.x + Prize.width
Prize_V_Rect = Prize.y + Prize.height

class Vertical_GS():
    color = RED
    rotate = 180
    mag = Magazine(WIN_WIDTH - 40,WIN_HEIGHT - 70,color)

    def movement(self,keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.x - self.mov_vel > Prize.x + Prize.width + 10:
            self.x -= self.mov_vel
        if keys_pressed[pygame.K_RIGHT] and self.x + self.mov_vel + self.width < WIN_WIDTH :
            self.x += self.mov_vel

    def bullet(self,event_key,sound):
        if event_key == pygame.K_RCTRL and self.mag.frame_count == 0:
            self.mag.make_changes()
            sound.play()
            bullet = pygame.Rect(
                self.x + round(self.width/2,3) - 2 , self.y , 4,10)
            self.bullet_list.append(bullet)

    def handle_bullet(self):
        if self.mag.frame_count != 0:
            if self.mag.frame_count == self.mag.next_reload_frame:
                self.mag.next_reload_frame = next(self.mag.reload_sp_iterator)
                next(self.mag.val_index).color = self.mag.color

            if self.mag.frame_counter():
                del self.bullet_list[:]
                self.mag.frame_count = 0
                for obj in self.mag.bullet_dict.values():
                    obj.color = self.mag.color

        for bullet in self.bullet_list:
            bullet.y -= self.bul_vel
            if bullet.y + bullet.width <= 0:
                self.bullet_list.remove(bullet)
                break

    def gunship_border(self):
        x = Prize_H_Rect + 10
        y = Prize_V_Rect
        width = WIN_WIDTH - x
        height = 5
        return Base_obj(x,y,width,height)
