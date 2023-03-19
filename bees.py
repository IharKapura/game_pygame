import pygame
from random import randint
from pathlib import Path
from pygame.sprite import Sprite


class Bees(Sprite):

    #инициализация врагов
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = [
            pygame.image.load(Path("images","bees","bees_1.png")).convert_alpha(),
            pygame.image.load(Path("images","bees","bees_2.png")).convert_alpha(),
            pygame.image.load(Path("images","bees","bees_3.png")).convert_alpha(),
            pygame.image.load(Path("images","bees","bees_4.png")).convert_alpha(),
            pygame.image.load(Path("images","bees","bees_5.png")).convert_alpha(),
            pygame.image.load(Path("images","bees","bees_6.png")).convert_alpha(),
        ]
        self.rect = pygame.Rect(x, y, 64, 57)
        self.image_count = randint(0, 5)
        self.change_x = randint(600, 1100)
        self.change_y = 100
        self.speed_x = randint(-5, 5)
        self.speed_y = randint(10, 20)


    def update(self, player, sounds, boss):
        self.change_x += self.speed_x
        self.change_y += self.speed_y
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (-100 > self.rect.x or self.rect.x > 2000 or self.rect.y > 1100) and boss.lives > 100:
            self.speed_x = randint(-5, 5)
            self.speed_y = randint(15, 25)
            self.change_x = randint(400, 1200)
            self.change_y = 0
            self.rect.x = self.change_x
            self.rect.y = 0
            self.image_count = randint(0, 5)
        elif (-100 > self.rect.x or self.rect.x > 2000 or self.rect.y > 1100) and boss.lives < 100:
            self.speed_x = randint(-5, 5)
            self.speed_y = randint(15, 25)
            self.change_x = randint(400, 1200)
            self.change_y = 0
            self.rect.x = self.change_x
            self.rect.y = 0
            self.image_count = randint(0, 5)
        if self.rect.colliderect(player.rect):
                self.speed_x = randint(-10, 10)
                self.speed_y = randint(10, 20)
                self.change_x = randint(400, 1200)
                self.change_y = 0
                self.rect.x = self.change_x
                self.rect.y = 0
                self.image_count = randint(0, 5)
                sounds.dead()
                self.rect.centery -= 10
                player.player_lives -= 1
                if player.lookright:
                    player.rect.centerx -= 30
                if not player.lookright:
                    player.rect.centerx += 30