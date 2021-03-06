import pygame
import os
pygame.display.init()
pygame.font.init()

from Gunship import YELLOW_SPACESHIP,RED_SPACESHIP
from Backdrop import WIN_WIDTH , WIN_HEIGHT , SPACE , COSMIC_STUFFS
from List_Of_Astroids import Astroids
from Target import Prize


WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,50,50)
YELLOW = (255,255,0)

HEALTH_FONT = pygame.font.SysFont('comicsans',30)
WINNER_FONT = pygame.font.SysFont('comicsans',50)
gameover_text = WINNER_FONT.render("GAME OVER",1,WHITE)
def game_over():
    WIN.blit(SPACE.image,(0,0))
    WIN.blit(gameover_text,((WIN_WIDTH - gameover_text.get_width())//2,(WIN_HEIGHT - gameover_text.get_height())//2))
    pygame.display.update()
    pygame.time.delay(3000)


def draw_surface():
    WIN.blit(SPACE.image,(0,0))
    COSMIC_STUFFS.draw(WIN)

    pygame.draw.rect(WIN,WHITE,YELLOW_SPACESHIP.border.obj)
    pygame.draw.rect(WIN,WHITE,RED_SPACESHIP.border.obj)

    YELLOW_SPACESHIP.mag.draw(WIN)
    RED_SPACESHIP.mag.draw(WIN)

    WIN.blit(YELLOW_SPACESHIP.image,(YELLOW_SPACESHIP.x,YELLOW_SPACESHIP.y))
    WIN.blit(RED_SPACESHIP.image,(RED_SPACESHIP.x,RED_SPACESHIP.y))

    for bullet in YELLOW_SPACESHIP.bullet_list:
        pygame.draw.rect(WIN,YELLOW_SPACESHIP.color,bullet)
    for bullet in RED_SPACESHIP.bullet_list:
        pygame.draw.rect(WIN,RED_SPACESHIP.color,bullet)

    WIN.blit(Prize.image,(Prize.x,Prize.y))
    health_text = HEALTH_FONT.render(str(Prize.health),1,WHITE)
    WIN.blit(health_text,(20 , WIN_HEIGHT - health_text.get_height() - 10))

    for rock in Astroids.Astroid_list:
        WIN.blit(rock.image,(rock.obj.x,rock.obj.y))
        rock.health_bar.draw(WIN)
    pygame.display.update()

def draw_winner(spaceship_dict):
    keys_set = set(spaceship_dict.keys())
    if len(keys_set) == 1:
        winner_text = WINNER_FONT.render("DRAW ! SHARE THE PILLS =)",1,WHITE)
    elif len(keys_set) > 1:
        winner_text = WINNER_FONT.render(f"{spaceship_dict[max(keys_set)]} GET THE PILLS !",1,WHITE)
    WIN.blit(winner_text,(WIN_WIDTH//2 - winner_text.get_width()//2
        ,WIN_HEIGHT//2 - winner_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)
    game_over()


def draw_gameover():
    message = WINNER_FONT.render("NO ONE GETS THE PILLS :')",1,WHITE)
    WIN.blit(message,((WIN_WIDTH - message.get_width())//2,(WIN_HEIGHT-message.get_height())//2))
    WIN.blit(Prize.game_over_image,(Prize.x-25,Prize.y-25))
    pygame.display.update()
    pygame.time.delay(3000)
    game_over()





