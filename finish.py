import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Finish(Sprite):
		
	#Инициализация кубов для завершения уровня
	def __init__(self, x, y):
		Sprite.__init__(self)		
		self.image = pygame.image.load(Path('images','bg','finish.png'))
		self.rect = pygame.Rect(x, y, 62, 63)

