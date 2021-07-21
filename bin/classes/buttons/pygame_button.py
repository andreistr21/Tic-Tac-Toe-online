import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


class Button:
    "Create a button, then blit the surface in the while loop"

    def __init__(self, text,  x=0, y=0, bg="black"):
        self.x = 0
        self.y = 0
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])


button1 = Button("Click here", x=10, y= 10, bg="navy")

def show_button1():
    screen.blit(button1.surface, (button1.x, button1.y))


def button1_click(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            if button1.rect.collidepoint(x, y):
                button1.change_text("You clicked me", bg="red")


loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        button1_click(event)
    show_button1()
    pygame.display.update()
    clock.tick(30)

pygame.quit()
