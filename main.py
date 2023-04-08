# import libraries
import pygame
import math
import random

# Initialize pygame
pygame.init()

# Define the dimension of game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# FPS Settings
# create an internal clock object
clock = pygame.time.Clock()
FPS = 60

# Create a game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load images
bg = pygame.transform.scale(pygame.image.load("PygameAssets/bg/bg1.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))


# Object-Oriented Programming (OOP)
# To represent real-life objects
class Castle():
    # Constructor - It is used to create a castle instance/object/clone
    def __init__(self):
        pass


############### MAIN GAME LOOP ###############
run = True
while run:
    clock.tick(FPS)

    screen.blit(bg, (0, 0))

    # Event Handler to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Update display window on every frame
    pygame.display.update()


pygame.quit()



