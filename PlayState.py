from GameState import GameState
import ButtonLibrary


class Play(GameState):
    def __init__(self):
        super().__init__()

        from Main import screen
        self.screen = screen

    def render(self):
        self.screen.fill(self.BLUE)

    def input(self):
        pass
