import pygame
import sys

# Initialize pygame stuff
pygame.init()

# How big we want our window in pixels
# width, height
size = 1280, 720

# Open a window with our desired size
screen = pygame.display.set_mode(size)

# Our main game loop
while True:
    # Stop the program if the window is closed or
    # escape is pressed on the keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

    screen.fill(pygame.Color(0, 0, 0))

    pygame.display.flip()
