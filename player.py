import pygame
from pathlib import Path
from pygame.sprite import Sprite


#Начальная позиция игрока
coor_x = 900
coor_y = 450
#Нижняя граница экрана
coor_screen_dawn = 1080
#Координаты для завершения уровня
coor_level_finish_x = [1800, 1920]
coor_level_finish_y = 997


class Player(Sprite):


    lookright = True

    #инициализация игрока
    def __init__(self,screen):
        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(Path("images","player.png")).convert_alpha()
        self.rect = pygame.Rect(0, 0, 60, 50)
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - coor_x
        self.rect.centery = self.screen_rect.centery + coor_y
        self.cube_list = []
        #Переменные для изменения движения игрока
        self.change_x = 0
        self.change_y = 0
        self.jerk_change_x = 0
        #Переменные статуса игрока
        self.jerk_can = False
        self.player_lives = 3
        self.player_gameover = False
        self.player_gamewin = False
        self.player_power = False
        self.player_get_power = True
        self.player_get_fire = True
        self.player_fire_power = False
        self.player_get_frozen = True
        self.player_frozen_power = False
        #Переменные для прыжка
        self.is_jump = False
        self.jump_count = 7
        #Картинки для персонажа
        self.jerk_right = pygame.image.load(Path("images", "player", "Fire_bear", "fire_jerk_r.png")).convert_alpha()
        self.jerk_left = pygame.image.load(Path("images", "player", "Fire_bear", "fire_jerk_l.png")).convert_alpha()
        self.walk_left = [
            pygame.image.load(Path("images","player_left","br_m_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","br_m_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","br_m_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","br_m_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","br_m_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","br_m_l_6.png")).convert_alpha(),
        ]
        self.walk_right = [
            pygame.image.load(Path("images","player_right","br_m_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","br_m_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","br_m_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","br_m_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","br_m_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","br_m_r_6.png")).convert_alpha(),
        ]
        self.fight_left = [
            pygame.image.load(Path("images","player_fight","fight_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_l_6.png")).convert_alpha(),
        ]
        self.fight_right = [
            pygame.image.load(Path("images","player_fight","fight_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","fight_r_6.png")).convert_alpha(),
        ]
        self.image_jump_rl = [ 
            pygame.image.load(Path("images","jump","jump_up_r.png")).convert_alpha(),
            pygame.image.load(Path("images","jump","jump_dn_r.png")).convert_alpha(),
            pygame.image.load(Path("images","jump","jump_up_l.png")).convert_alpha(),
            pygame.image.load(Path("images","jump","jump_dn_l.png")).convert_alpha(),
        ]
        #Переменные для анимации персонажа
        self.player_animw_count = 0
        self.player_animf_count = 0

    #обновление игрока
    def update_player(self, level, cube_power, sounds, tablet):
        self.player_win(level)
        self.player_dead(sounds)
        self.gravitation()
        self.chek_collision(level)
        self.collision_bad_cube(level, sounds)
        self.colission_power(level, cube_power, sounds)
        self.collision_enemies(level, sounds)
        self.collision_lives(level, sounds)
        self.colission_tablet(level, tablet)
        self.jerk()
        #левая и правая граница экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1920:
            self.rect.right = 1920

    #Картинки для силы огня
    def player_fire(self, bullet):
        if not self.lookright:
            self.flip()
            self.lookright = True
        self.image = pygame.image.load(Path("images","player", "Fire_bear", "fire_player.png")).convert_alpha()
        bullet.image = pygame.image.load(Path("images","player_fight","fire_bear_ball.png")).convert_alpha()
        self.walk_left = [
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_l_6.png")).convert_alpha(),
        ]
        self.walk_right = [
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_br_m_r_6.png")).convert_alpha(),
        ]
        self.fight_left = [
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_l_6.png")).convert_alpha(),
        ]
        self.fight_right = [
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "Fire_bear", "fire_fight_r_6.png")).convert_alpha(),
        ]
    
    #Картинки для силы льда
    def player_frozen(self, bullet):
        if not self.lookright:
            self.flip()
            self.lookright = True
        self.image = pygame.image.load(Path("images","player", "frozen_bear", "frozen_player.png")).convert_alpha()
        bullet.image = pygame.image.load(Path("images","player_fight","frozen_bear_ball.png")).convert_alpha()
        self.walk_left = [
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_l_6.png")).convert_alpha(),
        ]
        self.walk_right = [
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_br_m_r_6.png")).convert_alpha(),
        ]
        self.fight_left = [
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_l_6.png")).convert_alpha(),
        ]
        self.fight_right = [
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player", "frozen_bear", "frozen_fight_r_6.png")).convert_alpha(),
        ]

    #Получение урона
    def taking_damage(self):
        self.player_lives -= 1

    #Проверка игрока на столкновение с кубами для бега по кубам
    def chek_collision(self, level):
        #Движение персонажа по оси Х
        self.rect.x += (self.change_x + self.jerk_change_x)
        #Проверка столкновения с кубами по Х
        block_hit_list = pygame.sprite.spritecollide(self, level.platforms, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right        
        #Движение персонажа по оси У
        self.rect.y += self.change_y
        #Проверка столкновения с кубами по У
        block_hit_list = pygame.sprite.spritecollide(self, level.platforms, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
			# Остановка движения по У
            self.change_y = 0
            self.on_ground = True

    #Столкновения c плохими кубами
    def collision_bad_cube(self, level, sounds):
        bad_hit_list = pygame.sprite.spritecollide(self, level.bad_platforms, False)
        for block in bad_hit_list:
            if self.rect.colliderect(block.rect):
                sounds.dead()
                self.rect.centerx = self.screen_rect.centerx - coor_x
                self.rect.centery = self.screen_rect.centery + coor_y
                self.player_lives -= 1

    #Столкновение с местами для получение силы
    def colission_power(self, level, cube_power, sounds):
        power_hit_list = pygame.sprite.spritecollide(self, level.player_power, False)
        for power in power_hit_list:
            if self.rect.colliderect(power.rect) and level.level_number == 4:
                self.player_get_power = True
                cube_power.change_cube_power()
            elif self.rect.colliderect(power.rect) and cube_power.fire:
                sounds.get_fire()
                self.player_get_fire = True
                cube_power.change_fire_power()
            elif self.rect.colliderect(power.rect) and cube_power.frozen:
                sounds.get_fire()
                self.player_get_frozen = True
                cube_power.change_frozen_power()

    #Столкновение с врагами
    def collision_enemies(self, level, sounds):
        enemies_hit_list = pygame.sprite.spritecollide(self, level.enemies, False)
        for enemies in enemies_hit_list:
            if self.rect.colliderect(enemies.rect):
                sounds.dead()
                self.rect.centerx = self.screen_rect.centerx - coor_x
                self.rect.centery = self.screen_rect.centery + coor_y
                self.player_lives -= 1
                   
        enemies_scorp_hit_list = pygame.sprite.spritecollide(self, level.enemies_scorp, False)
        for enemies_scorp in enemies_scorp_hit_list:
            if self.rect.colliderect(enemies_scorp.rect):
                sounds.dead()
                self.rect.centerx = self.screen_rect.centerx - coor_x
                self.rect.centery = self.screen_rect.centery + coor_y
                self.player_lives -= 1

        enemies_bug_hit_list = pygame.sprite.spritecollide(self, level.enemies_bug, False)
        for enemies_bug in enemies_bug_hit_list:
            if self.rect.colliderect(enemies_bug.rect):
                sounds.dead()
                self.rect.centerx = self.screen_rect.centerx - coor_x
                self.rect.centery = self.screen_rect.centery + coor_y
                self.player_lives -= 1

    #Столкновение с жизнями
    def collision_lives(self, level, sounds):
        lives_hit_list = pygame.sprite.spritecollide(self, level.lives, False)
        for live in lives_hit_list:
            if self.rect.colliderect(live.rect):
                level.lives.clear()
                if self.player_lives <= 4:
                    sounds.get_lives()
                    self.player_lives += 1

    #Столкновение с стабличкой финиша для завершения уровня
    def player_win(self, level):
        finish_hit = pygame.sprite.spritecollide(self, level.finish, False)
        for finish in finish_hit:
            if self.rect.colliderect(finish.rect):
                self.player_gamewin = True
    
    #Столкновение с табличками для отрисовки текста
    def colission_tablet(self, level, tablet):
        tablet_hit = pygame.sprite.spritecollide(self, level.tablets, False)
        for tabl in tablet_hit:
            if self.rect.colliderect(tabl.rect):
                if level.level_number == 1:
                    self.screen.blit(tablet.player_say[0], (self.rect.centerx - 532, self.rect.centery - 371))
                elif level.level_number == 4:
                    self.screen.blit(tablet.player_say[1], (self.rect.centerx - 532, self.rect.centery - 371))
                elif level.level_number == 7:
                    self.screen.blit(tablet.player_say[2], (self.rect.centerx - 532, self.rect.centery - 371))
                elif level.level_number == 9:
                    self.screen.blit(tablet.player_say[3], (self.rect.centerx - 532, self.rect.centery - 371))
                elif level.level_number == 13:
                    self.screen.blit(tablet.player_say[4], (self.rect.centerx - 532, self.rect.centery - 371))
    # Гравитация
    def gravitation(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            #Сила гравитации
            self.change_y += 0.95
    
    #Прыжок
    def jump(self, level):        
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, level.platforms, False)
        self.rect.y -= 10
		# Если все в порядке, прыгаем вверх
        if len(platform_hit_list) > 0 or self.rect.bottom >= coor_screen_dawn:
            if not self.player_frozen_power:
                self.change_y = -13
            elif self.player_frozen_power:
                self.change_y = -20
    
    #Движение влево
    def left(self):
        self.change_x = -8
        if self.lookright:
            self.flip()
            self.lookright = False

    #Движение влево
    def right(self):
        self.change_x = 8
        if not self.lookright:
            self.flip()
            self.lookright = True

    #Остановка персонажа
    def stop(self):
        self.change_x = 0

    #Рывок
    def jerk(self):
        if self.jerk_can and self.player_fire_power and self.lookright:
            self.jerk_change_x = 8
        elif self.jerk_can and self.player_fire_power and not self.lookright:
            self.jerk_change_x = -8
        elif not self.jerk_can:
            self.jerk_change_x = 0

    #Поворот изоброжения по вертикали
    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
                            
    # Отрисовка игрока
    def draw_player(self):
        keys = pygame.key.get_pressed()
        #Анимация движения влево
        if keys[pygame.K_a] and not keys[pygame.K_LCTRL] or keys[pygame.K_LEFT] and not keys[pygame.K_LCTRL]:
            if self.player_animw_count == 5 :
                self.player_animw_count = 0
                self.screen.blit(self.walk_left[self.player_animw_count], self.rect)
            else:
                self.player_animw_count += 1
                self.screen.blit(self.walk_left[self.player_animw_count], self.rect)
        #Анимация движения вправо
        elif keys[pygame.K_d] and not keys[pygame.K_LCTRL] or keys[pygame.K_RIGHT] and not keys[pygame.K_LCTRL]:
            if self.player_animw_count == 5 :
                self.player_animw_count = 0
                self.screen.blit(self.walk_right[self.player_animw_count], self.rect)
            else:
                self.player_animw_count += 1
                self.screen.blit(self.walk_right[self.player_animw_count], self.rect)
        #Анимация атаки влево
        elif keys[pygame.K_q] and self.player_get_power:
            if self.player_animf_count == 5 :
                self.player_animf_count = 0
                self.screen.blit(self.fight_left[self.player_animf_count], (self.rect.centerx - 30, self.rect.centery - 45))
            else:
                self.player_animf_count += 1
                self.screen.blit(self.fight_left[self.player_animf_count], (self.rect.centerx - 30, self.rect.centery - 45))
        #Анимация атаки вправо
        elif keys[pygame.K_e] and self.player_get_power:
            if self.player_animf_count == 5 :
                self.player_animf_count = 0
                self.screen.blit(self.fight_right[self.player_animf_count], (self.rect.centerx - 30, self.rect.centery - 45))
            else:
                self.player_animf_count += 1
                self.screen.blit(self.fight_right[self.player_animf_count], (self.rect.centerx - 30, self.rect.centery - 45))
        elif keys[pygame.K_LCTRL] and self.player_fire_power and self.lookright:
            self.screen.blit(self.jerk_right, self.rect)
        elif keys[pygame.K_LCTRL] and self.player_fire_power and not self.lookright:
            self.screen.blit(self.jerk_left, self.rect)
        else:
            self.screen.blit(self.image, self.rect)

    #Cмерть игрока
    def player_dead(self, sounds):
        if coor_screen_dawn <= self.rect.centery:
            sounds.dead()
            self.rect.centerx = self.screen_rect.centerx - coor_x
            self.rect.centery = self.screen_rect.centery + coor_y
            self.player_lives -= 1
        if self.player_lives <= 0:
            self.rect.centerx = self.screen_rect.centerx - coor_x
            self.rect.centery = self.screen_rect.centery + coor_y
            self.player_gameover = True