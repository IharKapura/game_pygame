import pygame
from pathlib import Path


class Sounds():


    def __init__(self):
        #Инициализация музыки и звуков
        self.play_menu = True
        self.list_music = [
            'green-hill-zone.mp3',
            'menu.mp3',
        ]
        self.music_count = 0
        self.music_tick = False
        pygame.mixer.music.load(Path('sounds', self.list_music[self.music_count]))
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
        self.fire_jerk = pygame.mixer.Sound(Path('sounds', 'fire_jerk.mp3'))
        self.fire_jerk.set_volume(0.1)

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

    #Звук звук огненного рывка
    def jerk_fire(self):
        self.fire_jerk.play()

    #Звук включения огненной силы
    def set_fire_power(self):
        self.act_fire_power.play()

    #Звук получения урона
    def dead(self):
        self.hit_player.play()