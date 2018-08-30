import pygame


class AssetLoader:
    def __init__(self):
        # Load all external files into memory
        pygame.font.init()
        self.small_font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 24)
        self.medium_font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 36)
        self.regular_font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 48)
        self.large_font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 86)

        self.logo = pygame.image.load("Assets/Sprites/MillionaireLogoSmall.png")
        self.logo_rect = self.logo.get_rect()

        self.background = pygame.image.load("Assets/Sprites/Backgrounds.PNG")
        self.background_rect = self.background.get_rect()

        self.tick = pygame.image.load("Assets/Sprites/Tick.png")
        self.tick_rect = self.tick.get_rect()

        self.phone = pygame.image.load("Assets/Sprites/Phone.png")
        self.phone_rect = self.phone.get_rect()
