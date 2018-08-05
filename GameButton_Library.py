import pygame
import Main


class GameButton():

    def __init__(self, x, y, width, height, colour, text, pressed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.pressed = pressed

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.width:
                    if pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.height:
                        self.pressed = True

        pygame.draw.rect(Main.screen, self.colour, (self.x, self.y, self.width, self.height))