import pygame
from pygame.sprite import Sprite

class Cube(Sprite):
	
	
	def __init__(self, x, y):
		# инициализация кубов
		Sprite.__init__(self)
		self.image = pygame.Surface((77,77))
		self.image = pygame.image.load('images/level1_image\cube_forest.png')
		self.rect = pygame.Rect(x, y, 77, 77)
		self.image1 = pygame.image.load('images/level1_image\cube_w_spike.png')
