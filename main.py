import pygame, controls
from player import Player
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
from sounds import Sounds
from tablet import Tablet
from boss import Boss
from bees import Bees


WIDTH = 1920
HEIGHT = 1080
FPS = 60


def main():    
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bear can be a hero")
    player = Player(screen)
    bg = Bg(screen, player)
    bullet = Bullet(screen, player)
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
    sounds = Sounds()
    tablet = Tablet(0, 0)
    boss = Boss(0, 0)
    bees = Bees(0, 0)
    clock = pygame.time.Clock()
    #Проигрывание музыки в меню на старте игры
    if sounds.play_menu and menu.menu_ON:
        sounds.menu.play(-1)


    while True:       
        controls.events(screen, player, bullet, level, bg, cube_power,
                        cube, bad_cube, menu, sounds, boss)
        controls.update(screen, bg, player, enemies, bullet,
                        level, cube, bad_cube, cube_power,
                        enemies_scorp, enemies_bug, finish,
                        lives, menu, sounds, tablet, boss, bees)
        clock.tick(FPS)
        pygame.display.update()
        pygame.display.flip()
        print(clock)
        
if __name__ == "__main__":
    main()