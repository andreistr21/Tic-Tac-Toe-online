# Space invaders

import pygame


pygame.init()
size = w, h = 500, 400
main_surface = pygame.display.set_mode((size))
pygame.display.set_caption("Label")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


class Label:
    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        self.set(text)

    def set(self, text):
        self.text = font.render(text, 1, pygame.Color("White"))
        size = w, h = self.text.get_size()
        self.rect = pygame.Rect(self.x, self.y, w, h)
        self.surface = pygame.Surface(size)
        self.surface.blit(self.text, (0, 0))


lab1 = Label("Click me", 0, 0)

def main():

    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mx, my = pygame.mouse.get_pos()
                    if lab1.rect.collidepoint(mx, my):
                        lab1.set("You clicked me")

        main_surface.blit(lab1.surface, (0, 0))
        pygame.display.update()
        clock.tick(60)
    # when press quit button it exit
    pygame.quit()


main()
