import pygame, controls

from player import *
from bullet import Bullet
from bg import Bg
from enemies import Enemies
from enemies_scorp import EnemiesScorp
from enemies_bug import EnemiesBug
from level import Level
from cube import Cube
from bad_cube import BadCube
from cube_power import CubePower
from finish import Finish
from lives import Lives
from menu import Menu
#from pygame.sprite import Group




WIDTH = 1920
HEIGHT = 1080
FPS = 60
FULLWINDOW = False


def main():
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLWINDOW)
    pygame.display.set_caption("Bear can be a hero")
    #all_sprites = pygame.sprite.Group()
    player = Player(screen)
    bullet = Bullet(screen, player)
    bg = Bg(screen, player)
    menu = Menu(screen)
    cube = Cube(0, 0)
    bad_cube = BadCube(0, 0)
    cube_power = CubePower(0, 0)
    level = Level()
    enemies = Enemies(0, 0)
    enemies_scorp = EnemiesScorp(0, 0)
    enemies_bug = EnemiesBug(0, 0)
    finish = Finish(0, 0)
    lives = Lives(0, 0)
    clock = pygame.time.Clock()

    #Музыка для фона
    #level.play_music_bg()

    run_game = True

    while run_game:
        
        controls.events(player, bullet, level, bg, cube_power, cube, bad_cube, menu)
        controls.update(screen, bg, player, enemies, bullet, level, cube, bad_cube, cube_power, enemies_scorp, enemies_bug, finish, lives, menu)
        clock.tick(FPS)
        pygame.display.update()
        pygame.display.flip()
        print(clock)

        
if __name__ == "__main__":
    main()