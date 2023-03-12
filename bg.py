import pygame, pathlib
from pathlib import Path
""" from player import Player """
from pygame.sprite import Sprite
from pygame.sprite import Group


class Bg(Sprite):


    def __init__(self, screen, player):
        #инициализация фона
        super(Bg, self).__init__()
        self.screen = screen
        self.player = player
        self.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
        self.live = pygame.image.load(Path('images','player','lives.png')).convert_alpha()

        #Текст
        font_text = pygame.font.SysFont('arial', 40)
        self.text_run = font_text.render('Press "A" go left or Press "D" go right', False, "Black")
        self.text_jump = font_text.render('Press "Space" to jump', False, "Black")

    def update_bg(self, player, level):
        #обновление заднего фона, текстаб жизней
        self.draw(player, level)
        self.lives(player)
    

    def draw(self, player, level):
        self.screen.blit(self.bg1, (0, 0))
        #Отрисовка текста
        if 0 <= player.rect.centerx <= 160 and level.level_number == 1:
            self.screen.blit(self.text_run, (100, 0))
        if 640 <= player.rect.centerx <= 815 and level.level_number == 1:
            self.screen.blit(self.text_jump, (100, 0))
    

    #Счетчик жизней
    def lives(self, player):
        if player.player_lives == 3:
            self.screen.blit(self.live, (10,10))
            self.screen.blit(self.live, (40,10))
            self.screen.blit(self.live, (70,10))
        elif player.player_lives == 2:
            self.screen.blit(self.live, (10,10))
            self.screen.blit(self.live, (40,10))
        elif player.player_lives == 1:
            self.screen.blit(self.live, (10,10))


    #Размещение силы для игрока
    def power_for_player(self, bullet):
        """ bullet.bullet_rect.centerx = 450
        bullet.bullet_rect.centery = 450 """
        self.screen.blit(bullet.bullet_image, (450,450))