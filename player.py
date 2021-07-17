from constants import *
import pygame
import random
import wood
import zombie
import math
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
        self.xmouse, self.ymouse = pygame.mouse.get_pos()
        self.angle = math.atan2(self.ymouse-self.y, self.xmouse-self.x)


    def update(self, main_block_group, zombie_group):
        self.key_input()

        if pygame.sprite.spritecollide(self, zombie_group, False):
            self.image.fill((236, 0, 0))


        else:
            self.image.fill((255, 255 ,255))


        if pygame.sprite.spritecollide(self, main_block_group, False):
            self.speed = 0


        else:
            self.speed = 5




    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x += -self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed



        if keys[pygame.K_UP]:
            self.rect.y += -self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
