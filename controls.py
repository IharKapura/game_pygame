import pygame
import sys
from pathlib import Path

#Отслеживание событий
def events(screen, player, bullet, level, bg, cube_power, cube, bad_cube, menu, sounds):

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
            if event.key == pygame.K_LCTRL and player.player_fire_power:
                sounds.jerk_fire()
                player.jerk_can = True
            #Прыжок
            if event.key == pygame.K_SPACE:
                sounds.sound_jump()
                player.jump(level)
                if player.player_frozen_power:
                    cube_power.jump = True
            #Атака
            if event.key == pygame.K_e and player.player_get_power:
                sounds.sound_shot()
                bullet.shot_right(player)
            if event.key == pygame.K_q and player.player_get_power:
                sounds.sound_shot()
                bullet.shot_left(player)
            #Переключение силы
            if event.key == pygame.K_1 and player.player_get_fire:
                sounds.set_fire_power()
                player.player_fire_power = True
                player.player_frozen_power = False
                player.player_fire(bullet)
            if event.key == pygame.K_2 and player.player_get_frozen:
                sounds.set_fire_power()
                player.player_fire_power = False
                player.player_frozen_power = True
                player.player_frozen(bullet)
            #Рестарт c последнего чекпоинта
            if event.key == pygame.K_r and player.player_gameover:
                player.player_gameover = False
                player.player_lives = 3
                if level.level_number < 5:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 2
                    level.level1_2()
                    bg.bg1 = pygame.image.load(Path('images','bg','forest_bg.png')).convert_alpha()
                elif 5 <= level.level_number < 8:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 5
                    level.level1_5()
                    bg.bg1 = pygame.image.load(Path('images','bg','forest_bg.png')).convert_alpha()
                elif 8 <= level.level_number < 10:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 8
                    level.level2_0(bg, cube, bad_cube)
                    bg.bg1 = pygame.image.load(Path('images','bg','cave_level.jpg')).convert_alpha()
                elif 10 <= level.level_number < 14:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 10
                    level.level2_2()
                    bg.bg1 = pygame.image.load(Path('images','bg','cave_level.jpg')).convert_alpha()
                elif 14 <= level.level_number < 16:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 14
                    level.level2_6(bg, cube, bad_cube)
                    bg.bg1 = pygame.image.load(Path('images','bg','frozen_level.jpg.')).convert_alpha()
                elif 16 <= level.level_number < 19:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 16
                    level.level2_8()
                    bg.bg1 = pygame.image.load(Path('images','bg','frozen_level.jpg.')).convert_alpha()
                elif 19 <= level.level_number < 22:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 19
                    level.level3_1(bg, cube, bad_cube)
                    bg.bg1 = pygame.image.load(Path('images','bg','field.png.')).convert_alpha()
                elif 22 <= level.level_number:
                    level.platforms = []
                    level.bad_platforms = []
                    level.level_number = 22
                    level.level3_4()
                    bg.bg1 = pygame.image.load(Path('images','bg','field.png.')).convert_alpha()
            #Переход на следующий уровень
            if event.key == pygame.K_r and player.player_gamewin:
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
                    sounds.music_count = 1
                    level.level2_0(bg, cube, bad_cube)
                elif level.level_number == 9:
                    level.level2_1(cube_power)
                elif level.level_number == 10:
                    level.level2_2()
                elif level.level_number == 11:
                    level.level2_3()
                elif level.level_number == 12:
                    level.level2_4()
                elif level.level_number == 13:
                    level.level2_5()
                elif level.level_number == 14:
                    level.level2_6(bg, cube, bad_cube)
                elif level.level_number == 15:
                    level.level2_7(cube_power)
                elif level.level_number == 16:
                    level.level2_8()
                elif level.level_number == 17:
                    level.level2_9()
                elif level.level_number == 18:
                    level.level3_0()
                elif level.level_number == 19:
                    level.level3_1(bg, cube, bad_cube)
                elif level.level_number == 20:
                    level.level3_2()
                elif level.level_number == 21:
                    level.level3_3()
                elif level.level_number == 22:
                    level.level3_4()
                player.rect.centerx = player.screen_rect.centerx - 900
                player.rect.centery = player.screen_rect.centery + 450
                if level.level_number < 8:
                    bg.bg1 = pygame.image.load(Path('images','bg','forest_bg.png')).convert_alpha()
                elif 14 > level.level_number >= 8:
                    bg.bg1 = pygame.image.load(Path('images','bg','cave_level.jpg')).convert_alpha()
                elif 19 > level.level_number >= 14:
                    bg.bg1 = pygame.image.load(Path('images','bg','frozen_level.jpg')).convert_alpha()
                elif level.level_number >= 19:
                    bg.bg1 = pygame.image.load(Path('images','bg','field.png')).convert_alpha()
        if event.type == pygame.KEYUP:
            #Бег
            if event.key == pygame.K_a and player.change_x < 0 or event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_d and player.change_x > 0 or event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()
            if event.key == pygame.K_SPACE:
                if player.player_frozen_power:
                    cube_power.jump = False
            #Рывок
            if event.key == pygame.K_LCTRL:
                player.jerk_can = False

#Обновление всех объектов
def update(screen, bg, player, enemies, bullet, level, cube, bad_cube, cube_power, enemies_scorp, enemies_bug, finish, lives, menu, sounds, tablet):
    if not player.player_gameover or not player.player_gamewin:
        if menu.menu_ON:
            menu.update()
            sounds.play_music_bg()
        else:
            sounds.menu.stop()
            bg.update_bg(player, level)
            bullet.update(player, level, sounds)
            enemies.update()
            enemies_scorp.update()
            enemies_bug.update()
            cube_power.update(screen, player)
            bad_cube.update()
            level.update(screen, cube, bad_cube, cube_power, enemies, enemies_scorp, enemies_bug, finish, lives, tablet)
            player.draw_player()
            player.update_player(level, cube_power, sounds, tablet)
            if player.player_gameover:
                bg.bg1 = pygame.image.load(Path('images','gameover.png')).convert_alpha()
                bg.update_bg(player, level)
            elif player.player_gamewin:
                bg.bg1 = pygame.image.load(Path('images','gamewin.png')).convert_alpha()
                bg.update_bg(player, level)
            if level.level_number == 0:
                level.level1_1()
                level.level_number += 1
