from constants import *
import pygame
import random
import player
from main_block import *
import main_block
class Health(main_block.Main_block):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 20
        self.x = 0
        self.y = 0
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 90, 0))
        self.rect = pygame.Rect(self.image.get_rect())
