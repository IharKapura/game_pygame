import pygame, random, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class Enemies (Sprite):


    def __init__(self, x, y):
        #инициализация врагов
        Sprite.__init__(self)

        self.image = pygame.image.load(Path("images","enemies","_bower_r_st.png")).convert_alpha()
        self.rect = pygame.Rect(x , y, 122, 139)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        ...
    """ def gravitation(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

		# Если уже на земле, то ставим позицию Y как 0
        if self.rect.y >= 1040 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 1040 - self.rect.height """
    

    def enemies_del(self):
        self.image = pygame.image.load(Path("images","enemies","_bower_l_a4.png")).convert_alpha()
