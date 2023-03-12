import pygame, pathlib
from pathlib import Path
#from player import Player
from pygame.sprite import Sprite


class Bullet(Sprite):


    def __init__(self, screen, player):
        #инициализация пули
        super(Bullet, self).__init__()
        self.screen = screen
        self.bullets = []
        self.image = pygame.image.load(Path("images","player_fight","_bear_a_ball.png")).convert_alpha()
        self.rect = pygame.Rect(0, 0, 30, 32)
        self.change_x = 0
        self.x = player.rect.x
        self.y = player.rect.y

    def update(self, player, level, enemies):
        self.draw_bullet(player)
        self.kill_enemies(level, enemies)

        if self.bullets:
            for (i, el) in enumerate(self.bullets):
                    self.rect = pygame.Rect(el.x, el.y, 30, 32)
                    el.x += self.change_x

            if i > 1:
                self.bullets.pop(i)
            elif el.x > (player.rect.centerx + 200):
                self.bullets.pop(i)
            elif el.x < (player.rect.centerx - 200):
                self.bullets.pop(i)
            



    def draw_bullet(self, player):
        if self.bullets:
            for (i, el) in enumerate(self.bullets):
                    self.screen.blit(self.image, (el.x, el.y))
                    el.x += self.change_x

            if i > 1:
                self.bullets.pop(i)
            elif el.x > (player.rect.centerx + 200):
                self.bullets.pop(i)
            elif el.x < (player.rect.centerx - 200):
                self.bullets.pop(i)
     



    def shot_right(self, player):
        #Бросок меда
        self.change_x = 25
        self.bullets.append(self.image.get_rect(center = (player.rect.centerx , player.rect.centery)))

    def shot_left(self, player):
        #Бросок меда
        self.change_x = -25
        self.bullets.append(self.image.get_rect(center = (player.rect.centerx , player.rect.centery)))
        

    def kill_enemies(self, level, enemies):
        bullet_hit_list = pygame.sprite.spritecollide(self, level.enemies, False)
        for enem in bullet_hit_list:
            for el in level.enemies:
                if self.rect.colliderect(enem.rect):
                    level.enemies.remove(el)



