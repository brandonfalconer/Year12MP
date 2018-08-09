import ButtonLibrary
import GameState

BLUE = (0, 0, 255)

start_button = ButtonLibrary.GameButton(100, 100, 200, 200, BLUE, "Start", False)
buttons = []
buttons.append(start_button)


class Menu():
    #@staticmethod
    def render(self):
        start_button.draw()
