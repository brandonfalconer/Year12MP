import pygame
import ButtonLibrary
from GameState import GameState


class Menu(GameState):
    def __init__(self):
        from Main import SCREEN_HEIGHT, SCREEN_WIDTH
        super().__init__()

        #pygame.font.init()
        #self.font = pygame.font.Font("Assets/Fonts/Tahoma.ttf", 64)

        self.start_button = ButtonLibrary.GameButton(200, 600, 200, 100, self.YELLOW, "Start", False)
        ButtonLibrary.buttons.append(self.start_button)
        self.rules_button = ButtonLibrary.GameButton(500, 600, 200, 100, self.YELLOW, "Rules", False)
        ButtonLibrary.buttons.append(self.rules_button)
        self.exit_button = ButtonLibrary.GameButton(800, 600, 200, 100, self.YELLOW, "Exit", False)
        ButtonLibrary.buttons.append(self.exit_button)

    def render(self):
        from Main import GSM, screen
        screen.fill(self.BLUE)

        self.start_button.draw()
        self.rules_button.draw()
        self.exit_button.draw()

        if self.start_button.pressed:
            GSM.game_state = 2

        if self.rules_button.pressed:
            GSM.game_state = 1

        if self.exit_button.pressed:
            pygame.quit()

        # Drawing Text
        text = self.AssetLoader.regular_font.render("Who wants to be a Millionaire?", True, (0, 0, 0))
        screen.blit(text, (300, 800))

    def input(self):
        from Main import event

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                print("click")

                for button in ButtonLibrary.buttons:
                    if (button.x < mouse_x < button.x + button.width) and (
                            button.y < mouse_y < button.y + button.height):
                        button.pressed = True
                        print("pressed")
