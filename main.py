# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # DeltaTime in seconds
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Pygame Quit")
                sys.exit()

        for thing in updatable:
            thing.update(dt)

        # Draw
        screen.fill((0, 0, 0))
        for thing in drawable:
            thing.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
            if asteroid.collision(player):
                print("Game over")
                print(f"Asteroid: {asteroid.position}")
                print(f"Player:   {player.position}")
                sys.exit()

        pygame.display.flip()  # Updates display, call last

        dt = clock.tick(60) / 1000  # Wait 1/60th of a sec


if __name__ == "__main__":
    main()
