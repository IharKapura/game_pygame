import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite



class Finish(Sprite):
	
	
	def __init__(self, x, y):
		# инициализация кубов
		Sprite.__init__(self)
		
		#Конец уровня
		self.image = pygame.image.load(Path('images','_bg','finish.png'))
		self.rect = pygame.Rect(x, y, 62, 63)

