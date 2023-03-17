import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite
from pygame.sprite import Group


class Menu(Sprite):


    def __init__(self, screen):
        self.screen = screen
        self.menu_play = pygame.image.load(Path('images','menu_play.png')).convert_alpha()
        self.menu_controls = pygame.image.load(Path('images','menu_controls.png')).convert_alpha()
        self.menu_quit = pygame.image.load(Path('images','menu_quit.png')).convert_alpha()
        self.controls = pygame.image.load(Path('images','controls.png')).convert_alpha()
        self.menu_count = 1
        self.menu_ON = True

    
    def update(self):
        self.draw()


    def draw(self):
        if self.menu_count == 1:
            self.screen.blit(self.menu_play, (0, 0))
        elif self.menu_count == 2:
            self.screen.blit(self.menu_controls, (0, 0))
        elif self.menu_count == 3:
            self.screen.blit(self.menu_quit, (0, 0))
        elif self.menu_count == 4:
            self.screen.blit(self.controls, (0, 0))





    