import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Lives(Sprite):
	#Инициализация кубов жизни
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = pygame.image.load(Path('images','player','lives.png'))
		self.rect = pygame.Rect(x, y, 25, 25)

	
