import pygame
from pathlib import Path
from cube import Cube
from bad_cube import BadCube
from cube_power import CubePower
from enemies import Enemies
from enemies_scorp import EnemiesScorp
from enemies_bug import EnemiesBug
from finish import Finish
from lives import Lives
from tablet import Tablet


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
		#Изображение для чекпоинта
		self.checkpoint = pygame.image.load(Path('images','bg','checkpoint.png')).convert_alpha()
		#Списки объектов
		self.platforms = []
		self.bad_platforms = []
		self.player_power = []
		self.enemies = []
		self.enemies_scorp = []
		self.enemies_bug = []
		self.level = []
		self.finish = []
		self.lives = []
		self.tablets = []
		#Номер уровня
		self.level_number = 8

	# Обновление уровня
	def update(self, screen, cube, bad_cube, cube_power, enemies, enemies_scorp, enemies_bug, finish, lives, tablet):
		self.draw(screen, cube, bad_cube, cube_power, enemies, enemies_scorp, enemies_bug, finish, lives, tablet)

	# Отрисовка уровня
	def draw(self, screen, cube, bad_cube, cube_power, enemies, enemies_scorp, enemies_bug, finish, lives, tablet):
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					screen.blit(cube.image, (x, y))
				elif col == "C":
					screen.blit(self.checkpoint, (x, y + 21))
				elif col == "+":
					screen.blit(bad_cube.image, (x, y))
				elif col == "T":
					screen.blit(tablet.image, (x, y))
				elif col == "^":
					screen.blit(bad_cube.image[bad_cube.anim_count], (x, y))
				elif col == "*":
					screen.blit(cube_power.image[cube_power.anim_count], (x, y + 7))
				elif col == "H":
					for i in self.lives:
						screen.blit(i.image, (x + 26, y + 26))
				elif col == "E":
					for i in self.enemies:
						screen.blit(i.image[enemies.anim_count], (x , y + 15))
				elif col == "S":
					for i in self.enemies_scorp:
						screen.blit(i.image[enemies_scorp.anim_count], (x , y + 27))
				elif col == "B":
					for i in self.enemies_bug:
						screen.blit(i.image[enemies_bug.anim_count], (x , y + 45))
				elif col == "F":
					for i in self.finish:
						screen.blit(i.image, (x, y + 21))
				x += 73
			y += 73
			x = 0

	#Размещение объектов по уровню
	# o - обычный куб
	# + - шип
	# Е - враг растение
	# S - враг скорпион
	# * - сила
	# ^ - плампя
	# F - конец уровня
	def object_rect(self):
		self.enemies.clear()
		self.enemies_scorp.clear()
		self.enemies_bug.clear()
		self.lives.clear()
		self.finish.clear()
		self.tablets.clear()
		self.player_power.clear()

		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					cb = Cube(x,y)
					self.platforms.append(cb)
				elif col == "+":
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				elif col == "^":
					cb = BadCube(x,y)
					self.bad_platforms.append(cb)
				elif col == "*":
					cb = CubePower(x, y)
					self.player_power.append(cb)
				elif col == "T":
					cb = Tablet(x, y)
					self.tablets.append(cb)
				elif col == "H":
					cb = Lives(x, y)
					self.lives.append(cb)
				elif col == "E":
					cb = Enemies(x,y)
					self.enemies.append(cb)
				elif col == "S":
					cb = EnemiesScorp(x, y)
					self.enemies_scorp.append(cb)
				elif col == "B":
					cb = EnemiesBug(x, y)
					self.enemies_bug.append(cb)
				elif col == "F":
					cb = Finish(x, y)
					self.finish.append(cb)
				x += 73
			y += 73
			x = 0

	# Уровень 1_1(1)
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
				"           T      H         ",
				"           oooooooo      F  ",
				"ooooooooooooooooooo  ooooooo"
			]		
		self.object_rect()

	#Уровень 1_2(2)
	def level1_2(self):

		self.level = [
				"                            ",
				"               H            ",
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
				" C      o   o         oo F  ",
				"ooo   ooo  o oo o  oooooooooo"	
		]
		self.object_rect()

	#Уровень 1_3(3)
	def level1_3(self):
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
				"ooooo            EH         ",
				"      o   ooooooooo    oo  o",
				"     o o  S        ++++ oF o",
				"ooooooooooooo   oooooooooooo"
			]		
		self.object_rect()

	#Уровень 1_4(4)
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
				"        T                    ",
				"       ooooo*   o            ",
				"      oooooo    oo          ",
				"     ooooooo    ooo         ",
				"    oooooooo     B          ",
				"   oooooooooooooooooo  EF   ",
				"oooooooooooooooooooooooooooo"
			]
		self.object_rect()

	#Уровень 1_5(5)
	def level1_5(self):
		self.level = [
				"       +++                  ",
				" ooo   ooo  ooo ooo         ",
				"                        o   ",
				"                    B o     ",
				"      +    +  +     o       ",
				"    oooo  ooo o ooo         ",
				"o                           ",
				"   o                        ",
				"  oo                    H   ",
				"o             S         o   ",
				" oooo   oo   oooooo     o   ",
				"                     ooo    ",
				"                ooooo       ",
				" C        E    oooooo    F  ",
				"ooooooo   oooooooooooooooooo"
			] 
		self.object_rect()

	#Уровень 1_6(6)
	def level1_6(self):
		self.level = [
				"                            ",
				"                            ",
				"                          + ",
				"    o   oo  + ++     B +  o ",
				"   o        o oo     oooo o ",
				"o                   o   o o ",
				"  oo         oo oo      o o ",
				"       o       +          + ",
				"    o          o H ++     o ",
				"oo       + S   oooooo o ooo ",
				"   oo  o o o   o       +    ",
				"              o      ooo    ",
				"             o     oo       ",
				"       E    ooo         F   ",
				"oooo   ooooooooooooooooooooo"
			]
		self.object_rect()

	#Уровень 1_7(7)
	def level1_7(self):
		self.level = [
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"              E             ",
				"              oooo          ",
				"          o                 ",
				"           o         +  S+  ",
				"            o        o  oo  ",
				"             o     +oo  ooo ",
				"              o    ooo  oooo",
				"                  oooo  oooo",
				"          T   oo++oooo   F  ",
				"oooooooooooooooooooooooooooo"
			]
		self.object_rect()

	#Уровень 2_0(8)
	def level2_0(self, bg, cube, bad_cube):
		self.level = [
				"                            ",
				"                            ",
				"    H ^            o        ",
				"   ooo ooo o  o   o^^^      ",
				"                 o ooo      ",
				"                o        B  ",
				"     ^    E ^  o        oooo",
				"    o o   o o o        ^    ",
				"o                     ^o    ",
				"oo                    o     ",
				"o   o    ^    oo^^^^        ",
				"        ooo     ^^^^o       ",
				"   ooo   o      oooo^       ",
				"oC             oooooo    F  ",
				"ooo^^^ooo^^^oooooooooooooooo"
			]
		bg.change_bg_cave()
		cube.change_cube_cave()
		bad_cube.change_bad_cube_cave()
		self.object_rect()


