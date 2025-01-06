import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), center=self.position, radius=self.radius, width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            self.kill()
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2

        self.kill()
