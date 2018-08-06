import pygame

# Variables
screen = pygame.display.set_mode([1280, 720])
pygame.font.init()
font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 30)
i = 1

class GameButton:

    def __init__(self, x, y, width, height, colour, text, pressed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.pressed = pressed

    def update(self):
        # Checking if the button has been pressed
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1:
                    print("x:"+str(pygame.mouse.get_pos()[0]))
                    print("y:"+str(pygame.mouse.get_pos()[1]))
                    if (pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.width) and (pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.height):
                        self.pressed = True
                        self.colour = (0, 0, 0)

        # Drawing a rectangle
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

        # Drawing Text
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + 50, (self.y + self.height / 2 - 10)))