import pygame

screen = pygame.display.set_mode([1280, 720])


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
        # Button press
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1:
                    print("x:"+str(pygame.mouse.get_pos()[0]))
                    print("y:"+str(pygame.mouse.get_pos()[1]))
                    if (pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.width) and (pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.height):
                        self.pressed = True
                        self.colour = (0, 0, 0)

        # Draw Rectangle
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
