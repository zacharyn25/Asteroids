import pygame
from constants import *
from player import *

def main():
    #Initialze the pygame
    pygame.init()

    #Create Clock Object 
    clock = pygame.time.Clock()
    dt = 0 #delta time

    #Create display screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Create a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        #This allows the ability close the pygame window via the 'x' in the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Fills the pygame display with a black background
        screen.fill((0,0,0))

        #Draw the player object 
        player.draw(screen)

        #Update player position
        player.update(dt)

        #Updates the pygame display each iteration
        pygame.display.flip()

        #Update at 60 FPS
        time_since_called = clock.tick(60) #(seconds)
        dt = time_since_called / 1000 #(milliseconds)

if __name__ == "__main__":
    main()