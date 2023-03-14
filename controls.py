import pygame, pathlib
import sys

from pathlib import Path
""" from player import Player """
""" from enemies import Enemies """
""" from bullet import Bullet """
""" from bg import Bg """
""" from level import Level """
""" from cube import Cube """

def events(player,bullet, level, bg, screen):

    #Оброботка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_a:
                player.left()
            if event.key == pygame.K_d:
                player.right()
            if event.key == pygame.K_LCTRL:
                player.jerk_can = True
            if event.key == pygame.K_SPACE:
                player.jump(level)
            if event.key == pygame.K_e and player.player_get_power:
                bullet.shot_right(player)
            if event.key == pygame.K_q and player.player_get_power:
                bullet.shot_left(player)
            if event.key == pygame.K_1 and player.player_get_fire:
                player.player_fire_power = True
                player.player_fire(bullet)
            if event.key == pygame.K_r and player.player_gameover == True:
                player.player_gameover = False
                player.player_lives = 3
                bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
            if event.key == pygame.K_r and player.player_gamewin == True:
                player.player_gamewin = False
                level.level_number += 1
                level.platforms = []
                level.bad_platforms = []
                if level.level_number == 2:
                    level.level1_2()
                if  level.level_number == 3:
                    level.level1_3()
                if  level.level_number == 4:
                    level.level1_4()
                if level.level_number == 5:
                    level.level1_5()
                if level.level_number == 6:
                    level.level1_6()
                player.player_lives = 3
                player.rect.centerx = player.screen_rect.centerx - 900
                player.rect.centery = player.screen_rect.centery + 450
                bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_d and player.change_x > 0:
                player.stop()
            if event.key == pygame.K_LCTRL:
                player.jerk_can = False


def update(screen, bg, player, enemies, bullet, level, cube, bad_cube, cube_power, enemies_scorp):
    if player.player_gameover == False or player.player_gamewin == False:
        #обновление экрана
        bg.update_bg(player, level)
        bullet.update(player, level)
        #bg.change_screen(player)
        #player.collide(level)
        #level.update(screen, cube)
        #level.draw(screen, cube)
        enemies.update()
        enemies_scorp.update()
        level.update(screen, cube, bad_cube, cube_power, enemies, enemies_scorp)
        #bullet.shot(player)
        #enemies.update_enemies()
        #level.draw(screen, bg)
        #collision(player, level)
        player.draw_player()
        player.update_player(level, cube_power)
        #enemies.draw_enemies()
        #pygame.display.flip()
    if player.player_gameover == True:
        bg.bg1 = pygame.image.load(Path('images','gameover.png')).convert_alpha()
        bg.update_bg(player, level)
    if player.player_gamewin == True:
        bg.bg1 = pygame.image.load(Path('images','gamewin.png')).convert_alpha()
        bg.update_bg(player, level)
    if level.level_number == 0:
        level.level1_6()
        level.level_number += 1










""" def collision(player, level):
    # столкновения
    bad_hit_list = pygame.sprite.spritecollide(player, level.bad_platforms, False)
    for block in bad_hit_list:
            if player.rect.colliderect(block.rect):
                self.rect.centerx = self.screen_rect.centerx - coor_x
                self.rect.centery = self.screen_rect.centery + coor_y
                player.player_lives -= 1

                print("YES")
                print(player.player_lives)
            elif player.rect.left == block.rect.right:
                player.player_lives -= 1 """