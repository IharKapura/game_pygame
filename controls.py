import pygame, pathlib
import sys

from pathlib import Path
""" from player import Player """
""" from enemies import Enemies """
""" from bullet import Bullet """
""" from bg import Bg """
""" from level import Level """
""" from cube import Cube """

def events(player,bullet, level, bg, cube):

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
            if event.key == pygame.K_SPACE:
                player.jump(level)
            if event.key == pygame.K_LCTRL:
                player.jerk(level)
            if event.key == pygame.K_e:
                bullet.shot_right(player)
            if event.key == pygame.K_q:
                bullet.shot_left(player)
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
                    cube.change_cube_cave()
                    level.level1_3()
                if  level.level_number == 4:
                    level.level1_4()
                player.player_lives = 3
                player.rect.centerx = player.screen_rect.centerx - 900
                player.rect.centery = player.screen_rect.centery + 450
                bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_d and player.change_x > 0:
                player.stop()
            if event.key == pygame.K_LSHIFT:
                player.stop()


def update(screen, bg, player, enemies, bullet, level, cube, bad_cube):
    if player.player_gameover == False or player.player_gamewin == False:
        #обновление экрана
        bg.update_bg(player, level)
        #bg.change_screen(player)
        #player.collide(level)
        #level.update(screen, cube)
        #level.draw(screen, cube)
        level.update(screen, cube, bad_cube)
        bullet.update(player)
        #bullet.shot(player)
        #enemies.update()
        #enemies.update_enemies()
        #level.draw(screen, bg)
        #collision(player, level)
        player.draw_player()
        player.update_player(level)
        #enemies.draw_enemies()
        #pygame.display.flip()
    if player.player_gameover == True:
        bg.bg1 = pygame.image.load(Path('images','gameover.png')).convert_alpha()
        bg.update_bg(player, level)
    if player.player_gamewin == True:
        bg.bg1 = pygame.image.load(Path('images','gamewin.png')).convert_alpha()
        bg.update_bg(player, level)
    if level.level_number == 0:
        level.level1()
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