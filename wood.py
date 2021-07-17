from constants import *
import pygame
import random
import player
from main_block import *
import main_block
class Wood(main_block.Main_block):
    def __init__(self):
        super().__init__()
        self.image.fill((139, 69, 19))
