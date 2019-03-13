import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 320, 520)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super(GameSprite, self).__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):

    def __init__(self, is_alt=False):
        super(BackGround, self).__init__("./image/bg.png")
        if is_alt:
            self.rect.y = -SCREEN_RECT.height

    def update(self):
        super(BackGround, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):

    def __init__(self):
        super(Enemy, self).__init__("./image/enemy1.png")
        self.speed = random.randint(1, 3)
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)

    def update(self):
        super(Enemy, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            # print("enemy out, deleting...")
            self.kill()

    def __del__(self):
        pass
        # print("enemy %s is killed." % self.rect)


class Hero(GameSprite):

    def __init__(self):
        super(Hero, self).__init__("./image/plane.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 20
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        min_x = 0
        max_x = SCREEN_RECT.width-self.rect.width
        if self.rect.x <= min_x:
            self.rect.x = min_x
        elif self.rect.x >= max_x:
            self.rect.x = max_x

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx - 3
            bullet.rect.bottom = self.rect.y - i*20
            self.bullets.add(bullet)

    def __del__(self):
        pass


class Bullet(GameSprite):

    def __init__(self):
        super(Bullet, self).__init__("./image/bullet.png", -2)

    def update(self):
        super(Bullet, self).update()
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        pass

