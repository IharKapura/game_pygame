import pygame, controls

from player import *
from bullet import Bullet
from bg import Bg
from enemies import Enemies
from level import Level
from cube import Cube
from pygame.sprite import Group




WIDTH = 1920
HEIGHT = 1020
FPS = 60


def main():
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BEAR TRAVELER")
    #all_sprites = pygame.sprite.Group()

    player = Player(screen)
    bullet = Bullet(screen, player)
    bg = Bg(screen, player)
    cube = Cube(0, 0)
    level = Level(player, cube)
    enemies = Enemies(screen)
    clock = pygame.time.Clock()

    #Размещение всех кубов
    level.rect_cube()

    gameplay = True
   
    #Добавление текста
    """ font_text = pygame.font.Font('fonts\MoonDance-Regular.ttf', 40)
    text_surface = font_text.render("Break", False, "Green") """


    #TODO Разобраться со звуком
    """ bg_sound = pygame.mixer.Sound('sounds/_battle.mp3')
    bg_sound.play() """
    
    

    while True:
        
        if gameplay:
            controls.events(player, bullet, level)
            #controls.collision(screen, player, enemies, bullet, level)
            controls.update(screen, bg, player, enemies, bullet, level, cube)
            #bullet.shot(screen, player)
            clock.tick(FPS)
        else:
            screen.fill((87,88,89))
        pygame.display.update()
        pygame.display.flip()
        #print(player.rect)

        
if __name__ == "__main__":
    main()