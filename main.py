# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    #Initialze the pygame
    pygame.init()

    #Create display screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        #This allows the ability close the pygame window via the 'x' in the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Fills the pygame display with a black background
        screen.fill((0,0,0))
        
        #Updates the pygame display each iteration
        pygame.display.flip()

if __name__ == "__main__":
    main()