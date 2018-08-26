import pygame

buttons = []


# Simple class that draws a clickable rounded rectangle button, with text
class GameButton:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pressed = False
        self.cursor = False
        self.alpha = 150
        self.rect = pygame.Rect(x, y, width, height)

        pygame.font.init()
        self.font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 36)

    def rounded_rectangle(self, screen, colour, text, t_colour, r_width, xr, yr):

        # Highlight
        if self.cursor and colour == (230, 230, 0):
            new_colour = (200, 200, 0)
        elif self.cursor and colour == (0, 0, 205):
            new_colour = (0, 0, 240)
        else:
            new_colour = colour

        # Drawing a rounded rectangle button - source
        clip = screen.get_clip()

        # left and right
        screen.set_clip(clip.clip(self.rect.inflate(0, -yr * 2)))
        pygame.draw.rect(screen, new_colour, self.rect.inflate(1 - r_width, 0), r_width)

        # top and bottom
        screen.set_clip(clip.clip(self.rect.inflate(-xr * 2, 0)))
        pygame.draw.rect(screen, new_colour, self.rect.inflate(0, 1 - r_width), r_width)

        # top left corner
        screen.set_clip(clip.clip(self.rect.left, self.rect.top, xr, yr))
        pygame.draw.ellipse(screen, new_colour, pygame.Rect(self.rect.left, self.rect.top, 2 * xr, 2 * yr), r_width)

        # top right corner
        screen.set_clip(clip.clip(self.rect.right - xr, self.rect.top, xr, yr))
        pygame.draw.ellipse(screen, new_colour, pygame.Rect(self.rect.right - 2 * xr, self.rect.top, 2 * xr, 2 * yr), r_width)

        # bottom left
        screen.set_clip(clip.clip(self.rect.left, self.rect.bottom - yr, xr, yr))
        pygame.draw.ellipse(screen, new_colour, pygame.Rect(self.rect.left, self.rect.bottom - 2 * yr, 2 * xr, 2 * yr), r_width)

        # bottom right
        screen.set_clip(clip.clip(self.rect.right - xr, self.rect.bottom - yr, xr, yr))
        pygame.draw.ellipse(screen, new_colour, pygame.Rect(self.rect.right - 2 * xr, self.rect.bottom - 2 * yr, 2 * xr, 2 * yr), r_width)

        screen.set_clip(clip)

        # Drawing Text
        text = self.font.render(text, True, t_colour)
        screen.blit(text, (self.x + 60, (self.y + self.height / 2 - 25)))

    def circle(self, screen, colour, text, t_colour, radius, width):

        # Drawing a circle button
        if self.cursor and colour == (230, 230, 0):
            new_colour = (200, 200, 0)
        elif self.cursor and colour == (0, 0, 205):
            new_colour = (0, 0, 240)
        else:
            new_colour = colour

        pygame.draw.circle(screen, new_colour, (self.x, self.y), radius, width)

        text = self.font.render(text, True, t_colour)
        screen.blit(text, ((self.x / 2) - 5, (self.y + self.height / 2 - 25)))

    def update_mouse(self):
        from Main import event

        # Highlight if the cursor is hovering over the button
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        for button in buttons:
            if (button.x < mouse_x < button.x + button.width) and (
                    button.y < mouse_y < button.y + button.height):
                button.cursor = True
            else:
                button.cursor = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

                for button in buttons:
                    if (button.x < mouse_x < button.x + button.width) and (
                            button.y < mouse_y < button.y + button.height):
                        button.pressed = True
                    else:
                        button.pressed = False