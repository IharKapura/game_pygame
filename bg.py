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
        self.text_run = pygame.image.load(Path('images','_bg','text_run.png')).convert_alpha()
        self.text_jump = pygame.image.load(Path('images','_bg','text_jump.png')).convert_alpha()
        self.text_fight = pygame.image.load(Path('images','_bg','text_fight.png')).convert_alpha()
        self.text_fire_power = pygame.image.load(Path('images','_bg','text_fire_power.png')).convert_alpha()

    def update_bg(self, player, level):
        #обновление заднего фона, текстаб жизней
        self.draw(player, level)
        self.lives(player)
    

    def draw(self, player, level):
        self.screen.blit(self.bg1, (0, 0))
        #Отрисовка текста
        if 0 <= player.rect.centerx <= 160 and level.level_number == 1:
            self.screen.blit(self.text_run, (230 , 440))
        elif 640 <= player.rect.centerx <= 815 and level.level_number == 1:
            self.screen.blit(self.text_jump, (450, 440))
        elif player.player_get_power and level.level_number == 4 and player.player_gameover == False and player.player_gamewin == False:
            self.screen.blit(self.text_fight, (450, 300))
        elif player.player_get_fire and level.level_number == 9 and player.player_gameover == False and player.player_gamewin == False:
            self.screen.blit(self.text_fire_power, (1000, 300))
    

    #Счетчик жизней
    def lives(self, player):
        if player.player_lives == 5:
            self.screen.blit(self.live, (10,10))
            self.screen.blit(self.live, (40,10))
            self.screen.blit(self.live, (70,10))
            self.screen.blit(self.live, (100,10))
            self.screen.blit(self.live, (130,10))
        elif player.player_lives == 4:
            self.screen.blit(self.live, (10,10))
            self.screen.blit(self.live, (40,10))
            self.screen.blit(self.live, (70,10))
            self.screen.blit(self.live, (100,10))
        elif player.player_lives == 3:
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
    def change_bg_cave(self):
        self.bg1 = pygame.image.load(Path('images','_bg','cave_level.jpg')).convert_alpha()