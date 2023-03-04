import pygame
from player import Player
from level import Level
from bg import Bg
from cube import Cube


class Level_01(Level):
	def __init__(self, player):
		# Вызываем родительский конструктор
		Level.__init__(self, player)

		# Массив с данными про кубы. Данные в таком формате:
		# ширина, высота, x и y позиция
		level = [
			[210, 32, 500, 500],
			[210, 32, 200, 400],
			[210, 32, 600, 300],
		]

		# Перебираем массив и добавляем каждую платформу в группу спрайтов - сube_list
		for cube in level:
			block = Cube()
			block.rect.x = cube[2]
			block.rect.y = cube[3]
			block.player = self.player
			self.cube_list.add(block)