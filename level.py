import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite
from cube import Cube






#Заготовка для пустого уровня
""" self.level = [
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
			] """


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
				"ooo+++ooo++o+oo+o++oooooooooo"	
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
				"                        o   ",
				"                        o   ",
				"      oo  o  ooo   oooo o   ",
				"    o                 o o   ",
				"   o                  o o   ",
				"o       o             o o   ",
				"  ooo       oo        o o   ",
				"                oo    o o   ",
				"                     oo o   ",
				"  oooo  o   o  oooo   o o   ",
				"o                           ",
				"ooooo                       ",
				"      o   ooooooooo    oo   ",
				"     o o                o   ",
				"ooooooooooooo   oooooooooooo"
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
				"            oooo            ",
				"           oooooo           ",
				"          oooooooo          ",
				"         oooooooooo         ",
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


	def level4(self):
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
			pygame.mixer.music.load('sounds/_battle.mp3')
			pygame.mixer.music.play(-1)
