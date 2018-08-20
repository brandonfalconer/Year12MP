import pygame
from GameState import GameState
import ButtonLibrary


class Rules(GameState):
    def __init__(self):
        super().__init__()

        game_button = ButtonLibrary.GameButton
        self.back_button = game_button(100, 600, 200, 100)
        ButtonLibrary.buttons.append(self.back_button)

    def render(self):
        from Main import GSM, screen
        screen.fill(self.BLUE)

        self.back_button.draw(screen, self.YELLOW, "Back", 0, 32, 32)

        if self.back_button.pressed:
            GSM.game_state = 0
            GSM.menu.__init__()

    def input(self):
        from Main import event

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

                for button in ButtonLibrary.buttons:
                    if (button.x < mouse_x < button.x + button.width) and (
                            button.y < mouse_y < button.y + button.height):
                        button.pressed = True
                    else:
                        button.pressed = False
