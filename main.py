# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # DeltaTime in seconds

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        pygame.display.flip()  # Updates display, call last
        dt = clock.tick(60) / 1000  # Wait 1/60th of a sec


if __name__ == "__main__":
    main()
