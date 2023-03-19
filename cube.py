import pygame
from pathlib import Path
from pygame.sprite import Sprite



class Cube(Sprite):
		
	# Инициализация кубов
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = pygame.image.load(Path('images','level1_image','cube_forest.png'))
		self.rect = pygame.Rect(x, y, 73, 73)
	
	# Изменения картинки куба для уровня пещера
	def change_cube_cave(self):
		self.image = pygame.image.load(Path('images','level2','cube_cave.png'))

	# Изменения картинки куба для ледянного уровня
	def change_cube_frozen(self):
		self.image = pygame.image.load(Path('images','level3','frozen_cube.png'))

	# Изменения картинки куба для ледянного уровня
	def change_cube_field(self):
		self.image = pygame.image.load(Path('images','level4','cube_field.png'))