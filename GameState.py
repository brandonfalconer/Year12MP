import AssetLoaderLibrary


class GameState:
    def __init__(self):
        self.AssetLoader = AssetLoaderLibrary.AssetLoader()

        # Define some colors
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (230, 230, 0)
        self.PURPLE = (255, 0, 255)
        self.CYAN = (0, 255, 255)
        self.WHITE = (255, 255, 255)

    def render(self):
        pass

    def input(self):
        pass

    def dispose(self):
        pass
