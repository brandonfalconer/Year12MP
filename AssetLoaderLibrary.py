import pygame


class AssetLoader:
    def __init__(self):

        pygame.font.init()
        self.regular_font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 32)
        self.large_font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 64)

        self.logo = pygame.image.load("Assets/Sprites/MillionaireLogo.jpg")
        self.logo_rect = self.logo.get_rect()
