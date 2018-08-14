import pygame
import ButtonLibrary
from GameState import GameState


class Menu(GameState):
    def __init__(self):
        super().__init__()
        
        game_button = ButtonLibrary.GameButton

        self.start_button = game_button(240, 400, 200, 100, self.YELLOW, "Start")
        ButtonLibrary.buttons.append(self.start_button)
        self.rules_button = game_button(540, 400, 200, 100, self.YELLOW, "Rules")
        ButtonLibrary.buttons.append(self.rules_button)
        self.exit_button = game_button(840, 400, 200, 100, self.YELLOW, "Exit")
        ButtonLibrary.buttons.append(self.exit_button)

    def render(self):
        from Main import GSM, screen

        # Draw Background
        screen.fill(self.BLUE)
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

        # Draw and update buttons
        self.start_button.draw(screen)
        self.rules_button.draw(screen)
        self.exit_button.draw(screen)

        ButtonLibrary.GameButton.DrawRoundRect(self.start_button, screen, self.YELLOW, pygame.Rect(100, 100, 200, 100), 0, 32, 32)

        if self.start_button.pressed:
            GSM.game_state = 2

        if self.rules_button.pressed:
            GSM.game_state = 1

        if self.exit_button.pressed:
            pygame.quit()

        # Drawing Text
        text = self.AssetLoader.large_font.render("Who wants to be a", True, (255, 255, 255))
        screen.blit(text, (390, 100))
        text_newline = self.AssetLoader.large_font.render("Millionaire?", True, (255, 255, 255))
        screen.blit(text_newline, (490, 200))

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
