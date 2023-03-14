import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class CubePower (Sprite):


	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = [
			pygame.image.load(Path('images','_bg','power_ball_1.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_2.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_3.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_4.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_5.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_6.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_7.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_8.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_9.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_ball_10.png')).convert_alpha(),
		]
		self.rect = pygame.Rect(x, y, 284, 286)
		self.fire = False
		self.anim_count = False
		self.tick = 0

	def update(self):
		self.anim_cube()


	def anim_cube(self):
		if self.tick == 100:
			self.tick = 0
		else:
			self.tick += 1
		if self.tick == 0:
			self.anim_count = 0
		elif self.tick == 10:
			self.anim_count = 1
		elif self.tick == 20:
			self.anim_count = 2
		elif self.tick == 30:
			self.anim_count = 3
		elif self.tick == 40:
			self.anim_count = 4
		elif self.tick == 50:
			self.anim_count = 5
		elif self.tick == 60:
			self.anim_count = 6
		elif self.tick == 70:
			self.anim_count = 7
		elif self.tick == 80:
			self.anim_count = 8
		elif self.tick == 90:
			self.anim_count = 9


	#Изменение картинки плохих кубов для уровня пещера
	def change_cube_power(self):
		self.image = [
			pygame.image.load(Path('images','_bg','power_1.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_2.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_3.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_4.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_5.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_6.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_7.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_8.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_9.png')).convert_alpha(),
			pygame.image.load(Path('images','_bg','power_10.png')).convert_alpha(),
		]

	def change_fire_power(self):
		self.fire = True
		self.image = pygame.image.load(Path("images","player_fight","fire_bear_ball.png")).convert_alpha()