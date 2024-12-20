from typing import override
import pygame
import sys


class Game:
    """A class representing our Game"""

    def __init__(self):
        """Initializes our game"""

        # Initialize pygame stuff
        pygame.init()

        # How big we want our window in pixels
        # width, height
        self.size = 1280, 720

        # Open a window with our desired size
        self.window_surface = pygame.display.set_mode(self.size)
        # Set window name
        pygame.display.set_caption("Angry Fly")

        # Used for consistent framerate
        self.clock = pygame.time.Clock()
        self.framerate = 60

        # Sprite group
        self.all_sprites = pygame.sprite.Group()

    def run(self):
        """
        What will happen each frame of the program running
        """

        while True:
            # Delta time
            dt = self.clock.tick() / 1000

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()

            # Game logic
            self.window_surface.fill(pygame.Color(173, 216, 230))

            pygame.display.flip()


# Main function
if __name__ == "__main__":
    game = Game()

    game.run()
