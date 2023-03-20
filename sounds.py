import pygame
from pathlib import Path


class Sounds():
    #Инициализация музыки и звуков
    def __init__(self):
        self.play_menu = True
        self.list_music = [
            'green-hill-zone.mp3',
            'fire_level.mp3',
            'frozen_level.mp3',
            'field_level.mp3',
            'final-zone.mp3',
            'end_game.mp3',
        ]
        self.music_tick = False
        pygame.mixer.music.load(Path('sounds', self.list_music[0]))
        pygame.mixer.music.set_volume(0.04)
        self.menu = pygame.mixer.Sound(Path('sounds', 'menu.mp3'))
        self.menu.set_volume(0.2)
        self.jump = pygame.mixer.Sound(Path('sounds', 'jump.wav'))
        self.jump.set_volume(0.1)
        self.shot = pygame.mixer.Sound(Path('sounds', 'shot.wav'))
        self.shot.set_volume(0.1)
        self.lives = pygame.mixer.Sound(Path('sounds', 'lives.wav'))
        self.lives.set_volume(0.1)
        self.hit_enemies = pygame.mixer.Sound(Path('sounds', 'hit_enemies.wav'))
        self.hit_enemies.set_volume(0.1)
        self.get_fire_power = pygame.mixer.Sound(Path('sounds', 'activate_fire_power.mp3'))
        self.get_fire_power.set_volume(0.1)
        self.fire_power = pygame.mixer.Sound(Path('sounds', 'activate_fire_power.mp3'))
        self.fire_power.set_volume(0.05)
        self.hit_player = pygame.mixer.Sound(Path('sounds', 'dead.wav'))
        self.hit_player.set_volume(0.1)
        self.frozen_power = pygame.mixer.Sound(Path('sounds', 'frozen.mp3'))
        self.frozen_power.set_volume(0.1)
        self.hit_hive = pygame.mixer.Sound(Path('sounds', 'hive_hit.wav'))
        self.hit_hive.set_volume(0.15)
        self.hive_bees = pygame.mixer.Sound(Path('sounds', 'bees.wav'))
        self.hive_bees.set_volume(0.1)


    #Проигрывание музыки на задний фон
    def play_music_bg(self):
        pygame.mixer.music.play(-1)

    #Звук прыжка
    def sound_jump(self):
        self.jump.play()

    #Звук броска
    def sound_shot(self):
        self.shot.play()

    #Звук поулчения жизни
    def get_lives(self):
        self.lives.play()

    #Звук звук убийста врага
    def hitenemies(self):
        self.hit_enemies.play()

    #Звук получение огненной силы
    def get_fire(self):
        self.get_fire_power.play()
    
    #Звук ледяной силы
    def frozen(self):
        self.frozen_power.play()

    #Звук звук огненного рывка
    def jerk_fire(self):
        self.fire_power.play()

    #Звук включения огненной силы
    def set_fire_power(self):
        self.fire_power.play()

    #Звук получения урона
    def dead(self):
        self.hit_player.play()

    #Звук удара по улею
    def hive_hit(self):
        self.hit_hive.play()

    #Звук улея при получении урона
    def bees_hive(self):
        self.hive_bees.play()