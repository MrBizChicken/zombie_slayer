from constants import *
import pygame
import player
from pygame import mixer
mixer.init()


pygame.init()


clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
player_group = pygame.sprite.Group()

player = player.Player()
player_group.add(player)

pygame.init()


def main():


    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()

        draw()
        update()
        pygame.display.flip()

    pygame.quit()




def draw():
    surface.fill((0, 200, 0))
    player_group.draw(surface)


def update():
    player_group.update()



if __name__ == "__main__":
    main()
