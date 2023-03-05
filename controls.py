import pygame, pathlib
import sys

from pathlib import Path
""" from player import Player """
""" from enemies import Enemies """
""" from bullet import Bullet """
""" from bg import Bg """
""" from level import Level """
""" from cube import Cube """

def events(player,bullet, level, bg):

    #Оброботка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left()
            if event.key == pygame.K_d:
                player.right()
            if event.key == pygame.K_SPACE:
                player.jump(level)
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
                player.player_lives = 3
                player.rect.centerx = player.screen_rect.centerx - 900
                player.rect.centery = player.screen_rect.centery + 450
                bg.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_d and player.change_x > 0:
                player.stop()


def update(screen, bg, player, enemies, bullet, level, cube):
    if player.player_gameover == False or player.player_gamewin == False:
        #обновление экрана
        bg.update_bg(player)
        #bg.change_screen(player)
        #level.update()
        #player.collide(level)
        level.draw(screen, cube)
        bullet.update(player)
        #level.update(screen, cube)
        #bullet.shot(player)
        #enemies.update()
        #enemies.update_enemies()
        #level.draw(screen, bg)
        player.draw_player()
        player.update_player(level, )
        #enemies.draw_enemies()
        #pygame.display.flip()
    if player.player_gameover == True:
        bg.bg1 = pygame.image.load(Path('images','gameover.png')).convert_alpha()
        bg.update_bg(player)
    if player.player_gamewin == True:
        bg.bg1 = pygame.image.load(Path('images','gamewin.png')).convert_alpha()
        bg.update_bg(player)





    




""" def collision(screen, player, enemies, bullet, level):
    # столкновения
    ...
    if level.rect.colliderect(player.rect):
        if player.change_x > 0:
            player.rect.right = level.cube_list.rect.left
        if player.change_x < 0:
            player.rect.left = level.cube_list.rect.right
        if player.change_y > 0:
            player.rect.bottom = level.cube_list.rect.top
            player.change_y = 0
        if player.change_y <0:
            player.rect.top = level.cube_list.rect.bottom """
