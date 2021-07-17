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
player_group = pygame.sprite.Group()
hot_bar_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
wood_group = pygame.sprite.Group()
main_block_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()



wood = wood.Wood()
wood_group.add(wood)
player = player.Player()
player_group.add(player)
zombie = zombie.Zombie()
zombie_group.add(zombie)
main_block = main_block.Main_block()
main_block_group.add(main_block)
door = door.Door()
door_group.add(door)




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
    player_group.draw(surface)
    hot_bar_group.draw(surface)
    zombie_group.draw(surface)
    wood_group.draw(surface)
    door_group.draw(surface)


def update():
    player_group.update(zombie_group, main_block_group)
    hot_bar_group.update()
    zombie_group.update()
    wood_group.update()
    main_block_group.update()
    door_group.update()




if __name__ == "__main__":
    main()
