from constants import *
import pygame
import player
import hot_bar
import zombie
import wood
import main_block
import door
from pygame import mixer
mixer.init()


pygame.init()


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
all_sprites = pygame.sprite.Group()
hot_bar_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(player.Player((300, 220)), zombie.Zombie(), main_block.Main_block(), door.Door(), wood.Wood())



rows = 1
cols = 10
width = 4 + GAME_WIDTH // cols
height = (GAME_HEIGHT // 2)  // rows

for c in range(cols):

    for r in range(rows):
        hot_bar_group.add(hot_bar.Hot_bar(c * width, r * height + GAME_HEIGHT - 50, 50, 50))



pygame.init()




def main():


    running = True

    while running:
        clock.tick(TICK_RATE)
        # pos = pygame.mouse.get_pos()
        # print(pos)
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
    all_sprites.draw(surface)
    hot_bar_group.draw(surface)


def update():
    all_sprites.update()
    hot_bar_group.update()




if __name__ == "__main__":
    main()
