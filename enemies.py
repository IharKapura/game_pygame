import pygame, random, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class Enemies(Sprite):


    def __init__(self, screen):
        #инициализация врагов
        super(Enemies, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(Path("images","enemies","_bower_r_st.png")).convert_alpha()
        self.rect = self.image.get_rect() 
        self.rect.centerx = random.randrange( 1920  - self.rect.width)
        self.speedy = random.randrange(1, 8)
        self.rect.centery = self.screen_rect.centery + 420
        self.change_x = 0
        self.change_y = 0

    def update(self):
        #обновление позиции врагов
        #self.rect.centerx += self.change_x
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
    
    def draw_enemies(self):
    #Отрисовка врагов
        self.screen.blit(self.image, self.rect)

    def enemies_del(self, player):
        self.image = pygame.image.load(Path("images","enemies","_bower_l_a4.png")).convert_alpha()
        player.change_x = 0