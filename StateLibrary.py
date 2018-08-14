import pygame


class State:
    # Global Constants
    # Define some colors
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)
    WHITE = (255, 255, 255)

    # Screen dimensions
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    # Variables
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    buttons = []

    def __init__(self):
        pass