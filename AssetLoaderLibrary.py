import pygame


class AssetLoader:
    def __init__(self):

        pygame.font.init()
        self.regular_font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 48)
        self.large_font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 86)

        self.logo = pygame.image.load("Assets/Sprites/MillionaireLogo.jpg")
        self.logo_rect = self.logo.get_rect()

        self.background = pygame.image.load("Assets/Sprites/Backgrounds.PNG")
        self.background_rect = self.background.get_rect()
