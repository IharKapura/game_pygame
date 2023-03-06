import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite

class Cube(Sprite):
	
	
	def __init__(self, x, y):
		# инициализация кубов
		Sprite.__init__(self)
		#self.image = pygame.Surface((77,77))
		self.image = pygame.image.load(Path('images','level1_image','cube_forest.png')).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect = pygame.Rect((x + 2), (y + 5), 73, 70)
		self.image1 = pygame.image.load(Path('images','level1_image','cube_w_spike.png')).convert_alpha()
		self.rect1 = self.image1.get_rect()
		self.rect1 = pygame.Rect((x + 2), (y + 5), 73, 70)

class Level(object):
	def __init__(self, player, cube):
		# Создаем группу спрайтов (поместим платформы различные сюда)
		#self.cube_list = pygame.sprite.Group()
		self.platforms = []
		self.bad_platforms = []
		#self.cube_list.add(cube)

		self.music_bg = True

		self.level_number = 0
		#Уровень 1
		self.level = []

		""" self.bg = bg """

	# Обновление уровня
	def update(self, screen, cube):
		self.draw(screen, cube)
		#self.draw(screen, cube, bg)


	# Отрисовка уровня
	def draw(self, screen, cube):
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					screen.blit(cube.image, (x, y))
				if col == "+":
					screen.blit(cube.image1, (x, y))
				x += 73
			y += 73
			x = 0


	# Уровень 1
	def level1(self):
		self.level = [
				"                            ",
				"                            ",
				"               o            ",
				"    o oo        o   o  o    ",
				"o      o   o   o   o   o    ",
				"   o   o          o    o    ",
				"  oooo   oo     o      o    ",
				"o             o        o    ",
				" o                     o    ",
				"  o                    o    ",
				"   oo   o  oo   ooo   oo    ",
				"                   o   o    ",
				"                    o  o    ",
				"        o   o         oo    ",
				"ooo  +ooo++o oo o  oooooooooo"	
		]
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = Cube(x,y)
					self.bad_platforms.append(cb)
				x += 73
			y += 73
			x = 0


	#Уровень 2
	def level2(self):
		self.level = [
				"                            ",
				"                            ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"                        o   ",
				"oooooooooooooooooooooooooooo"
			]
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = Cube(x,y)
					self.bad_platforms.append(cb)
				x += 73
			y += 73
			x = 0
	

	#Уровень 3
	def level3(self):
		self.level = [
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"oooooooooooooooooooooooooooo"
			]
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = Cube(x,y)
					self.bad_platforms.append(cb)
				x += 73
			y += 73
			x = 0

	def rect_cube(self):
		...
		""" x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = Cube(x,y)
					self.bad_platforms.append(cb)
				x += 73
			y += 73
			x = 0 """
	



	def play_music_bg(self):
		if self.music_bg:
			pygame.mixer.music.load('sounds/1-title.mp3')
			pygame.mixer.music.play()
