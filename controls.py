import pygame, pathlib
import sys

from pathlib import Path
""" from player import Player """
""" from enemies import Enemies """
""" from bullet import Bullet """
""" from bg import Bg """
""" from level import Level """
""" from cube import Cube """

def events(player,bullet, level, bg, cube_power, cube, bad_cube, menu):

    #Оброботка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        
        if event.type == pygame.KEYDOWN:
            if menu.menu_ON:
                if event.key == pygame.K_s and menu.menu_count <= 2 or event.key == pygame.K_DOWN and menu.menu_count <= 2:
                    menu.menu_count += 1
                elif event.key == pygame.K_w and menu.menu_count >= 2 or event.key == pygame.K_UP and menu.menu_count >= 2:
                    menu.menu_count -= 1
                elif event.key == pygame.K_RETURN and menu.menu_count == 1:
                    menu.menu_ON = False
                elif event.key == pygame.K_RETURN and menu.menu_count == 2:
                    menu.menu_count = 4
                elif event.key == pygame.K_ESCAPE and menu.menu_count == 4:
                    menu.menu_count = 2
                elif event.key == pygame.K_RETURN and menu.menu_count == 3 or event.key == pygame.K_ESCAPE and menu.menu_count == 3:
                    sys.exit()
            if event.key == pygame.K_ESCAPE:
                menu.menu_ON = True
            #Бег
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.left()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
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
            #Рестарт c последнего чекпоинта
            if event.key == pygame.K_r and player.player_gameover == True:
                player.player_gameover = False
                player.player_lives = 3
                if level.level_number < 5:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 2
                    level.level1_2()
                    bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
                elif 5 <= level.level_number < 8:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 5
                    level.level1_5()
                    bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
                elif 8 <= level.level_number < 10:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 8
                    level.level2_0(bg, cube, bad_cube)
                    bg.bg1 = pygame.image.load(Path('images','_bg','cave_level.jpg')).convert_alpha()
                elif 10 <= level.level_number:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 10
                    level.level2_2()
                    bg.bg1 = pygame.image.load(Path('images','_bg','cave_level.jpg')).convert_alpha()
            #Переход на следующий уровень
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
                    level.level2_0(bg, cube, bad_cube)
                elif level.level_number == 9:
                    level.level2_1(cube_power)
                elif level.level_number == 10:
                    level.level2_2()
                elif level.level_number == 11:
                    level.level2_3()
                elif level.level_number == 12:
                    level.level2_4()
                player.rect.centerx = player.screen_rect.centerx - 900
                player.rect.centery = player.screen_rect.centery + 450
                if level.level_number < 8:
                    bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
                elif level.level_number >= 8:
                    bg.bg1 = pygame.image.load(Path('images','_bg','cave_level.jpg')).convert_alpha()
        if event.type == pygame.KEYUP:
            #Бег
            if event.key == pygame.K_a and player.change_x < 0 or event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_d and player.change_x > 0 or event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()
            #Рывок
            if event.key == pygame.K_LCTRL:
                player.jerk_can = False


def update(screen, bg, player, enemies, bullet, level, cube, bad_cube, cube_power, enemies_scorp, enemies_bug, finish, lives, menu):
    if player.player_gameover == False or player.player_gamewin == False:
        if menu.menu_ON:
            menu.update()
        else:
            bg.update_bg(player, level)
            bullet.update(player, level)
            enemies.update()
            enemies_scorp.update()
            enemies_bug.update()
            cube_power.update()
            bad_cube.update()
            level.update(screen, cube, bad_cube, cube_power, enemies, enemies_scorp, enemies_bug, finish, lives)
            player.draw_player()
            player.update_player(level, cube_power)
            if player.player_gameover == True:
                bg.bg1 = pygame.image.load(Path('images','gameover.png')).convert_alpha()
                bg.update_bg(player, level)
            elif player.player_gamewin == True:
                bg.bg1 = pygame.image.load(Path('images','gamewin.png')).convert_alpha()
                bg.update_bg(player, level)
            if level.level_number == 0:
                level.level1_1()
                level.level_number += 1
