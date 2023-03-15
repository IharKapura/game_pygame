import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class BadCube (Sprite):


	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = pygame.image.load(Path('images','level1_image','cube_w_spike.png'))
		self.rect = pygame.Rect(x + 20, y + 10, 33, 33)
		self.anim_count = False
		self.tick = 0

	#Изменение картинки плохих кубов для уровня пещера
	def change_bad_cube_cave(self):
		self.image = []
		self.image = [
			pygame.image.load(Path('images','level2','cube_fire_1.png')).convert_alpha(),
			pygame.image.load(Path('images','level2','cube_fire_2.png')).convert_alpha(),
			pygame.image.load(Path('images','level2','cube_fire_3.png')).convert_alpha(),
			pygame.image.load(Path('images','level2','cube_fire_4.png')).convert_alpha(),
			pygame.image.load(Path('images','level2','cube_fire_5.png')).convert_alpha(),
			pygame.image.load(Path('images','level2','cube_fire_6.png')).convert_alpha(),
					]
		
		


	def update(self):
		self.anim_cube()


	def anim_cube(self):
		if self.tick == 30:
			self.tick = 0
		else:
			self.tick += 1
		if self.tick == 0:
			self.anim_count = 0
		elif self.tick == 5:
			self.anim_count = 1
		elif self.tick == 10:
			self.anim_count = 2
		elif self.tick == 15:
			self.anim_count = 3
		elif self.tick == 20:
			self.anim_count = 4
		elif self.tick == 25:
			self.anim_count = 5