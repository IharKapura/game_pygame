import pygame, controls

from player import *
from bullet import Bullet
from bg import Bg
from enemies import Enemies
from enemies_scorp import EnemiesScorp
from level import Level
from cube import Cube
from bad_cube import BadCube
from cube_power import CubePower
from finish import Finish
#from pygame.sprite import Group




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
    level = Level()
    enemies = Enemies(0, 0)
    enemies_scorp = EnemiesScorp(0, 0)
    finish = Finish(0, 0)
    clock = pygame.time.Clock()

    #Музыка для фона
    #level.play_music_bg()

    run_game = True




    
    

    while run_game:
        
        controls.events(player, bullet, level, bg, cube_power, cube, bad_cube)
        controls.update(screen, bg, player, enemies, bullet, level, cube, bad_cube, cube_power, enemies_scorp, finish)
        clock.tick(FPS)
        pygame.display.update()
        pygame.display.flip()
        print(clock)

        
if __name__ == "__main__":
    main()