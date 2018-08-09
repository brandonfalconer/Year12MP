import ButtonLibrary
import GameState
import Main

BLUE = (0, 0, 255)

start_button = ButtonLibrary.GameButton(100, 100, 200, 200, BLUE, "Start", False)
Main.buttons.append(start_button)


class Menu(GameState):
    #@staticmethod
    def render(self):
        start_button.draw()
