import sys
import pygame

"""
# TODO
- Blue Sky: Make a Pygame window with a blue background.
- Game Character: Find a bitmap image of a game character you like or
convert an image to a bitmap. Make a class that draws the character at the
center of the screen, then match the background color of the image to the background color of the screen or vice versa.

"""

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()