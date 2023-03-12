import pygame, random, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class Enemies (Sprite):


    def __init__(self, x, y):
        #инициализация врагов
        Sprite.__init__(self)
        self.image = [
            pygame.image.load(Path("images","enemies","enemies_1.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","enemies_2.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","enemies_3.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","enemies_4.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","enemies_5.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","enemies_6.png")).convert_alpha(),
        ]
        self.rect = pygame.Rect(x , y, 68, 65)
        self.anim_count = False
        self.tick = 0


    #Обновление врагов
    def update(self):
        self.anim_enem()


    #Анимация врагов
    def anim_enem(self):
        if self.tick == 200:
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
        elif self.tick == 133:
            self.anim_count = 4
        elif self.tick == 166:
            self.anim_count = 5
