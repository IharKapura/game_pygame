import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite



class Lives(Sprite):
	
	
	def __init__(self, x, y):
		# инициализация кубов
		Sprite.__init__(self)
		
		#Куб
		self.image = pygame.image.load(Path('images','player','lives.png'))
		self.rect = pygame.Rect(x, y, 25, 25)

	
