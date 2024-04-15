import sys
import pygame

from settings import Settings
from ship import Ship

"""
# TODO
- Game Character: Find a bitmap image of a game character you like or
convert an image to a bitmap. Make a class that draws the character at the
center of the screen, then match the background color of the image to the background color of the screen or vice versa.

"""

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)            
            self.ship.blitme()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()