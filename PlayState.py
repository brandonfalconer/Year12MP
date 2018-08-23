from GameState import GameState
import ButtonLibrary


class Play(GameState):
    def __init__(self):
        super().__init__()

        from Main import screen
        self.screen = screen

    def render(self):
        from Main import screen

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

        screen.blit(self.AssetLoader.logo, (300, 100, 100, 300))

    def input(self):
        pass
