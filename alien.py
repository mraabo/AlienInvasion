import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class representing a single alien. """

    def __init__(self, ai_settings, screen):
        """ Initialize alien and set starting position. """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()

        # Start each new alien near top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draw alien at its current position. """
        self.screen.blit(self.image, self.rect)
