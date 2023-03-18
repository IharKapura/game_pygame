import pygame
from pathlib import Path
from pygame.sprite import Sprite


class CubePower (Sprite):

	#Инициализация куба силы
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = [
			pygame.image.load(Path('images','bg','power_ball_1.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_2.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_3.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_4.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_5.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_6.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_7.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_8.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_9.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_ball_10.png')).convert_alpha(),
		]
		self.frozen_jump = pygame.image.load(Path("images", "player", "Frozen_bear", "jump_frozen.png")).convert_alpha()
		self.rect = pygame.Rect(x, y, 284, 286)
		self.jump = False
		self.fire = False
		self.frozen = False
		self.anim_count = False
		self.tick = 0


	#Обновление куба силы
	def update(self, screen, player):
		self.anim_cube()
		self.draw_jump(screen, player)

	def draw_jump(self,screen, player):
		if self.jump and player.lookright:
			screen.blit(self.frozen_jump, (player.rect.centerx - 45, player.rect.centery + 5))
		if self.jump and not player.lookright:
			screen.blit(self.frozen_jump, (player.rect.centerx - 25, player.rect.centery + 5))


	#Анимация силы
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
			pygame.image.load(Path('images','bg','power_1.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_2.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_3.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_4.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_5.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_6.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_7.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_8.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_9.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_10.png')).convert_alpha(),
		]

	#Изменение куба силы на куб с силой огня
	def change_fire_powerball(self):
		self.fire = True
		self.image = [
			pygame.image.load(Path('images','bg','power_fire_ball_1.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_2.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_3.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_4.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_5.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_6.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_7.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_8.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_9.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_ball_10.png')).convert_alpha(),
		]

	#Изменение куба силы на куб с силой без огня
	def change_fire_power(self):
		self.fire = False
		self.image = [
			pygame.image.load(Path('images','bg','power_fire_1.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_2.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_3.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_4.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_5.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_6.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_7.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_8.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_9.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_fire_10.png')).convert_alpha(),
		]

		#Изменение куба силы на куб с силой льда
	def change_frozen_powerball(self):
		self.frozen = True
		self.image = [
			pygame.image.load(Path('images','bg','power_frozen_ball_1.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_2.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_3.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_4.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_5.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_6.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_7.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_8.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_9.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_ball_10.png')).convert_alpha(),
		]

	#Изменение куба силы на куб с силой без огня
	def change_frozen_power(self):
		self.frozen = False
		self.image = [
			pygame.image.load(Path('images','bg','power_frozen_1.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_2.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_3.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_4.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_5.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_6.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_7.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_8.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_9.png')).convert_alpha(),
			pygame.image.load(Path('images','bg','power_frozen_10.png')).convert_alpha(),
		]