import pygame


def button(screen, position, text, size, color, bg):
    font = pygame.font.SysFont("Arial", size)
    # text_render = font.render(text, True, color)
    text_render = font.render(text, False, color)
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w + 1, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, bg, (x, y, w + 2, h))
    return screen.blit(text_render, (x, y))
