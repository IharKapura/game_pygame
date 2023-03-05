import pygame
import sys
""" from player import Player """
""" from enemies import Enemies """
""" from bullet import Bullet """
""" from bg import Bg """
""" from level import Level """
""" from cube import Cube """

def events(player,bullet, level):

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_d and player.change_x > 0:
                player.stop()


def update(screen, bg, player, enemies, bullet, level, cube):
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
    player.update_player(level)
    #enemies.draw_enemies()
    pygame.display.flip()





    




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
