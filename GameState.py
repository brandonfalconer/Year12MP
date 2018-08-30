import AssetLoaderLibrary
import ButtonLibrary


class GameState:
    def __init__(self):
        self.AssetLoader = AssetLoaderLibrary.AssetLoader()

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 205)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (230, 230, 0)
        self.PURPLE = (255, 0, 255)
        self.CYAN = (0, 255, 255)
        self.WHITE = (255, 255, 255)

    def render(self):
        pass

    def input(self):
        # update game button input
        game_button = ButtonLibrary.GameButton(0, 0, 0, 0)
        game_button.update_mouse()
