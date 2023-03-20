import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Bullet(Sprite):

    #инициализация меда
    def __init__(self, screen, player):
        super(Bullet, self).__init__()
        self.screen = screen
        self.bullets = []
        self.image = pygame.image.load(Path("images","player_fight","bear_a_ball.png")).convert_alpha()
        self.rect = pygame.Rect(0, 0, 30, 32)
        #Для скорости пули
        self.change_x = False

    #Обновление броска меда
    def update(self, player, level, sounds, boss):
        self.draw_bullet(player, boss)
        self.kill_enemies(level, sounds, boss)

        if self.bullets:
            for (i, el) in enumerate(self.bullets):
                    self.rect = pygame.Rect(el.x, el.y, 30, 32)
                    el.x += self.change_x

            if i > 1 or self.rect.colliderect(boss.rect):
                self.bullets.pop(i)
            elif el.x > (player.rect.centerx + 300):
                self.bullets.pop(i)
            elif el.x < (player.rect.centerx - 300):
                self.bullets.pop(i)
        else:
            self.rect = pygame.Rect(0, 0, 30, 32)
    # Отрисовка меда
    def draw_bullet(self, player, boss):
        if self.bullets:
            for (i, el) in enumerate(self.bullets):
                    self.screen.blit(self.image, (el.x, el.y))
                    el.x += self.change_x

            if i > 1:
                self.bullets.pop(i)
            elif el.x > (player.rect.centerx + 300):
                self.bullets.pop(i)
            elif el.x < (player.rect.centerx - 300):
                self.bullets.pop(i)
     
    #Бросок меда
    def shot_right(self, player):
        self.change_x = 15
        self.bullets.append(self.image.get_rect(center = (player.rect.centerx , player.rect.centery)))

    #Бросок меда
    def shot_left(self, player):
        self.change_x = -15
        self.bullets.append(self.image.get_rect(center = (player.rect.centerx , player.rect.centery)))
        
    #Столкновение меда и смерть врагов
    def kill_enemies(self, level, sounds, boss):
        enemies_hit_list = pygame.sprite.spritecollide(self, level.enemies, False)
        for enem in enemies_hit_list:
            for el in level.enemies:
                if self.rect.colliderect(enem.rect):
                    sounds.hitenemies()
                    level.enemies.remove(el)

        enemies_scorp_hit_list = pygame.sprite.spritecollide(self, level.enemies_scorp, False)
        for enem in enemies_scorp_hit_list:
            for el in level.enemies_scorp:
                if self.rect.colliderect(enem.rect):
                    sounds.hitenemies()
                    level.enemies_scorp.remove(el)

        enemies_bug_hit_list = pygame.sprite.spritecollide(self, level.enemies_bug, False)
        for enem in enemies_bug_hit_list:
            for el in level.enemies_bug:
                if self.rect.colliderect(enem.rect):
                    sounds.hitenemies()
                    level.enemies_bug.remove(el)

        boss_hit_list = pygame.sprite.spritecollide(self, level.boss_hive, False)
        for enem in boss_hit_list:
            for el in level.boss_hive:
                if self.rect.colliderect(enem.rect):
                    sounds.hive_hit()
                    sounds.bees_hive()
                    boss.lives -= 1
                    self.bullets.clear()


