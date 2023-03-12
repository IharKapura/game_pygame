import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite
from cube import Cube
from bad_cube import BadCube
from cube_power import CubePower
from enemies import Enemies
from bg import Bg






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

		self.platforms = []
		self.bad_platforms = []
		self.player_power = []
		self.enemies = []
		self.level = []

		self.music_bg = True

		self.level_number = 0

		""" self.bg = bg """


	# Обновление уровня
	def update(self, screen, cube, bad_cube, cube_power, enemies):
		self.draw(screen, cube, bad_cube, cube_power, enemies)


	# Отрисовка уровня
	def draw(self, screen, cube, bad_cube, cube_power, enemies):
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					screen.blit(cube.image, (x, y))
				if col == "+":
					screen.blit(bad_cube.image, (x, y))
				if col == "*":
					screen.blit(cube_power.image, (x, y + 40))
				if col == "E":
					for i in self.enemies:
						screen.blit(i.image[enemies.anim_count], (x, y + 15))
				x += 73
			y += 73
			x = 0


	# Уровень 1_1
	def level1_1(self):
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
				"           o                ",
				"ooooooooooooooooooo  ooooooo"
			]
		
		x=y=0
		# Размещение кубов
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				if col == "E":
					en = Enemies(x,y)
					self.enemies.append(en)
				if col == "*":
					cb = CubePower(x, y)
					self.player_power.append(cb)
				x += 73
			y += 73
			x = 0


	#Уровень 1_2
	def level1_2(self):
		self.enemies.clear()
		self.level = [
				"                            ",
				"                            ",
				"               o            ",
				"    o oo       +o   o  o    ",
				"o      o   o   o   o   o    ",
				"   o E o ++       o    o    ",
				"  oooo   oo     o      o    ",
				"o             o        o    ",
				" o                     o    ",
				"  o                   Eo    ",
				"   oo   o  oo   ooo   oo    ",
				"                   o   o    ",
				"                    o  o    ",
				"        o   o         oo    ",
				"ooo   ooo  o oo o  oooooooooo"	
		]

		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				if col == "E":
					en = Enemies(x,y)
					self.enemies.append(en)
				x += 73
			y += 73
			x = 0


	#Уровень 1_3
	def level1_3(self):
		self.enemies.clear()
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
				"ooooo            E          ",
				"      o   ooooooooo    oo  o",
				"     o o  E        ++++ o  o",
				"ooooooooooooo   oooooooooooo"
			]
		
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				if col == "E":
					en = Enemies(x,y)
					self.enemies.append(en)
				x += 73
			y += 73
			x = 0


	#Уровень 1_4
	def level1_4(self):
		self.enemies.clear()
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
				"              *             ",
				"            oooo            ",
				"           oooooo           ",
				"          oooooooo          ",
				"         oooooooooo      E  ",
				"oooooooooooooooooooooooooooo"
			]
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				if col == "*":
					cb = CubePower(x, y)
					self.player_power.append(cb)
				if col == "E":
					en = Enemies(x,y)
					self.enemies.append(en)
				x += 73
			y += 73
			x = 0


	#Уровень 1_5
	def level1_5(self):
		self.enemies.clear()
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
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				if col == "*":
					cb = CubePower(x, y)
					self.player_power.append(cb)
				if col == "E":
					en = Enemies(x,y)
					self.enemies.append(en)
				x += 73
			y += 73
			x = 0


	#Музыка для заднего фона
	def play_music_bg(self):
		if self.music_bg:
			pygame.mixer.music.load('sounds/1-title.mp3')
			pygame.mixer.music.play(-1)
