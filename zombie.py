from constants import *
import pygame
import random
import player
class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 32
        self.height = 32
        self.x = 30
        self.y = 200
        self.speed = 2
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 109 ,0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.player = player.Player()

    def update(self):
        if self.player.x > self.x:
            self.rect.x += -self.speed
