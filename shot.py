import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    #def __init__(self, x, y, rotation):
    def __init__(self, position, rotation):
        x, y = position
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
