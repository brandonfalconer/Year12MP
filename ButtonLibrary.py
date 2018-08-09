import pygame

# Variables
screen = pygame.display.set_mode([1280, 720])
pygame.font.init()
font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 30)


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

    def draw(self):
        # Drawing a rectangle
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

        # Drawing Text
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + 50, (self.y + self.height / 2 - 10)))
