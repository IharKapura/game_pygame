import pygame, random, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class EnemiesBug (Sprite):


    def __init__(self, x, y):
        #инициализация врагов
        Sprite.__init__(self)
        self.image = [
            pygame.image.load(Path("images","enemies","bug_1.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","bug_2.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","bug_3.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","bug_4.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","bug_5.png")).convert_alpha(),
            pygame.image.load(Path("images","enemies","bug_6.png")).convert_alpha(),
        ]
        self.rect = pygame.Rect(x - 10, y + 10 , 77, 35)
        self.change_x = False
        self.anim_count = False
        self.tick = 0
        self.tick_move = 0


    #Обновление врагов
    def update(self):
        self.anim_enem()
        self.move()

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


    def move(self):
        
        if self.tick_move == 100: 
            self.tick_move = 0
        else:
            self.tick_move += 1
        if 0 <= self.tick_move < 50:
            self.change_x += 10
        elif 50 <= self.tick_move < 100:
            self.change_x -= 10
