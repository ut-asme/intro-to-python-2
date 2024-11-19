import random
import sys

import pygame


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

        self.position = pygame.math.Vector2(self.rect.midleft)

        self.gravity = 4
        self.vertical_velocity = 0
        self.jump_power = -1.2

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

    def is_offscreen(self, screen_height):
        """
        If the player is offscreen
        """
        return self.position.y > screen_height + 36 or self.position.y < -36


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, screen_height, sprite_group):
        """
        Initializes an obstacle
        """
        super().__init__(sprite_group)

        img = pygame.image.load("assets/hill.png")
        img = pygame.transform.scale_by(img, 3)

        vertical_offset = random.randint(0, screen_height // 6)
        orientation = random.choice(["up", "down"])
        if orientation == "up":
            self.image = img
            self.rect = self.image.get_rect(
                bottomleft=(x, screen_height + vertical_offset)
            )
            self.position = pygame.math.Vector2(self.rect.bottomleft)
        else:
            self.image = pygame.transform.rotate(img, 180)
            self.rect = self.image.get_rect(topleft=(x, -vertical_offset))
            self.position = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt, speed, screen_width):
        """
        Handles updates to the obstacle objects
        """
        # Moves them left
        self.position.x -= speed * dt
        self.rect.x = round(self.position.x)

    def is_offscreen(self):
        """
        Returns True if obstacle is offscreen
        """
        return self.rect.x + 144 <= 0


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
        self.player = Player(144, self.size[1] // 2, self.all_sprites)

        # Make obstacles
        self.obstacle_speed = 400
        self.obstacles = []
        for i in range(4):
            self.obstacles.append(
                Obstacle(
                    self.size[0] // 2 + self.size[0] // 4 * i,
                    self.size[1],
                    self.all_sprites,
                )
            )

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

            for i, obstacle in enumerate(self.obstacles):
                obstacle.update(dt, self.obstacle_speed, self.size[0])
                if obstacle.is_offscreen():
                    # Replace with a new obstacle object
                    obstacle.kill()
                    self.obstacles[i] = Obstacle(
                        self.size[0], self.size[1], self.all_sprites
                    )

            self.check_collisions()

            self.all_sprites.draw(self.window_surface)

            pygame.display.flip()

    def check_collisions(self):
        """
        Handles collisions between the player and world
        """
        if self.player.is_offscreen(self.size[1]):
            sys.exit()

        for obstacle in self.obstacles:
            if pygame.sprite.collide_mask(self.player, obstacle):
                sys.exit()


# Main function
if __name__ == "__main__":
    game = Game()

    game.run()
