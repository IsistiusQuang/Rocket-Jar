import pygame

from Backdrop import WIN_WIDTH , WIN_HEIGHT
from Target import Prize
from Base_Class import Base_obj


Prize_H_Rect = Prize.x + Prize.width
Prize_V_Rect = Prize.y + Prize.height

class Horizontal_GS():
    rotate = 90

    def movement(self,keys_pressed):
        if keys_pressed[pygame.K_w] and self.y - self.mov_vel > 0:
            self.y -= self.mov_vel
        if keys_pressed[pygame.K_s] and self.y + self.mov_vel + self.width < Prize.y - 10:
            self.y += self.mov_vel

    def bullet(self,event_key,sound):
        if event_key == pygame.K_LCTRL and len(self.bullet_list) < self.bullets_limit:
            sound.play()
            bullet = pygame.Rect(
                self.x + self.width,self.y + round(self.height/2,3) - 2,10,4)
            self.bullet_list.append(bullet)

    def handle_bullet(self):
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
