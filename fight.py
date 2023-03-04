import pygame
import sys
from player import Player
from enemies import Enemies
from pygame.sprite import Sprite
from bg import Bg


class Fight(Sprite):


    def __init__(self,screen):
        #инициализация боя
        super(Fight, self).__init__()
        self.screen = screen
