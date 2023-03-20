import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Tablet(Sprite):
		
	#Инициализация табличек
	def __init__(self, x, y):
		Sprite.__init__(self)		
		self.image = pygame.image.load(Path('images', 'tablet.png'))
		self.rect = pygame.Rect(x, y, 174, 84)
		self.player_say = [
			pygame.image.load(Path('images', 'read_tablet_first.png')),
			pygame.image.load(Path('images', 'read_tablet_second.png')),
			pygame.image.load(Path('images', 'read_tablet_third.png')),
			pygame.image.load(Path('images', 'read_tablet_fourth.png')),
			pygame.image.load(Path('images', 'read_tablet_fifth.png')),
			pygame.image.load(Path('images', 'read_tablet_sixth.png')),
			pygame.image.load(Path('images', 'read_tablet_seventh.png')),
			pygame.image.load(Path('images', 'read_tablet_eighth.png')),
			pygame.image.load(Path('images', 'read_tablet_ninth.png')),
		]

