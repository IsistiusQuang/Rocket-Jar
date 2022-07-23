import pygame
import os
pygame.mixer.init()

from Backdrop import WIN_WIDTH , WIN_HEIGHT


ASTROID_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
TARGET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

ASTROID_HIT_SOUND.set_volume(0.1)
TARGET_HIT_SOUND.set_volume(0.1)
BULLET_FIRE_SOUND.set_volume(0.1)

PRICE_HIT = pygame.USEREVENT + 1
ASTROID_HIT = pygame.USEREVENT + 2


def astroid_impact(astroid,price):
    if astroid.obj.colliderect(price.obj):
        price.init_flicker()
        TARGET_HIT_SOUND.play()
        if price.health == 1:
            pygame.event.post(pygame.event.Event(PRICE_HIT))
        else:
            price.health -= 1
            astroid.astroid_stage = 1


def bullet_impact(astroid,spaceship):
    for bullet in spaceship.bullet_list:
        if bullet.colliderect(astroid.obj):
            ASTROID_HIT_SOUND.play()
            astroid.astr_health -= 1
            astroid.health_bar.decreasin_length()
            astroid.shadow.init_flicker()
            spaceship.bullet_list.remove(bullet)
            if astroid.astr_health == 0:
                astroid.astroid_stage = 1
                spaceship.score += 1
            break

