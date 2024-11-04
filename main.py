import pygame
import sys

pygame.init()

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(pygame.Color(0, 0, 0))

    pygame.display.flip()
