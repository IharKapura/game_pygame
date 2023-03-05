import pygame, pathlib
from pathlib import Path
from player import Player
from pygame.sprite import Sprite


class Bg(Sprite):


    def __init__(self, screen, player):
        #инициализация фона
        super(Bg, self).__init__()
        self.screen = screen
        self.player = player
        self.bg1 = pygame.image.load(Path('images','_bg','forest_bg.png')).convert_alpha()
        self.bg_clouds = [
            pygame.image.load(Path('images','_bg','облака_1.png')).convert_alpha(),
            pygame.image.load(Path('images','_bg','облака_2.png')).convert_alpha(),
            pygame.image.load(Path('images','_bg','облака_3.png')).convert_alpha(),
            pygame.image.load(Path('images','_bg','облака_4.png')).convert_alpha(),
            pygame.image.load(Path('images','_bg','облака_5.png')).convert_alpha(),
        ]
        self.bg_tree = [
            pygame.image.load(Path('images','_bg','_tree_1.png')).convert_alpha(),
            pygame.image.load(Path('images','_bg','_tree_2.png')).convert_alpha(),
            pygame.image.load(Path('images','_bg','_tree_3.png')).convert_alpha(),
            pygame.image.load(Path('images','_bg','_tree_4.png')).convert_alpha(),
        ]
        self.bg_count = 0
        self.bg_x = 0

    def update_bg(self, player):
        #Отрисовка и обновление экрана 
        #self.change_screen(player)    
        self.draw()
    

    def draw(self):
        self.screen.blit(self.bg1, (self.bg_x, 0))

    def change_screen(self, player):
        if 1900 <= player.rect.centerx >= 1920:
            print('YES')
            self.bg_x = -1920
