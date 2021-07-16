from constants import *
import pygame
import random
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 32
        self.height = 32
        self.x = 0
        self.y = 0
        self.speed = 5
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255 ,255))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)

    def update(self, zombie_group):
        self.key_input()
        if pygame.sprite.spritecollide(self, zombie_group, False):
            self.image.fill((236, 0, 0))


        else:
            self.image.fill((255, 255 ,255))    






    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            if self.rect.x > 0:
                self.rect.x += -self.speed

        if keys[pygame.K_RIGHT]:
            if self.rect.left < GAME_WIDTH:
                self.rect.x += self.speed



        if keys[pygame.K_UP]:

            if self.rect.y > 0:
                self.rect.y += -self.speed

        if keys[pygame.K_DOWN]:
            if self.rect.top < GAME_HEIGHT:
                self.rect.y += self.speed
