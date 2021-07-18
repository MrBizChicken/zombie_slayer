# from constants import *
# import pygame
# import random
# import wood
# import zombie
# import math
# from pygame.math import Vector2
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#
#         self.width = 32
#         self.height = 32
#         self.x = 0
#         self.y = 0
#         self.speed = 5
#         self.image = pygame.Surface((self.width, self.height))
#         self.image.fill((255, 255 ,255))
#         self.rect = pygame.Rect(self.image.get_rect())
#         self.rect.topleft = (self.x, self.y)
#
#
#
#
#
#     def update(self, main_block_group, zombie_group):
#         self.key_input()
#
#         if pygame.sprite.spritecollide(self, zombie_group, False):
#             self.image.fill((236, 0, 0))
#
#
#         else:
#             self.image.fill((255, 255 ,255))
#
#
#         if pygame.sprite.spritecollide(self, main_block_group, False):
#             self.speed = 0
#
#
#         else:
#             self.speed = 5
#
#
#
#
#     def key_input(self):
#
#         keys = pygame.key.get_pressed()
#
#         if keys[pygame.K_LEFT]:
#             self.rect.x += -self.speed
#
#         if keys[pygame.K_RIGHT]:
#             self.rect.x += self.speed
#
#
#
#         if keys[pygame.K_UP]:
#             self.rect.y += -self.speed
#
#         if keys[pygame.K_DOWN]:
#             self.rect.y += self.speed

import pygame as pg
from pygame.math import Vector2
from pprint import pprint

class Player(pg.sprite.Sprite):

    def __init__(self, pos):

        super().__init__()
        self.image = pg.image.load("player.png")
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.speed = 5
        self.pos = Vector2(pos)
        pprint(pg.color.THECOLORS)

    def update(self):
        self.rotate()
        self.key_input()


    def rotate(self):
        # The vector to the target (the mouse position).
        direction = pg.mouse.get_pos() - self.pos
        # .as_polar gives you the polar coordinates of the vector,
        # i.e. the radius (distance to the target) and the angle.
        radius, angle = direction.as_polar()
        # Rotate the image by the negative angle (y-axis in pygame is flipped).
        self.image = pg.transform.rotate(self.orig_image, -angle)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)

    def key_input(self):

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.rect.x += -self.speed

        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed



        if keys[pg.K_UP]:
            self.rect.y += -self.speed

        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
