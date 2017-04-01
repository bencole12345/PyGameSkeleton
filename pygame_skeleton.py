import os
import pygame
from pygame.locals import *


DISPLAY_SETTINGS = {
    "fps": 60,
    "window_width": 800,
    "window_height": 600,
    "max_delta_t": 0.1
}

COLOURS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}

IMAGES = {
    # List all images here, in this format:
    #     'file_path.png': None
    # assuming that all images are stored under images/<file path>
}


class Game:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((DISPLAY_SETTINGS["window_width"], DISPLAY_SETTINGS["window_height"]))
        self.clock = pygame.time.Clock()
        self.running = True
        self.initialise_images()
        self.initialise_game()

    def initialise_images(self):
        for source in IMAGES:
            IMAGES[source] = pygame.image.load(os.path.join('images', 'bla.png'))

    def initialise_game(self):

        # Set all of the gameplay variables to their initial values here.

        pass

    def start_game(self):
        while self.running:
            self.delta_t = self.clock.tick(DISPLAY_SETTINGS["fps"])
            self.delta_t = min(self.delta_t, DISPLAY_SETTINGS["max_delta_t"])
            if self.state == Game.PLAYING:
                self.handle_inputs()
                self.update_state()
                self.draw_screen()

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.terminate()
            if event.type == QUIT:
                self.terminate()

    def update_state(self):

        # Write logic here to update the game state.

        pass

    def draw_screen(self):
        self.display.fill(COLOURS["black"])

        # Write all code that draws stuff on the screen here.

        pygame.display.update()

    def terminate(self):
        self.running = False
        pygame.quit()
        raise SystemExit


def main():
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
