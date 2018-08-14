import pygame
from pygame import gfxdraw

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

        pygame.font.init()
        self.font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 36)

    def draw(self, screen):
        # Drawing a rectangle
        s = pygame.Surface((self.width, self.height))

        if self.cursor:
            s.set_alpha(self.alpha/1.1)
        else:
            s.set_alpha(self.alpha)

        s.fill(self.colour)
        screen.blit(s, (self.x, self.y))

        #pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.width, self.height))

        # Drawing Text
        text = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + 60, (self.y + self.height / 2 - 25)))

    def DrawRoundRect(self, surface, color, rect, width, xr, yr):
        clip = surface.get_clip()

        # left and right
        surface.set_clip(clip.clip(rect.inflate(0, -yr * 2)))
        pygame.draw.rect(surface, color, rect.inflate(1 - width, 0), width)

        # top and bottom
        surface.set_clip(clip.clip(rect.inflate(-xr * 2, 0)))
        pygame.draw.rect(surface, color, rect.inflate(0, 1 - width), width)

        # top left corner
        surface.set_clip(clip.clip(rect.left, rect.top, xr, yr))
        pygame.draw.ellipse(surface, color, pygame.Rect(rect.left, rect.top, 2 * xr, 2 * yr), width)

        # top right corner
        surface.set_clip(clip.clip(rect.right - xr, rect.top, xr, yr))
        pygame.draw.ellipse(surface, color, pygame.Rect(rect.right - 2 * xr, rect.top, 2 * xr, 2 * yr), width)

        # bottom left
        surface.set_clip(clip.clip(rect.left, rect.bottom - yr, xr, yr))
        pygame.draw.ellipse(surface, color, pygame.Rect(rect.left, rect.bottom - 2 * yr, 2 * xr, 2 * yr), width)

        # bottom right
        surface.set_clip(clip.clip(rect.right - xr, rect.bottom - yr, xr, yr))
        pygame.draw.ellipse(surface, color, pygame.Rect(rect.right - 2 * xr, rect.bottom - 2 * yr, 2 * xr, 2 * yr),
                            width)

        surface.set_clip(clip)