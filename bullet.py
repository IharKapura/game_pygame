import pygame, pathlib
from pathlib import Path
#from player import Player
from pygame.sprite import Sprite


class Bullet(Sprite):


    def __init__(self, screen, player):
        #инициализация пули
        super(Bullet, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.player = player
        self.bullets = []
        self.bullet_image = pygame.image.load(Path("images","player_fight","_bear_a_ball.png")).convert_alpha()
        self.bullet_rect = self.bullet_image.get_rect()
        self.change_x = 0

    def update(self, player):

        keys = pygame.key.get_pressed()

        if self.bullets:
            for (i, el) in enumerate(self.bullets):
                    self.screen.blit(self.bullet_image, (el.x, el.y))
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
        self.bullets.append(self.bullet_image.get_rect(center = (player.rect.centerx , player.rect.centery - 10)))

    def shot_left(self, player):
        #Бросок меда
        self.change_x = -25
        self.bullets.append(self.bullet_image.get_rect(center = (player.rect.centerx , player.rect.centery - 10)))
        

        