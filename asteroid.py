from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.asteroid_color = (255,255,255)

    def draw(self, screen):
        pygame.draw.circle(screen, self.asteroid_color,(self.position.x,self.position.y),self.radius )

    def update(self, dt):
        self.position += self.velocity * dt