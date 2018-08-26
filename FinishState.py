from GameState import GameState
import ButtonLibrary


class Play(GameState):
    def __init__(self):
        from Main import screen
        super().__init__()

        button_library = ButtonLibrary.GameButton
        #self.ext_button = button_library.circle(screen, )

    def render(self):
        from Main import screen, GSM

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)
        screen.blit(self.AssetLoader.logo, (300, 100, 100, 300))

    def input(self):
        pass