#Уровень 2_1(9)
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
				"        *                   ",
				"                            ",
				"     T                      ",
				"     ooooo                  ",
				"    oooooo^^^^^oo           ",
				"   oooooooooooooo        F  ",
				"ooooooooooooooooo^^^^^^^ooooo"
			]
		cube_power.change_fire_powerball()
		self.object_rect()

#Уровень 2_2(10)
	def level2_2(self):
		self.level = [
				"                            ",
				"                         F  ",
				" H                 o     ooo",
				"^o^    oo o  o              ",
				" oo               o         ",
				"oo               o          ",
				"        o^o^oo              ",
				"      oooooooo              ",
				"o                           ",
				"  o ^                  o    ",
				"    ooo     oooo         o  ",
				"    oo                  o   ",
				"    o           o      o    ",
				" C             oo^^^^^^     ",
				"ooooooooooooooooo^^^^^^oooooo"
			]
		self.object_rect()

#Уровень 2_3(11)
	def level2_3(self):
		self.level = [
				"                           ",
				"                           ",
				"                           ",
				"      o^          o^^^^^ oo",
				"    o^oo         o ooooo   ",
				"   ooooo      o    ooooo   ",
				"o         o             o  ",
				"oo                       F ",
				"oo   o^             o    oo",
				"     ooo  oo               ",
				"      o       ^o           ",
				"H             ooo          ",
				"o        o    o    oo    o ",
				"        oo              o  ",
				"ooo^^^oooooooooo^^oooooooooo"
			]
		self.object_rect()

#Уровень 2_4(12)
	def level2_4(self):
		self.level = [
				"                            ",
				"                            ",
				"                            ",
				"    o^^^^^o  E       o      ",
				"     ooooo oooooo         o ",
				"                ^        o  ",
				"oo              ^  o    o   ",
				"  o             oo          ",
				"^^^^            ooo  o      ",
				"ooooH ^ ^ ^        o     oo ",
				"ooooooooooooo    ooo    ooo ",
				" F                 oo       ",
				"oooooooooooooooooooooo   oo ",
				"                        ooo ",
				"oooooooooooooooooooooooooooo"
			]
		self.object_rect()

#Уровень 2_5(13)
	def level2_5(self):
		self.level = [
				"              oooooooo      ",
				"                  ooo    F  ",
				"                   o     ooo",
				"                        oooo",
				"                     ooooooo",
				"        T           oooooooo",
				"     ooooooooo     ooooooooo",
				"o                           ",
				"   oo                       ",
				"       oo ^^^^ oooooo       ",
				"         oooooo          ooo",
				"          oooo        oH    ",
				"                  o    oo^^^",
				"       ^^     oo       ooooo",
				"oooooooooooooooo^^o^^^^ooooo"
			]
		self.object_rect()

#Уровень 2_6(14)
	def level2_6(self, bg, cube, bad_cube):
		self.level = [
				"              oooooooo      ",
				"                  ooo    F  ",
				"                   o     ooo",
				"                        oooo",
				"                     ooooooo",
				"        T           oooooooo",
				"     ooooooooo     ooooooooo",
				"o                           ",
				"   oo                       ",
				"       oo ^^^^ oooooo       ",
				"         oooooo          ooo",
				"          oooo        oH    ",
				"                  o    oo^^^",
				"       ^^     oo       ooooo",
				"oooooooooooooooo^^o^^^^ooooo"
			]
		bg.change_bg_frozen()
		cube.change_cube_frozen()
		bad_cube.change_bad_cube_frozen()
		self.object_rect()

	#Уровень 2_7(15)
	def level2_7(self, cube_power):
		self.level = [
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"                            ",
				"        *                   ",
				"                            ",
				"     T                      ",
				"     ooooo                  ",
				"    oooooo^^^^^oo           ",
				"   oooooooooooooo        F  ",
				"ooooooooooooooooo^^^^^^^ooooo"
			]
		cube_power.change_frozen_powerball()
		self.object_rect()