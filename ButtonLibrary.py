import pygame

buttons = []


# Simple class that draws a clickable button, with text
class GameButton:
    def __init__(self, x, y, width, height, colour, text, pressed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.pressed = pressed
        self.screen = pygame.display.set_mode([1280, 720])

        pygame.font.init()
        self.font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 30)

    def draw(self):
        # Drawing a rectangle
        pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.width, self.height))

        # Drawing Text
        text = self.font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text, (self.x + 50, (self.y + self.height / 2 - 10)))
