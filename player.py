
import pygame as pg
from pygame.math import Vector2
from pprint import pprint
import health
import zombie

class Player(pg.sprite.Sprite):

    def __init__(self, pos):

        super().__init__()
        self.image = pg.image.load("player.png")
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.speed = 5
        self.pos = Vector2(pos)
        self.health = health.Health()
        self.zombie = zombie.Zombie()
        pprint(pg.color.THECOLORS)

    def update(self, zombie_group):
        self.rotate()
        self.key_input()
        self.health_bar(zombie_group)

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








    def health_bar(self, zombie_group):
        self.health.x = self.rect.x + 50
        self.health.y = self.rect.y + 50
        if pg.sprite.spritecollide(self, zombie_group, False):
            self.health.width = self.health.width - 5

        if self.health.width == 35:
            self.health.color = (234, 246, 0)

        if self.health.width == 15:
            self.health.color = (234, 0, 0)

        if self.health.width == 0:
            self.health.color = (0, 190, 0)
            self.health.width = 50
