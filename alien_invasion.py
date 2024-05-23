import sys
import pygame

from settings import Settings
from ship import Ship

"""
12-4. Rocket: Make a game that begins with a rocket in the center of the screen.
Allow the player to move the rocket up, down, left, or right using the four arrow
keys. Make sure the rocket never moves beyond any edge of the screen.
12-5. Keys: Make a Pygame file that creates an empty screen. In the event loop,
print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run
the program and press various keys to see how Pygame responds.
"""

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)            
        self.ship.blitme()

        pygame.display.flip()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()