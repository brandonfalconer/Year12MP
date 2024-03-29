import pygame
import ButtonLibrary
from GameState import GameState
import sys


class Menu(GameState):
    def __init__(self):
        super().__init__()

        # Initiate Buttons
        game_button = ButtonLibrary.GameButton
        self.start_button = game_button(240, 400, 200, 100)
        self.rules_button = game_button(540, 400, 200, 100)
        self.exit_button = game_button(840, 400, 200, 100)
        ButtonLibrary.buttons.extend((self.start_button, self.rules_button, self.exit_button))

        pygame.mixer.music.load("Assets/Sound/Main Theme.mp3")
        pygame.mixer.music.play(-1)

    def render(self):
        from Main import GSM, screen

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

        # Draw and update buttons
        self.start_button.rounded_rectangle(screen, self.YELLOW, "Start", self.BLACK, 0, 32, 32)
        self.rules_button.rounded_rectangle(screen, self.YELLOW, "Rules", self.BLACK, 0, 32, 32)
        self.exit_button.rounded_rectangle(screen, self.YELLOW, "Exit", self.BLACK,0, 32, 32)

        if self.start_button.pressed:
            pygame.mixer.music.stop()
            GSM.game_state = 2
            GSM.play.__init__()

        if self.rules_button.pressed:
            GSM.game_state = 1
            GSM.rules.__init__()

        if self.exit_button.pressed:
            pygame.quit()
            sys.exit()

        # Drawing Text
        text = self.AssetLoader.large_font.render("Who wants to be a", True, (255, 255, 255))
        screen.blit(text, (290, 100))
        text_newline = self.AssetLoader.large_font.render("Millionaire?", True, (255, 255, 255))
        screen.blit(text_newline, (435, 200))

    def input(self):
        GameState.input(self)
