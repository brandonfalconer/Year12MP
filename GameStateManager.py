import MenuState
import RulesState
import PlayState


class GameStateManager:
    def __init__(self, game_state):
        self.game_state = game_state
        self.menu = MenuState.Menu()
        self.rules = RulesState.Rules()
        self.play = PlayState.Play()

    def render(self):
        if self.game_state == 0:
            self.menu.render()
        elif self.game_state == 1:
            self.rules.render()
        elif self.game_state == 2:
            self.play.render()

    def input(self):
        if self.game_state == 0:
            self.menu.input()
        elif self.game_state == 1:
            self.rules.input()
        elif self.game_state == 2:
            self.play.input()
