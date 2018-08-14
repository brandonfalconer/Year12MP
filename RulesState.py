from GameState import GameState
import ButtonLibrary


class Rules(GameState):
    def __init__(self):
        super().__init__()

    def render(self):
        from Main import screen
        screen.fill(self.BLUE)

    def input(self):
        pass
