#Asteroid class, inherits from the CircleShape class
import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        #Do not spawn new asteroids upon deletion
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        #Split into two new smaller Asteroids
        random_angle = random.uniform(20,50) #Angle between 20 and 50 degrees

        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-1 * random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        Asteroid_1.velocity = new_velocity_1 * 1.2
        Asteroid_2.velocity = new_velocity_2 * 1.2