import pygame
from pygame import *
import sys

import common.common as common
import bin.classes.buttonClass as button
import classes.textInputClass as textInput


def main():
    pygame.init()

    # Setup the window
    pygame.display.set_caption("Tic Tac Toe")
    game_display = pygame.display.set_mode((common.window_size_x, common.window_size_y))
    logo_image = pygame.image.load("../resources/logo.png")
    pygame.display.set_icon(logo_image)
    fps_clock = pygame.time.Clock()

    game_display.fill(common.color_light_gray)

    button_join_to_server = button.button(game_display, (common.window_size_x / 2 - 75, 75), "Join to server", 30,
                                          common.color_black, common.color_gray)
    button_create_new_server = button.button(game_display, (common.window_size_x / 2 - 100, 150), "Create new server",
                                             30, common.color_black, common.color_gray)

    first_window_show = True
    join_to_server_window = False
    create_new_server_window = False

    # First window loop
    while first_window_show:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_join_to_server.collidepoint(pygame.mouse.get_pos()):
                    first_window_show = False
                    join_to_server_window = True
                    break

                if button_create_new_server.collidepoint(pygame.mouse.get_pos()):
                    first_window_show = False
                    create_new_server_window = True
                    break

            # Proper exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps_clock.tick(60)

    # Init variables
    text_input = None
    text = None

    # Fill next screen if button pushed
    if join_to_server_window or create_new_server_window:
        game_display.fill(common.color_light_gray)
        text_input = textInput.TextInput(font_size=20)

    # Join to server window window loop
    while join_to_server_window:
        game_display.fill(common.color_light_gray)

        events = pygame.event.get()
        for event in pygame.event.get():
            # Proper exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        game_display.blit(text_input.get_surface(), (10, 10))

        if text_input.update(events):
            text = text_input.get_text()
            join_to_server_window = False
            break

        pygame.display.update()
        fps_clock.tick(60)

    # Crate new server window loop
    while create_new_server_window:
        for event in pygame.event.get():

            # Proper exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps_clock.tick(60)


if __name__ == '__main__':
    main()
