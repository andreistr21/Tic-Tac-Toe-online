import pygame
from pygame import *
import sys
import socket

import common.common as common
import bin.classes.buttonClass as button
import classes.textInputClass as textInput


def FillWindow(game_display):
    game_display.fill(common.color_light_gray)

    pygame.draw.line(
        game_display,
        common.color_yellow,
        (0, 150 + common.width_of_line / 2),
        (common.window_size_x, 150 + common.width_of_line / 2),
        width=common.width_of_line,
    )
    pygame.draw.line(
        game_display,
        common.color_yellow,
        (0, 306 + common.width_of_line / 2),
        (common.window_size_x, 306 + common.width_of_line / 2),
        width=common.width_of_line,
    )

    pygame.draw.line(
        game_display,
        common.color_yellow,
        (150 + common.width_of_line / 2, 0),
        (150 + common.width_of_line / 2, common.window_size_x),
        width=common.width_of_line,
    )
    pygame.draw.line(
        game_display,
        common.color_yellow,
        (306 + common.width_of_line / 2, 0),
        (306 + common.width_of_line / 2, common.window_size_x),
        width=common.width_of_line,
    )


def WhichRectangle(mouse_poz):
    if mouse_poz[0] <= 150:
        if mouse_poz[1] <= 150:
            return 0
        if 156 <= mouse_poz[1] <= 306:
            return 3
        if mouse_poz[1] >= 312:
            return 6
    if 156 <= mouse_poz[0] <= 306:
        if mouse_poz[1] <= 150:
            return 1
        if 156 <= mouse_poz[1] <= 306:
            return 4
        if mouse_poz[1] >= 312:
            return 7
    if mouse_poz[0] >= 312:
        if mouse_poz[1] <= 150:
            return 2
        if 156 <= mouse_poz[1] <= 306:
            return 5
        if mouse_poz[1] >= 312:
            return 8


def Game(game_display, state_table, rectangle_number, who_is_next, list_of_rectangles, is_end):
    if state_table[rectangle_number] is None:
        if who_is_next[0] == "cross":
            DrawCross(game_display, rectangle_number, list_of_rectangles)

            state_table[rectangle_number] = "cross"
            who_is_next[0] = "zero"
        else:
            DrawZero(game_display, rectangle_number, list_of_rectangles)

            state_table[rectangle_number] = "zero"
            who_is_next[0] = "cross"

    cross_win = CheckForWin(state_table, "cross")
    zero_win = CheckForWin(state_table, "zero")

    is_out_of_space = True

    for el in state_table:
        if el is None:
            is_out_of_space = False

    if cross_win:
        WinText("'Cross' win", game_display)
        is_end[0] = 2
    elif zero_win:
        WinText("'Zero' win", game_display)
        is_end[0] = 2
    elif is_out_of_space and not cross_win and not zero_win:
        WinText("A draw", game_display)
        is_end[0] = 2


def DrawCross(game_display, rectangle_number, list_of_rectangles):
    x = list_of_rectangles[rectangle_number][0]
    y = list_of_rectangles[rectangle_number][1]

    pygame.draw.line(
        game_display,
        common.color_black,
        (x + 10, y + 10),
        (x + 150 - 10, y + 150 - 10),
        width=13,
    )
    pygame.draw.line(
        game_display,
        common.color_black,
        (x + 10, y + 150 - 10),
        (x + 150 - 10, y + 10),
        width=13,
    )


def DrawZero(game_display, rectangle_number, list_of_rectangles):
    x = list_of_rectangles[rectangle_number][0]
    y = list_of_rectangles[rectangle_number][1]

    pygame.draw.circle(game_display, common.color_black, (x + 75, y + 75), 65, width=10)


def CheckForWin(state_table, who):
    # Check horizontal lines
    if (
            state_table[0] == f"{who}"
            and state_table[1] == f"{who}"
            and state_table[2] == f"{who}"
    ):
        return True
    elif (
            state_table[3] == f"{who}"
            and state_table[4] == f"{who}"
            and state_table[5] == f"{who}"
    ):
        return True
    elif (
            state_table[6] == f"{who}"
            and state_table[7] == f"{who}"
            and state_table[8] == f"{who}"
    ):
        return True
    # Check vertical lines
    elif (
            state_table[0] == f"{who}"
            and state_table[3] == f"{who}"
            and state_table[6] == f"{who}"
    ):
        return True
    elif (
            state_table[1] == f"{who}"
            and state_table[4] == f"{who}"
            and state_table[7] == f"{who}"
    ):
        return True
    elif (
            state_table[2] == f"{who}"
            and state_table[5] == f"{who}"
            and state_table[8] == f"{who}"
    ):
        return True
    # Check diagonals
    elif (
            state_table[0] == f"{who}"
            and state_table[4] == f"{who}"
            and state_table[8] == f"{who}"
    ):
        return True
    elif (
            state_table[2] == f"{who}"
            and state_table[4] == f"{who}"
            and state_table[6] == f"{who}"
    ):
        return True
    else:
        return False


