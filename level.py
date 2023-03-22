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
from boss import Boss
from bees import Bees


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
			]
			 """


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
		self.boss_hive = []
		self.bees = []
		self.honey = []
		#Номер уровня
		self.level_number = 0

	# Обновление уровня
	def update(self, screen, cube, bad_cube, cube_power, enemies, enemies_scorp, enemies_bug, finish, lives, tablet, boss, bees):
		self.draw(screen, cube, bad_cube, cube_power, enemies, enemies_scorp, enemies_bug, finish, lives, tablet, boss, bees)
	# Отрисовка уровня
	def draw(self, screen, cube, bad_cube, cube_power, enemies, enemies_scorp, enemies_bug, finish, lives, tablet, boss, bees):
		x=y=0
		for row in self.level:
			for col in row:
				if col == "o":
					screen.blit(cube.image, (x, y))
				elif col == "O" and not boss.dead:
					screen.blit(cube.image, (x, y))
				elif col == "Q":
					screen.blit(bees.image[bees.image_count], bees.rect)
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
				elif col == "M":
					screen.blit(finish.image_honey, (x, y))
				elif col == "J":
					if boss.lives >= 0 and not boss.dead:
						screen.blit(boss.image[0], (x, y))
					else:
						screen.blit(boss.image[1], (x, y))
				x += 73
			y += 73
			x = 0

	#Размещение объектов по уровню
	# o - обычный куб
	# Е - враг растение
	# S - враг скорпион
	# В - враг жук
	# Н - жизнь
	# Т - табличка
	# * - сила
	# ^ - шип, плампя, ледяной шип, крутящиеся шипы
	# F - конец уровня
	# J - бос улей
	def object_rect(self):
		self.enemies.clear()
		self.enemies_scorp.clear()
		self.enemies_bug.clear()
		self.lives.clear()
		self.finish.clear()
		self.tablets.clear()
		self.player_power.clear()
		self.boss_hive.clear()
		self.bees.clear()

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
				elif col == "J":
					cb = Boss(x, y)
					self.boss_hive.append(cb)
				x += 73
			y += 73
			x = 0

	# Уровень (1)
	def level_1(self):
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
				"            T     H         ",
				"           oooooooo      F  ",
				"ooooooooooooooooooo  ooooooo"
			] 		
		self.object_rect()

	#Уровень (2)
	def level_2(self):

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

	#Уровень (3)
	def level_3(self):
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

	#Уровень (4)
	def level_4(self):
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

	#Уровень (5)
	def level_5(self):
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
				" C         E  o oooooo   F  ",
				"ooooooo   oooooooooooooooooo"
			] 
		self.object_rect()

	#Уровень (6)
	def level_6(self):
		self.level = [
				"                            ",
				"                            ",
				"                          + ",
				"    o   oo  + ++       +  o ",
				"   o        o oo     oooo o ",
				"o               B   o   o o ",
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

	#Уровень (7)
	def level_7(self):
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

	#Уровень (8)
	def level_8(self, bg, cube, bad_cube):
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
				"oC             oooooo   F   ",
				"ooo^^^ooo^^^oooooooooooooooo"
			]
		bg.change_bg_cave()
		cube.change_cube_cave()
		bad_cube.change_bad_cube_cave()
		self.object_rect()


#Уровень (9)
	def level_9(self,cube_power):
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

#Уровень (10)
	def level_10(self, bg, cube, bad_cube):
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
		bg.change_bg_cave()
		cube.change_cube_cave()
		bad_cube.change_bad_cube_cave()
		self.object_rect()

#Уровень (11)
	def level_11(self):
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

#Уровень (12)
	def level_12(self):
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

#Уровень (13)
	def level_13(self):
		self.level = [
				"              oooooooo      ",
				"                  ooo    F  ",
				"                   o     ooo",
				"                        oooo",
				"                     ooooooo",
				"        T           oooooooo",
				"     ooooooooo     ooooooooo",
				"o                           ",
				"   oo            E          ",
				"       oo ^^^^ oooooo       ",
				"         oooooo          ooo",
				"          oooo        oH    ",
				"                  o    oo^^^",
				"       ^^     oo       ooooo",
				"oooooooooooooooo^^o^^^^ooooo"
			]
		self.object_rect()

#Уровень (14)
	def level_14(self, bg, cube, bad_cube):
		self.level = [
				"                            ",
				"                            ",
				"                   B ^      ",
				"       E    ^ ^   ^ooo      ",
				"     oooo   oooo^^o     ^   ",
				"    o           oo      oo  ",
				"o             ^             ",
				" ^^o   ^      o           oo",
				" oo   ooo     ^ H        ooo",
				"             oo o      ooooo",
				"            oo          oooo",
				"o     o   o  o^^^^^^o    ooo",
				"oo      o    ooooooooo    oo",
				" C  o^^^ooo      S ooooo F o",
				"oooooooooooooooooooooooooooo"
			]
		bg.change_bg_frozen()
		cube.change_cube_frozen()
		bad_cube.change_bad_cube_frozen()
		self.object_rect()

	#Уровень (15)
	def level_15(self, cube_power):
		self.level = [
				"                            ",
				"  H              *          ",
				"  o            o      o     ",
				"               o      oo    ",
				" o             oooooooo  o  ",
				"                  o     oo  ",
				"o            o T     oooo   ",
				"o           ooooooooo       ",
				"oo         oo               ",
				"ooo       o                 ",
				"ooo  o    o                 ",
				"o        oo   ooo           ",
				"    ooo       o             ",
				"   ooooo    oo           F  ",
				"oooooooooooo^^^^^^^^^^^ooooo"
			]
		cube_power.change_frozen_powerball()
		self.object_rect()

	#Уровень (16)
	def level_16(self, bg, cube, bad_cube):
		self.level = [
				"                            ",
				"                            ",
				"       Eo                   ",
				"       o       oo^          ",
				"      o       ^  o       S  ",
				"            H ^         ooo ",
				"  o         oo^      ^ o    ",
				"              ^o     oo     ",
				"      o       ^ o           ",
				"              ^             ",
				"         o    ^      o      ",
				"    ^ ^       ^  ^^^^^^^^^^^",
				"   ooooo      ^  ooooooooooo",
				" C o   o      ^          F  ",
				"oooooooooooooooooooooooooooo"
			]
		bg.change_bg_frozen()
		cube.change_cube_frozen()
		bad_cube.change_bad_cube_frozen()
		self.object_rect()

	#Уровень (17)
	def level_17(self):
		self.level = [
				"                            ",
				"                            ",
				"           ^o       ^o      ",
				"^         ^o ^^^^^^o        ",
				"oo     o^oo           S^^H  ",
				"        o             oooooo",
				"  o              E          ",
				"            ^^  oooo    o oo",
				"o          ^oo^^    ^^^o  oo",
				"           o  oo    ooooo  o",
				" ooo      o             o  o",
				"        ^o              o  o",
				"        o     o^^^^o    o  o",
				"       o F    oooooo        ",
				"oooo^^^^oooooooooooooooooooo"
			]
		self.object_rect()

	#Уровень (18)
	def level_18(self):
		self.level = [
				"                            ",
				"                            ",
				"     o                      ",
				"     oo                     ",
				"    oooo                    ",
				"     oooo                   ",
				"o    ooooo                  ",
				"     E    o                 ",
				"    ooo    o                ",
				"     o      o               ",
				"o    oo^o    o T            ",
				"     oooo^    ooooo^        ",
				"    ooooooo        o^       ",
				"    ooooooo^^    H  o   F   ",
				"oooooooooooooooooooooooooooo"
			]
		self.object_rect()

	#Уровень (19)
	def level_19(self, bg, cube, bad_cube):
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
				" C             oooooo    F  ",
				"ooo^^^ooo^^^oooooooooooooooo"
			]
		bg.change_bg_field()
		cube.change_cube_field()
		bad_cube.change_bad_cube_field()
		self.object_rect()

	#Уровень (20)
	def level_20(self):
		self.level = [
				"                            ",
				"                            ",
				"                          ^ ",
				"    o   oo  ^ ^^     B ^  o ",
				"   o        o oo     oooo o ",
				"o                   o   o o ",
				"  oo         oo oo      o o ",
				"       o       ^          ^ ",
				"    o          o H ^^     o ",
				"oo       ^ S   oooooo o ooo ",
				"   oo  o o o   o       ^    ",
				"              o      ooo    ",
				"             o     oo       ",
				"       E    ooo         F   ",
				"oooo   ooooooooooooooooooooo"
			]
		self.object_rect()

	#Уровень (21)
	def level_21(self):
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

	#Уровень (22)
	def level_22(self, bg, cube, bad_cube):
		self.level = [
				"                            ",
				"                            ",
				"                   B ^      ",
				"       E    ^ ^   ^ooo      ",
				"     oooo   oooo^^o     ^   ",
				"    o           oo      oo  ",
				"o             ^             ",
				" ^^o   ^      o           oo",
				" oo   ooo     ^ H  T     ooo",
				"             oo o oooo ooooo",
				"            oo          oooo",
				"o     o   o  o^^^^^^o    ooo",
				"oo      o    ooooooooo    oo",
				" C  o^^^ooo      S ooooo F o",
				"oooooooooooooooooooooooooooo"
			]
		bg.change_bg_field()
		cube.change_cube_field()
		bad_cube.change_bad_cube_field()
		self.object_rect()
	
	# Уровень (23)
	def level_23(self):
		self.level = [
				"             Q            ",
				"                          ",
				"                          ",
				"    o       J             ",
				"                      o   ",
				"                       o  ",
				"   o    o  ^  ^ o ^o      ",
				"  o      ^^oOOo^^        o",
				"     o      ^^ oo         ",
				" o    ^   o          ooo  ",
				"        o                 ",
				"  o    o                o ",
				"                    oooooo",
				"    o^         ^o^   OOOF ",
				"ooooooooooooooooooooooooooo"
			]		
		self.object_rect()

	# Уровень (24)
	def level_24(self):
		self.level = [
				"                          ",
				"                          ",
				"                          ",
				"                          ",
				"                          ",
				"                          ",
				"                          ",
				"                          ",
				"                          ",
				"                  M       ",
				"                          ",
				"                          ",
				"                          ",
				"       T            F     ",
				"ooooooooooooooooooooooooooo"
			]		
		self.object_rect()