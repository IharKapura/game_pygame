import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite
from cube import Cube
from bad_cube import BadCube
from cube_power import CubePower
from enemies import Enemies
from enemies_scorp import EnemiesScorp
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
	def __init__(self):

		self.platforms = []
		self.bad_platforms = []
		self.player_power = []
		self.enemies = []
		self.enemies_scorp = []
		self.level = []

		self.music_bg = True

		self.level_number = 0

		""" self.bg = bg """


	# Обновление уровня
	def update(self, screen, cube, bad_cube, cube_power, enemies, enemies_scorp):
		self.draw(screen, cube, bad_cube, cube_power, enemies, enemies_scorp)


	# Отрисовка уровня
	def draw(self, screen, cube, bad_cube, cube_power, enemies, enemies_scorp):
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					screen.blit(cube.image, (x, y))
				if col == "+":
					screen.blit(bad_cube.image, (x, y))
				if col == "^":
					screen.blit(bad_cube.image[bad_cube.anim_count], (x, y))
				if col == "*":
					screen.blit(cube_power.image[cube_power.anim_count], (x, y + 40))
				if col == "E":
					for i in self.enemies:
						screen.blit(i.image[enemies.anim_count], (x , y + 15))
				if col == "S":
					for i in self.enemies_scorp:
						screen.blit(i.image[enemies_scorp.anim_count], (x , y + 27))
				x += 73
			y += 73
			x = 0


	#Размещение объектов по уровню
	# o - обычный куб
	# + - шип
	# Е - враг растение
	# S - враг скорпион
	# * - сила
	def object_rect(self):

		self.enemies.clear()
		self.enemies_scorp.clear()

		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				if col == "+":
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				if col == "^":
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				if col == "*":
					cb = CubePower(x, y)
					self.player_power.append(cb)
				if col == "E":
					en = Enemies(x,y)
					self.enemies.append(en)
				if col == "S":
					cb = EnemiesScorp(x, y)
					self.enemies_scorp.append(cb)
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
				"           oE               ",
				"ooooooooooooooooooo  ooooooo"
			]
		
		self.object_rect()


	#Уровень 1_2
	def level1_2(self):

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
				"  o                   So    ",
				"   oo   o  oo   ooo   oo    ",
				"                   o   o    ",
				"                    o  o    ",
				"        o   o         oo    ",
				"ooo   ooo  o oo o  oooooooooo"	
		]


		self.object_rect()



	#Уровень 1_3
	def level1_3(self):

		self.level = [
				"                        o   ",
				"                    S   o   ",
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
				"     o o  S        ++++ o  o",
				"ooooooooooooo   oooooooooooo"
			]
		
		self.object_rect()


	#Уровень 1_4
	def level1_4(self):

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
				"           o*   o            ",
				"          oo    oo          ",
				"         ooo    ooo         ",
				"        oooo     S          ",
				"       oooooooooooooo    E  ",
				"oooooooooooooooooooooooooooo"
			]

		self.object_rect()


	#Уровень 1_5
	def level1_5(self):

		self.level = [
				"       +++                  ",
				" ooo   ooo  ooo ooo         ",
				"                        o   ",
				"                      o     ",
				"      +    +  +     o       ",
				"    oooo  ooo o ooo         ",
				"o                           ",
				"   o                        ",
				"  oo                        ",
				"o             S         o   ",
				" oooo   oo   oooooo     o   ",
				"                     ooo    ",
				"                ooooo       ",
				"          E    oooooo       ",
				"ooooooo   oooooooooooooooooo"
			] 
		self.object_rect()


	#Уровень 1_6
	def level1_6(self):

		self.level = [
				"                            ",
				"                            ",
				"                          + ",
				"    o   oo  + ++       +  o ",
				"   o        o oo     oooo o ",
				"o                   o   o o ",
				"  oo         oo oo      o o ",
				"       o       +          + ",
				"    o          o   ++     o ",
				"oo       + S   oooooo o ooo ",
				"   oo  o o o   o       +    ",
				"              o      ooo    ",
				"             o     oo       ",
				"       E    ooo             ",
				"oooo   ooooooooooooooooooooo"
			]
		#cube_power.change_fire_power()
		self.object_rect()


	#Уровень 1_7
	def level1_7(self):
		self.level = [
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"               E            ",
				"               oooo         ",
				"           o                ",
				"            o         +  S+ ",
				"             o        o  oo ",
				"              o     +oo  ooo",
				"               o    ooo  ooo",
				"                   oooo  ooo",
				"               oo++oooo     ",
				"oooooooooooooooooooooooooooo"
			]

		self.object_rect()


	#Уровень 2_0
	def level2_0(self, bg, cube, bad_cube):
		self.level = [
				"                            ",
				"                            ",
				"      ^            o        ",
				"   ooo ooo o  o   o^^^      ",
				"                 o ooo      ",
				"                o           ",
				"     ^    E ^  o        oooo",
				"    o o   o o o        ^    ",
				"o                     ^o    ",
				"oo                    o     ",
				"o   o    ^    oo^^^^        ",
				"        ooo         o       ",
				"   ooo   o      oooo^       ",
				"o              oooooo       ",
				"ooo^^^ooo^^^oooooooooooooooo"
			]
		
		
		bg.change_bg_cave()
		cube.change_cube_cave()
		bad_cube.change_bad_cube_cave()
		self.object_rect()


#Уровень 2_1
	def level2_1(self,cube_power):
		self.level = [
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"      *                     ",
				"                            ",
				"                            ",
				"     ooooo                  ",
				"    o    o^^^^^oo           ",
				"   o     oooooooo           ",
				"oooooooooooooooooooooooooooo"
			]
		cube_power.change_fire_powerball()
		self.object_rect()
	#Музыка для заднего фона
	def play_music_bg(self):
		if self.music_bg:
			pygame.mixer.music.load('sounds/1-title.mp3')
			pygame.mixer.music.play(-1)
