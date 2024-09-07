# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    #Initialze the pygame
    pygame.init()

    #Create Clock Object 
    clock = pygame.time.Clock()
    dt = 0 #delta time

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

        #Update at 60 FPS
        time_since_called = clock.tick(60) #(s)
        dt = time_since_called / 1000 #(ms)

if __name__ == "__main__":
    main()