import pygame

buttons = []


# Simple class that draws a clickable button, with text
class GameButton:
    def __init__(self, x, y, width, height, colour, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.pressed = False
        self.cursor = False
        self.alpha = 200
        self.screen = pygame.display.set_mode([1280, 720])

        pygame.font.init()
        self.font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 36)

    def draw(self):
        # Drawing a rectangle
        s = pygame.Surface((self.width, self.height))

        if self.cursor:
            s.set_alpha(self.alpha/2)
        else:
            s.set_alpha(self.alpha)

        s.fill(self.colour)
        self.screen.blit(s, (self.x, self.y))

        #pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.width, self.height))

        # Drawing Text
        text = self.font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text, (self.x + 50, (self.y + self.height / 2 - 10)))
