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

class Horizontal_GS():
    color = YELLOW
    rotate = 90
    mag = Magazine(10,10,color)

    def movement(self,keys_pressed):
        if keys_pressed[pygame.K_w] and self.y - self.mov_vel > 0:
            self.y -= self.mov_vel
        if keys_pressed[pygame.K_s] and self.y + self.mov_vel + self.width < Prize.y - 10:
            self.y += self.mov_vel

    def bullet(self,event_key,sound):
        if event_key == pygame.K_LCTRL and self.mag.frame_count == 0:
            self.mag.make_changes()
            sound.play()
            bullet = pygame.Rect(
                self.x + self.width,self.y + round(self.height/2,3) - 2,10,4)
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
            bullet.x += self.bul_vel
            if bullet.x >= WIN_WIDTH:
                self.bullet_list.remove(bullet)
                break

    def gunship_border(self):
        x = 10 + 40 + 10
        y = 0
        width = 5
        height = Prize.y - 10
        return Base_obj(x,y,width,height)
