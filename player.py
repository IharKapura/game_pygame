import pygame, pathlib
from pathlib import Path
from level import Level
from pygame.sprite import Sprite

class Player(Sprite):

    lookright = True
    def __init__(self,screen):
        #инициализация игрока
        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.Surface((77, 54))
        self.image = pygame.image.load(Path("images","player.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, 60, 50)
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - 900
        self.rect.centery = self.screen_rect.centery + 450
        self.cube_list = []

        #Переменные для изменения движения персонажа
        self.change_x = 0
        self.change_y = 0

        #Для прыжка
        self.is_jump = False
        self.jump_count = 7

        #Картинки для персонажа
        self.walk_left = [
            pygame.image.load(Path("images","player_left","_br_m_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","_br_m_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","_br_m_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","_br_m_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","_br_m_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_left","_br_m_l_6.png")).convert_alpha(),
        ]
        self.walk_right = [
            pygame.image.load(Path("images","player_right","_br_m_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","_br_m_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","_br_m_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","_br_m_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","_br_m_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_right","_br_m_r_6.png")).convert_alpha(),
        ]
        self.fight_left = [
            pygame.image.load(Path("images","player_fight","_fight_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_6.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_l_6.png")).convert_alpha(),
        ]
        self.fight_right = [
            pygame.image.load(Path("images","player_fight","_fight_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_1.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_2.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_3.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_4.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_5.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_6.png")).convert_alpha(),
            pygame.image.load(Path("images","player_fight","_fight_r_6.png")).convert_alpha(),
        ]
        self.image_jump_rl = [ 
            pygame.image.load(Path("images","jump","_jump_up_r.png")).convert_alpha(),
            pygame.image.load(Path("images","jump","_jump_dn_r.png")).convert_alpha(),
            pygame.image.load(Path("images","jump","_jump_up_l.png")).convert_alpha(),
            pygame.image.load(Path("images","jump","_jump_dn_l.png")).convert_alpha(),
        ]

        #Пустое изображение
        self.blank_image = pygame.image.load(Path("images","_blank_image.png")).convert_alpha()

        self.player_animw_count = 0
        self.player_animf_count = 0


    #обновление позиции игрока
    def update_player(self, level):

        self.gravitation()
        self.chek_collision(level)

        #левая граница экрана
        if self.rect.left < 0:
            self.rect.left = 0


    def chek_collision(self, level):

        #Движение персонажа по оси Х
        self.rect.x += self.change_x

        #Проверка столкновения с другими объектами по Х
        block_hit_list = pygame.sprite.spritecollide(self, level.platforms, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
        
        #Движение персонажа по оси У
        self.rect.y += self.change_y

        #Проверка столкновения с другими объектами по У
        block_hit_list = pygame.sprite.spritecollide(self, level.platforms, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

			# Остановка движения по У
            self.change_y = 0



    
    # Гравитация
    def gravitation(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.95

		# Если уже на земле, то ставим позицию Y как 0
        if self.rect.y >= 1020 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 1020 - self.rect.height

    
    #Прыжок
    def jump(self, level):
        
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, level.platforms, False)
        self.rect.y -= 10

		# Если все в порядке, прыгаем вверх
        if len(platform_hit_list) > 0 or self.rect.bottom >= 1020:
            self.change_y = -15
    

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


    #Поворот изоброжения по вертикали
    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
    
                        
    # Отрисовка игрока
    def draw_player(self):
        keys = pygame.key.get_pressed()

        #Анимация движения влево
        if keys[pygame.K_a]:
            if self.player_animw_count == 5 :
                self.player_animw_count = 0
                self.screen.blit(self.walk_left[self.player_animw_count], self.rect)
            else:
                self.player_animw_count += 1
                self.screen.blit(self.walk_left[self.player_animw_count], self.rect)
        #Анимация движения вправо
        elif keys[pygame.K_d] :
            if self.player_animw_count == 5 :
                self.player_animw_count = 0
                self.screen.blit(self.walk_right[self.player_animw_count], self.rect)
            else:
                self.player_animw_count += 1
                self.screen.blit(self.walk_right[self.player_animw_count], self.rect)
        #Анимация атаки влево
        elif keys[pygame.K_q]:
            if self.player_animf_count == 11 :
                self.player_animf_count = 0
                self.screen.blit(self.fight_left[self.player_animf_count], (self.rect.centerx - 30, self.rect.centery - 45))
            else:
                self.player_animf_count += 1
                self.screen.blit(self.fight_left[self.player_animf_count], (self.rect.centerx - 30, self.rect.centery - 45))
        #Анимация атаки вправо
        elif keys[pygame.K_e]:
            if self.player_animf_count == 11 :
                self.player_animf_count = 1
                self.screen.blit(self.fight_right[self.player_animf_count], (self.rect.centerx - 30, self.rect.centery - 45))
            else:
                self.player_animf_count += 1
                self.screen.blit(self.fight_right[self.player_animf_count], (self.rect.centerx - 30, self.rect.centery - 45))
        else:
            self.screen.blit(self.image, self.rect)