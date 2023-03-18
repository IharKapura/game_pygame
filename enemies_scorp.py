import pygame
from pathlib import Path
from pygame.sprite import Sprite


class EnemiesScorp (Sprite):

    #инициализация врагов скорпионов
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = [
            pygame.image.load(Path("images","enemies","scorp_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","scorp_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","scorp_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","scorp_l_4.png")).convert_alpha(),
        ]
        self.rect = pygame.Rect(x , y, 68, 49)
        self.anim_count = False
        self.tick = 0

    #Обновление врагов скорпионов
    def update(self):
        self.anim_enem()

    #Анимация врагов скорпионов
    def anim_enem(self):
        if self.tick == 133:
            self.tick = 0
        else:
            self.tick += 1
        if self.tick == 0:
            self.anim_count = 0
        elif self.tick == 33:
            self.anim_count = 1
        elif self.tick == 66:
            self.anim_count = 2
        elif self.tick == 99:
            self.anim_count = 3

