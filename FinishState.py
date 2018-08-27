from GameState import GameState
import ButtonLibrary


class Finish(GameState):
    def __init__(self):
        super().__init__()

        self.exit_button = ButtonLibrary.GameButton
        ButtonLibrary.buttons.append(self.exit_button)

    def render(self):
        from Main import screen, GSM

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)
        screen.blit(self.AssetLoader.logo, (300, 200, 100, 300))

        self.exit_button.circle(screen, self.BLUE, "Exit", self.BLACK)

    def input(self):
        pass
