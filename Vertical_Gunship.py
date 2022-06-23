import pygame

from Backdrop import WIN_WIDTH , WIN_HEIGHT
from Target import Prize
from Base_Class import Base_obj


Prize_H_Rect = Prize.x + Prize.width
Prize_V_Rect = Prize.y + Prize.height

class Vertical_GS():
    rotate = 180

    def movement(self,keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.x - self.mov_vel > Prize.x + Prize.width + 10:
            self.x -= self.mov_vel
        if keys_pressed[pygame.K_RIGHT] and self.x + self.mov_vel + self.width < WIN_WIDTH :
            self.x += self.mov_vel

    def bullet(self,event_key,sound):
        if event_key == pygame.K_RCTRL and len(self.bullet_list) < self.bullets_limit:
            sound.play()
            bullet = pygame.Rect(
                self.x + round(self.width/2,3) - 2 , self.y , 4,10)
            self.bullet_list.append(bullet)

    def handle_bullet(self):
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
