import pygame
from pygame import *
import sys

import common.common as common
import classes.buttons.nice_button_2 as button


def main():
    pygame.init()

    # Setup the window
    pygame.display.set_caption("Tic Tac Toe")
    game_display = pygame.display.set_mode((common.window_size_x, common.window_size_y))
    logo_image = pygame.image.load("../resources/logo.png")
    pygame.display.set_icon(logo_image)
    fps_clock = pygame.time.Clock()

    button_join_to_server = button.button(pygame, (100, 100), "Join to server", 50)

    # Main loop
    while True:
        for event in pygame.event.get():
            # Proper exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps_clock.tick(30)


if __name__ == '__main__':
    main()
