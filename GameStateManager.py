import MenuState
import RulesState

menu = MenuState.Menu
rules = RulesState.Rules


class GameState:

    def __init__(self, game_state):
        self.game_state = game_state

    def render(self):
        if self.game_state == 0:
            menu.render()
        elif self.game_state == 1:
            rules.render()
