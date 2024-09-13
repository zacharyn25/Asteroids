import pygame

# Base class for game objects - inherits the pygame.sprite.Sprite class functionality
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    #Check if the Asteroid and Player Collide
    def checkCollision(self, object):
        distance_to = self.position.distance_to(object.position)
        
        if (distance_to <= (self.radius + object.radius)):
            return True
        return False