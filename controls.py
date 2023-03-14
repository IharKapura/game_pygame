import pygame, pathlib
import sys

from pathlib import Path
""" from player import Player """
""" from enemies import Enemies """
""" from bullet import Bullet """
""" from bg import Bg """
""" from level import Level """
""" from cube import Cube """

def events(player,bullet, level, bg, cube_power, cube, bad_cube):

    #Оброботка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            #Бег
            if event.key == pygame.K_a:
                player.left()
            if event.key == pygame.K_d:
                player.right()
            #Рывок
            if event.key == pygame.K_LCTRL:
                player.jerk_can = True
            #Прыжок
            if event.key == pygame.K_SPACE:
                player.jump(level)
            #Атака
            if event.key == pygame.K_e and player.player_get_power:
                bullet.shot_right(player)
            if event.key == pygame.K_q and player.player_get_power:
                bullet.shot_left(player)
            #Переключение силы
            if event.key == pygame.K_1 and player.player_get_fire:
                player.player_fire_power = True
                player.player_fire(bullet)
                if not player.lookright:
                    player.flip()
                    player.lookright = True
            #Рестарт и переключение уровня
            if event.key == pygame.K_r and player.player_gameover == True:
                player.player_gameover = False
                player.player_lives = 3
                if level.level_number < 8:
                    bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
                elif level.level_number >= 8:
                    bg.bg1 = pygame.image.load(Path('images','_bg','cave_level.jpg')).convert_alpha()
            if event.key == pygame.K_r and player.player_gamewin == True:
                player.player_gamewin = False
                level.level_number += 1
                level.platforms = []
                level.bad_platforms = []
                if level.level_number == 2:
                    level.level1_2()
                elif  level.level_number == 3:
                    level.level1_3()
                elif  level.level_number == 4:
                    level.level1_4()
                elif level.level_number == 5:
                    level.level1_5()
                elif level.level_number == 6:
                    level.level1_6()
                elif level.level_number == 7:
                    level.level1_7()
                elif level.level_number == 8:
                    level.level2_0(cube_power, bg, cube, bad_cube)
                player.player_lives = 3
                player.rect.centerx = player.screen_rect.centerx - 900
                player.rect.centery = player.screen_rect.centery + 450
                if level.level_number < 8:
                    bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
                elif level.level_number >= 8:
                    bg.bg1 = pygame.image.load(Path('images','_bg','cave_level.jpg')).convert_alpha()
        if event.type == pygame.KEYUP:
            #Бег
            if event.key == pygame.K_a and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_d and player.change_x > 0:
                player.stop()
            #Рывок
            if event.key == pygame.K_LCTRL:
                player.jerk_can = False


def update(screen, bg, player, enemies, bullet, level, cube, bad_cube, cube_power, enemies_scorp):
    if player.player_gameover == False or player.player_gamewin == False:
        bg.update_bg(player, level)
        bullet.update(player, level)
        enemies.update()
        enemies_scorp.update()
        cube_power.update()
        bad_cube.update()
        level.update(screen, cube, bad_cube, cube_power, enemies, enemies_scorp)
        player.draw_player()
        player.update_player(level, cube_power)
    if player.player_gameover == True:
        bg.bg1 = pygame.image.load(Path('images','gameover.png')).convert_alpha()
        bg.update_bg(player, level)
    if player.player_gamewin == True:
        bg.bg1 = pygame.image.load(Path('images','gamewin.png')).convert_alpha()
        bg.update_bg(player, level)
    if level.level_number == 0:
        level.level1_1()
        level.level_number += 1
