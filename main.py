from typing import override
import pygame
import sys


class Player(pygame.sprite.Sprite):
    """
    A class representing our player
    """

    def __init__(self, x, y, sprite_group):
        """
        Method to initialize our Player

        Takes an x and y value for the player position
        """

        # Make sure the sprite stuff is initialized and we
        # add the player to the game's sprite group
        super().__init__(sprite_group)

        img1 = pygame.image.load("assets/player1.png")
        img1 = pygame.transform.flip(img1, True, False)

        img2 = pygame.image.load("assets/player2.png")
        img2 = pygame.transform.flip(img2, True, False)

        self.images = [img1, img2]

        self.image = self.images[0]
        self.rect = self.image.get_rect(midleft=(x, y))

        self.position = pygame.math.Vector2()

        self.gravity = 1.5
        self.vertical_velocity = 0
        self.jump_power = -0.5

    def update(self, dt):
        """
        Handles updates to the player object
        """
        # Gravity
        self.vertical_velocity += self.gravity * dt
        self.position.y += self.vertical_velocity
        self.rect.y = round(self.position.y)

    def jump(self):
        """
        Makes the player jump and should be called from the pygame event loop
        """
        self.vertical_velocity = self.jump_power


class Game:
    """
    A class representing our Game
    """

    def __init__(self):
        """
        Initializes our game
        """

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

        # Make player
        self.player = Player(72, self.size[1] // 2, self.all_sprites)

    def run(self):
        """
        Performs all actions to make the game run
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.jump()

            # Game logic
            self.window_surface.fill(pygame.Color(173, 216, 230))

            self.player.update(dt)

            self.all_sprites.draw(self.window_surface)

            pygame.display.flip()


# Main function
if __name__ == "__main__":
    game = Game()

    game.run()
