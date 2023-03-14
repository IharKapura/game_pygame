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
        self.power = pygame.image.load(Path("images","player_fight","_bear_a_ball.png")).convert_alpha()
        self.fire_power = pygame.image.load(Path("images","player_fight","fire_bear_ball.png")).convert_alpha()

        #Текст
        font_text = pygame.font.SysFont('arial', 20)
        self.text_run = font_text.render('Press "A" go left or Press "D" go right', False, "Black")
        self.text_jump = font_text.render('Press "Space" to jump', False, "Black")
        self.text_fight = font_text.render('Press "E" to attack right and press "Q" to attack left', False, "Black")

    def update_bg(self, player, level):
        #обновление заднего фона, текстаб жизней
        self.draw(player, level)
        self.lives(player)
    

    def draw(self, player, level):
        self.screen.blit(self.bg1, (0, 0))
        #Отрисовка текста
        if 0 <= player.rect.centerx <= 160 and level.level_number == 1:
            self.screen.blit(self.text_run, (player.rect.centerx, player.rect.centery - 100))
        if 640 <= player.rect.centerx <= 815 and level.level_number == 1:
            self.screen.blit(self.text_jump, (player.rect.centerx, player.rect.centery - 100))
        if player.player_get_power and level.level_number == 4:
            self.screen.blit(self.text_fight, (player.rect.centerx, player.rect.centery - 100))
    

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
        if player.player_get_power and not player.player_fire_power:
            self.screen.blit(self.power, (10, 50))
        if player.player_fire_power:
            self.screen.blit(self.fire_power, (10, 50))


    #Размещение силы для игрока
    """ def power_for_player(self,player, bullet):
        if player.player_get_power:
            self.screen.blit(bullet.bullet_image, (450,450)) """