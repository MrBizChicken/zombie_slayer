from constants import *
import pygame
import random
import player
from main_block import *
import main_block
class Door(main_block.Main_block):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 64
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.center = self.rect.center



    def update(self):
        self.key_input()



    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.image = pygame.Surface((64, 10))
            self.image.fill((255, 255, 255))
            self.rect = pygame.Rect(self.image.get_rect())
            self.rect.center = self.rect.center




        elif keys[pygame.K_r]:
            self.image = pygame.Surface((10, 64))
            self.image.fill((255, 255, 255))
            self.rect = pygame.Rect(self.image.get_rect())
            self.rect.center = self.rect.center