def WinText(text, game_display):
    font = pygame.font.SysFont("Comic Sans MS", 60)
    text = font.render(text, True, common.color_green, common.color_black)
    textRect = text.get_rect()
    textRect.center = (common.window_size_x // 2, common.window_size_y // 2)
    game_display.blit(text, textRect)


def main():
    pygame.init()
    pygame.font.init()

    # Setup the window
    pygame.display.set_caption("Tic Tac Toe")
    game_display = pygame.display.set_mode((common.window_size_x, common.window_size_y))
    logo_image = pygame.image.load("../resources/logo.png")
    pygame.display.set_icon(logo_image)
    fps_clock = pygame.time.Clock()

    list_of_rectangles = [(0, 0, 150, 150), (156, 0, 150, 150), (312, 0, 150, 150),
                          (0, 156, 150, 150), (156, 156, 150, 150), (312, 156, 150, 150),
                          (0, 312, 150, 150), (156, 312, 150, 150), (312, 312, 150, 150)]

    # Init variables
    state_table = [None for _ in range(9)]  # cross / zero
    # rectangle_number = None
    who_is_next = ["cross"]  # cross / zero
    is_end = [1]  # 1 - not the end, 2 - the end

    # Init variables
    first_window_show = True
    join_to_server_window = False
    create_new_server_window = False
    game_window_client = False
    game_window_server = False
    text = None
    is_server_created = False
    server_socket = None
    client_socket = None
    is_server_turn = True
    connection = None

    text_input = textInput.TextInput(font_size=20)
    my_font = pygame.font.SysFont('Comic Sans MS', 15)
    text_server_ip = my_font.render('Server IP:', False, common.color_black)
    text_your_server_ip = my_font.render(f'Your server IP: 127.0.0.1:{common.port}', False, common.color_black)  # ToDo change IP
    text_waiting_for_another_player = my_font.render('Waiting for another player...', False, common.color_black)

    # Main loop
    while True:
        # First window
        if first_window_show:
            game_display.fill(common.color_light_gray)
            button_join_to_server = button.button(game_display, (common.window_size_x / 2 - 75, 75), "Join to server",
                                                  30, common.color_black, common.color_gray)
            button_create_new_server = button.button(game_display, (common.window_size_x / 2 - 100, 150),
                                                     "Create new server", 30, common.color_black, common.color_gray)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_join_to_server.collidepoint(pygame.mouse.get_pos()):
                        first_window_show = False
                        join_to_server_window = True

                    if button_create_new_server.collidepoint(pygame.mouse.get_pos()):
                        first_window_show = False
                        create_new_server_window = True

                # Proper exit
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        # Join to server window
        elif join_to_server_window:
            game_display.fill(common.color_light_gray)
            # Show text
            game_display.blit(text_server_ip, (10, 0))
            # Show input text
            game_display.blit(text_input.get_surface(), (10, 30))

            # Get all events and store in variable "events" fro use in two places
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        join_to_server_window = False
                        first_window_show = True

                # Proper exit
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if text_input.update(events):
                text = text_input.get_text()
                ip, port = text.split(":")
                client_socket = socket.create_connection((ip, port))
                game_window_client = True
                join_to_server_window = False

        # Create new server window
        elif create_new_server_window:
            game_display.fill(common.color_light_gray)
            # Show text
            game_display.blit(text_your_server_ip, (10, 0))
            game_display.blit(text_waiting_for_another_player, (10, 30))

            if not is_server_created:
                # Update screen, to see information, while waiting for the connection
                pygame.display.update()

                # Create the server
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_socket.bind(('127.0.0.1', common.port))
                server_socket.listen(1)
                connection, client_address = server_socket.accept()     # ToDo fix not responding error
                is_server_created = True
                game_window_server = True
                create_new_server_window = False

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        create_new_server_window = False
                        first_window_show = True

                # Proper exit
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        elif game_window_server:
            FillWindow(game_display)

            if is_server_turn:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and is_end[0] == 1:
                        mouse_poz = pygame.mouse.get_pos()
                        rectangle_number = WhichRectangle(mouse_poz)
                        rectangle_number_byte = bytes(str(rectangle_number), "utf-8")
                        connection.sendall(rectangle_number_byte)
                        Game(
                            game_display,
                            state_table,
                            rectangle_number,
                            who_is_next,
                            list_of_rectangles,
                            is_end
                        )
                    elif event.type == pygame.MOUSEBUTTONDOWN and is_end[0] == 2:
                        # Fill the window with patterns
                        FillWindow(game_display)

                        # Init variables
                        state_table = [None for _ in range(9)]  # cross / zero
                        rectangle_number = None
                        who_is_next = ["cross"]  # cross / zero
                        is_end = [1]  # 1 - not the end, 2 - the end

                        pygame.display.update()

                    # Proper exit
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            else:
                rectangle_number = int(connection.recv(1024).decode())
                Game(
                    game_display,
                    state_table,
                    rectangle_number,
                    who_is_next,
                    list_of_rectangles,
                    is_end
                )

        elif game_window_client:
            FillWindow(game_display)
            pygame.display.update()

            if not is_server_turn:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and is_end[0] == 1:
                        mouse_poz = pygame.mouse.get_pos()
                        rectangle_number = WhichRectangle(mouse_poz)
                        rectangle_number_byte = bytes(str(rectangle_number), "utf-8")
                        connection.sendall(rectangle_number_byte)
                        Game(
                            game_display,
                            state_table,
                            rectangle_number,
                            who_is_next,
                            list_of_rectangles,
                            is_end
                        )
                    elif event.type == pygame.MOUSEBUTTONDOWN and is_end[0] == 2:
                        # Fill the window with patterns
                        FillWindow(game_display)

                        # Init variables
                        state_table = [None for _ in range(9)]  # cross / zero
                        rectangle_number = None
                        who_is_next = ["cross"]  # cross / zero
                        is_end = [1]  # 1 - not the end, 2 - the end

                        pygame.display.update()

                    # Proper exit
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            else:
                rectangle_number = None
                try:
                    rectangle_number = connection.recv(1024).decode()
                    print(f"rectangle_number: {rectangle_number}")

                    Game(
                        game_display,
                        state_table,
                        rectangle_number,
                        who_is_next,
                        list_of_rectangles,
                        is_end
                    )

                    is_server_turn = True
                except Exception:
                    pass

        pygame.display.update()
        fps_clock.tick(60)


if __name__ == '__main__':
    main()
