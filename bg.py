import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Bg(Sprite):


    #инициализация фона
    def __init__(self, screen, player):
        super(Bg, self).__init__()
        self.screen = screen
        self.player = player
        self.bg1 = pygame.image.load(Path('images','bg','forest_bg.png')).convert_alpha()
        self.live = pygame.image.load(Path('images','player','lives.png')).convert_alpha()
        self.power = pygame.image.load(Path("images","player_fight","bear_a_ball.png")).convert_alpha()
        self.fire_power = pygame.image.load(Path("images","player_fight","fire_bear_ball.png")).convert_alpha()
        self.frozen_power = pygame.image.load(Path("images","player_fight","frozen_bear_ball.png")).convert_alpha()
        #Текст
        self.text_run = pygame.image.load(Path('images','bg','text_run.png')).convert_alpha()
        self.text_jump = pygame.image.load(Path('images','bg','text_jump.png')).convert_alpha()
        self.text_fight = pygame.image.load(Path('images','bg','text_fight.png')).convert_alpha()
        self.text_fire_power = pygame.image.load(Path('images','bg','text_fire_power.png')).convert_alpha()
        self.text_frozen_power = pygame.image.load(Path('images','bg','text_frozen_jump.png')).convert_alpha()
        self.text_can_switch = pygame.image.load(Path('images','bg','can_switch.png')).convert_alpha()

    #обновление заднего фона, текстаб жизней
    def update_bg(self, player, level):
        self.draw(player, level)
        self.lives(player)

    #отрисовка заднего фона и текста
    def draw(self, player, level):
        self.screen.blit(self.bg1, (0, 0))
        #Отрисовка текста
        if 0 <= player.rect.centerx <= 160 and level.level_number == 1:
            self.screen.blit(self.text_run, (230 , 440))
        elif 640 <= player.rect.centerx <= 815 and level.level_number == 1:
            self.screen.blit(self.text_jump, (450, 440))
        elif player.player_get_power and level.level_number == 4 and not player.player_gameover and not player.player_gamewin:
            self.screen.blit(self.text_fight, (450, 100))
        elif player.player_get_fire and level.level_number == 9 and not player.player_gameover and not player.player_gamewin:
            self.screen.blit(self.text_fire_power, (1000, 300))
        elif player.player_get_frozen and level.level_number == 15 and not player.player_gameover and not player.player_gamewin:
            self.screen.blit(self.text_frozen_power, (500, 150))
            self.screen.blit(self.text_can_switch, (1300, 550))

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
        if player.player_get_power and not player.player_fire_power and not player.player_frozen_power:
            self.screen.blit(self.power, (10, 50))
        elif player.player_fire_power and not player.player_frozen_power:
            self.screen.blit(self.fire_power, (10, 50))
        elif player.player_frozen_power and not player.player_fire_power:
            self.screen.blit(self.frozen_power, (10, 50))

    #Изменение фона на уровень пещера
    def change_bg_cave(self):
        self.bg1 = pygame.image.load(Path('images','bg','cave_level.jpg')).convert_alpha()

    #Изменение фона на уровень ледяной
    def change_bg_frozen(self):
        self.bg1 = pygame.image.load(Path('images','bg','frozen_level.jpg')).convert_alpha()

    #Изменение фона на уровень поля
    def change_bg_field(self):
        self.bg1 = pygame.image.load(Path('images','bg','field.png')).convert_alpha()