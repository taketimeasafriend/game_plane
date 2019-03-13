import pygame
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print("init game...")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__creat_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __creat_sprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("enemys are coming...")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 1
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -1
        else:
            self.hero.speed = 0

    def __event_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemys = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemys) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        pygame.display.update()

    @staticmethod
    def __game_over():
        print("exit game...")
        pygame.quit()
        exit()

    def start_game(self):
        print("game begin...")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__event_collide()
            self.__update_sprites()

            # screen.blit(bg, (0, 0))
            # screen.blit(hero, (110, 400))
            # enemy_group.update()
            # enemy_group.draw(screen)


if __name__ == '__main__':

    game = PlaneGame()
    game.start_game()
