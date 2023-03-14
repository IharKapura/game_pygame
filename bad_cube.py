import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class BadCube (Sprite):


	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = pygame.image.load(Path('images','level1_image','cube_w_spike.png'))
		self.rect = pygame.Rect(x + 10 , y + 20, 63, 63)

	#Изменение картинки плохих кубов для уровня пещера
	def change_cube_cave(self):
		self.image = pygame.image.load(Path('images','level2','cube_cave.png'))