import pygame, pathlib
from pathlib import Path
from pygame.sprite import Sprite


class Menu(Sprite):
    
    #Инициализация меню
    def __init__(self, screen):
        self.screen = screen
        self.menu_play = pygame.image.load(Path('images','menu_play.png')).convert_alpha()
        self.menu_controls = pygame.image.load(Path('images','menu_controls.png')).convert_alpha()
        self.menu_quit = pygame.image.load(Path('images','menu_quit.png')).convert_alpha()
        self.controls = pygame.image.load(Path('images','controls.png')).convert_alpha()
        self.resume_level = [
            pygame.image.load(Path('images','change_level_0.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_2_C.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_2_N.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_5_C.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_5_N.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_8_C.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_8_N.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_10_C.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_10_N.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_14_C.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_14_N.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_16_C.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_16_N.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_19_C.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_19_N.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_22_C.png')).convert_alpha(),
            pygame.image.load(Path('images','change_level_22_N.png')).convert_alpha(),
            ]
        self.menu_count = 1
        self.game_run = False
        self.change_count = 1
        self.change_lvl = 1
        self.menu_ON = True
        self.save = open('save.txt')
        self.progress = int(self.save.read())

    #Обновление меню
    def update(self):
        self.draw()

    #Отрисовка меню
    def draw(self):
        if self.menu_count == 1:
            self.screen.blit(self.menu_play, (0, 0))
        elif self.menu_count == 2:
            self.screen.blit(self.menu_controls, (0, 0))
        elif self.menu_count == 3:
            self.screen.blit(self.menu_quit, (0, 0))
        elif self.menu_count == 4:
            self.screen.blit(self.controls, (0, 0))
        elif self.menu_count == 5:
            if self.progress == 2:
                if self.change_count == 1:
                    self.screen.blit(self.resume_level[1], (0, 0))
                elif self.change_count == 2:
                    self.screen.blit(self.resume_level[2], (0, 0))
            elif self.progress == 5:
                if self.change_count == 1:
                    self.screen.blit(self.resume_level[3], (0, 0))
                elif self.change_count == 2:
                    self.screen.blit(self.resume_level[4], (0, 0))
            elif self.progress == 8:
                if self.change_count == 1:
                    self.screen.blit(self.resume_level[5], (0, 0))
                elif self.change_count == 2:
                    self.screen.blit(self.resume_level[6], (0, 0))
            elif self.progress == 10:
                if self.change_count == 1:
                    self.screen.blit(self.resume_level[7], (0, 0))
                elif self.change_count == 2:
                    self.screen.blit(self.resume_level[8], (0, 0))
            elif self.progress == 14:
                if self.change_count == 1:
                    self.screen.blit(self.resume_level[9], (0, 0))
                elif self.change_count == 2:
                    self.screen.blit(self.resume_level[10], (0, 0))
            elif self.progress == 16:
                if self.change_count == 1:
                    self.screen.blit(self.resume_level[11], (0, 0))
                elif self.change_count == 2:
                    self.screen.blit(self.resume_level[12], (0, 0))
            elif self.progress == 19:
                if self.change_count == 1:
                    self.screen.blit(self.resume_level[13], (0, 0))
                elif self.change_count == 2:
                    self.screen.blit(self.resume_level[14], (0, 0))
            elif self.progress == 22:
                if self.change_count == 1:
                    self.screen.blit(self.resume_level[15], (0, 0))
                elif self.change_count == 2:
                    self.screen.blit(self.resume_level[16], (0, 0))
            else:
                self.change_count = 2
                self.screen.blit(self.resume_level[0], (0, 0))





    def saves(self, level):
        if level.level_number == 1:
            self.save = open('save.txt', 'w')
            self.save.write('1')
            self.save.close()
        if level.level_number == 2:
            self.save = open('save.txt', 'w')
            self.save.write('2')
            self.save.close()
        elif level.level_number == 5:
            self.save = open('save.txt', 'w')
            self.save.write('5')
            self.save.close()
        elif level.level_number == 8:
            self.save = open('save.txt', 'w')
            self.save.write('8')
            self.save.close()
        elif level.level_number == 10:
            self.save = open('save.txt', 'w')
            self.save.write('10')
            self.save.close()
        elif level.level_number == 14:
            self.save = open('save.txt', 'w')
            self.save.write('14')
            self.save.close()
        elif level.level_number == 16:
            self.save = open('save.txt', 'w')
            self.save.write('16')
            self.save.close()
        elif level.level_number == 19:
            self.save = open('save.txt', 'w')
            self.save.write('19')
            self.save.close()
        elif level.level_number == 22:
            self.save = open('save.txt', 'w')
            self.save.write('22')
            self.save.close()


    