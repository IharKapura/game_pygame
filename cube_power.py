import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class CubePower (Sprite):


	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = pygame.image.load(Path('images','level1_image','cube_for_power_with_ball.png'))
		self.rect = pygame.Rect(x, y, 40, 40)

	#Изменение картинки плохих кубов для уровня пещера
	def change_cube_power(self):
		self.image = pygame.image.load(Path('images','level1_image','cube_for_power.png'))