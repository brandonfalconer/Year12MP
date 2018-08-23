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

    def rounded_rectangle(self, screen, colour, text, r_width, xr, yr):

        # Highlight
        if self.cursor and colour == (230, 230, 0):
            new_colour = (200, 200, 0)
        else:
            new_colour = colour

        # Drawing a rounded rectangle
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
        text = self.font.render(text, True, (0, 0, 0))
        screen.blit(text, (self.x + 60, (self.y + self.height / 2 - 25)))

        # Drawing a rectangle
        #s = pygame.Surface((self.width, self.height))

        #if self.cursor:
        #    s.set_alpha(self.alpha/1.1)
        #else:
        #    s.set_alpha(self.alpha)

        #s.fill(self.colour)
        #screen.blit(s, (self.x, self.y))
