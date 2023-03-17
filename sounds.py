import pygame
from pathlib import Path


class Sounds():


    def __init__(self):
        self.play_menu = True
        pygame.mixer.music.load(Path('sounds', 'green-hill-zone.mp3'))
        pygame.mixer.music.set_volume(0.04)
        self.menu = pygame.mixer.Sound(Path('sounds', 'menu.mp3'))
        self.menu.set_volume(0.2)
        self.jump = pygame.mixer.Sound(Path('sounds', 'jump.wav'))
        self.jump.set_volume(0.2)
        self.shot = pygame.mixer.Sound(Path('sounds', 'shot.wav'))
        self.shot.set_volume(0.1)
        self.lives = pygame.mixer.Sound(Path('sounds', 'lives.wav'))
        self.lives.set_volume(0.1)
        self.hit_enemies = pygame.mixer.Sound(Path('sounds', 'hit_enemies.wav'))
        self.hit_enemies.set_volume(0.1)
        self.get_fire_power = pygame.mixer.Sound(Path('sounds', 'activate_fire_power.mp3'))
        self.get_fire_power.set_volume(0.1)
        self.act_fire_power = pygame.mixer.Sound(Path('sounds', 'activate_fire_power.mp3'))
        self.act_fire_power.set_volume(0.1)
        self.hit_player = pygame.mixer.Sound(Path('sounds', 'dead.wav'))
        self.hit_player.set_volume(0.1)


    def play_music_bg(self):
        pygame.mixer.music.play(-1)


    def sound_jump(self):
        self.jump.play()

    
    def sound_shot(self):
        self.shot.play()


    def get_lives(self):
        self.lives.play()


    def hitenemies(self):
        self.hit_enemies.play()


    def get_fire(self):
        self.get_fire_power.play()

    
    def set_fire_power(self):
        self.act_fire_power.play()

    
    def dead(self):
        self.hit_player.play()


