import pygame, controls

from player import *
from bullet import Bullet
from bg import Bg
from enemies import Enemies
from level import Level
from cube import Cube
from bad_cube import BadCube
from cube_power import CubePower
from pygame.sprite import Group




WIDTH = 1920
HEIGHT = 1080
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
    bad_cube = BadCube(0, 0)
    cube_power = CubePower(0, 0)
    level = Level(player, cube)
    enemies = Enemies(0, 0)
    clock = pygame.time.Clock()

    #Музыка для фона
    level.play_music_bg()

    run_game = True
    #Добавление текста
    """ font_text = pygame.font.Font('fonts\MoonDance-Regular.ttf', 40)
    text_surface = font_text.render("Break", False, "Green") """


    #TODO Разобраться со звуком
    #pygame.mixer.music.load('sounds/1-title.mp3')
    #pygame.mixer.music.play()
    
    

    while run_game:
        
        controls.events(player, bullet, level, bg, screen)
        #controls.collision(player, level)
        controls.update(screen, bg, player, enemies, bullet, level, cube, bad_cube, cube_power)
        #bullet.shot(screen, player)
        clock.tick(FPS)
        pygame.display.update()
        pygame.display.flip()
        print(len(level.enemies))

        
if __name__ == "__main__":
    main()