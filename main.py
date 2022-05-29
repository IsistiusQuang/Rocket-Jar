import pygame

from Display_Game import draw_surface , draw_winner , draw_gameover
from Gunship import YELLOW_SPACESHIP , RED_SPACESHIP
from List_Of_Astroids import Astroids
from Target import Prize
from Impact_Handling import PRICE_HIT , astroid_impact , bullet_impact , BULLET_FIRE_SOUND


pygame.display.set_caption("First Game")


def main():
    clock = pygame.time.Clock()
    FPS = 60

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                YELLOW_SPACESHIP.bullet(event.key,BULLET_FIRE_SOUND)
                RED_SPACESHIP.bullet(event.key,BULLET_FIRE_SOUND)

            if event.type == PRICE_HIT:
                draw_gameover()
                run = False


        keys_pressed = pygame.key.get_pressed()
        YELLOW_SPACESHIP.movement(keys_pressed)
        RED_SPACESHIP.movement(keys_pressed)

        YELLOW_SPACESHIP.handle_bullet()
        RED_SPACESHIP.handle_bullet()

        for astroid in Astroids.Astroid_list:
            bullet_impact(astroid,YELLOW_SPACESHIP)
            bullet_impact(astroid,RED_SPACESHIP)
            astroid_impact(astroid,Prize)
            if astroid.astroid_stage == 1:
                Astroids.Astroid_list.remove(astroid)
                continue
            if astroid.spawn_delay():
                continue

            if astroid.frame_count == astroid.frame_limit:
                astroid.move_count += 1
                if astroid.move_count > astroid.move_limit:
                    if astroid.obj.x + astroid.width > astroid.checkpoints[-1].high_x or astroid.obj.y < astroid.checkpoints[-1].low_y:
                        astroid.to_checkpoint()

                    else:
                        print("\t\tCheckpoint reached")
                        astroid.make_border_limit()

                else:
                    astroid.make_frame_limit()
                    astroid.checking_previous_move()

            else:
                #print(f"Astroid border limit: {astroid.current_x_limit} , {astroid.current_y_limit}")
                #print(f"Astroid frame limit: {astroid.frame_limit}")
                astroid.move()

        draw_surface()

        if len(Astroids.Astroid_list) == 0:
            if Astroids.wave_count == Astroids.wave:
                draw_winner({YELLOW_SPACESHIP.score:YELLOW_SPACESHIP.name,RED_SPACESHIP.score:RED_SPACESHIP.name})
                run =  False
            elif Astroids.wave_count < Astroids.wave:
                Astroids.next_wave()


    pygame.quit()


if __name__ == "__main__":
    main()


