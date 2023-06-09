import pygame

class Ship:
    """ a class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set it's staring position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('D:/python codes/From 10 May 2021 (Second Wave Python)/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at the bottom center of the screen."""
        self.screen.blit(self.image, self.rect)
