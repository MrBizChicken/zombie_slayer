from constants import *
import pygame
import random
import player
class Main_block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 64
        self.height = 64
        self.x = random.randint(0, GAME_WIDTH)
        self.y = random.randint(0, GAME_HEIGHT)
        self.speed = 2
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 200, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)

    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            print("block gained!")
