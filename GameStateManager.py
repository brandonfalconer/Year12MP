import MenuState
import RulesState


class GameStateManager:
    def __init__(self, game_state):
        self.game_state = game_state
        self.menu = MenuState.Menu()
        self.rules = RulesState.Rules()

    def render(self):
        if self.game_state == 0:
            self.menu.render()
        elif self.game_state == 1:
            self.rules.render()

    def input(self):
        if self.game_state == 0:
            self.menu.input()
        elif self.game_state == 1:
            self.rules.input()
