import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Boss(Sprite):
    #инициализация врагов
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = [
            pygame.image.load(Path("images","bees","boss_bees.png")).convert_alpha(),
            pygame.image.load(Path("images","bees","boss_dead.png")).convert_alpha(),
        ]
        self.rect = pygame.Rect(x, y, 156, 309)
        self.lives = 100
        self.dead = False

    #Обновление босса
    def update(self):
        self.dead_boss()

    #Смерть босса
    def dead_boss(self):
        if self.lives <= 0:
            self.dead = True

