import pygame
import ButtonLibrary
from GameState import GameState


class Menu(GameState):
    def __init__(self):
        super().__init__()
        
        game_button = ButtonLibrary.GameButton

        self.start_button = game_button(240, 400, 200, 100)
        ButtonLibrary.buttons.append(self.start_button)
        self.rules_button = game_button(540, 400, 200, 100)
        ButtonLibrary.buttons.append(self.rules_button)
        self.exit_button = game_button(840, 400, 200, 100)
        ButtonLibrary.buttons.append(self.exit_button)

    def render(self):
        from Main import GSM, screen, done

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

        # Draw and update buttons
        self.start_button.rounded_rectangle(screen, self.YELLOW, "Start", 0, 32, 32)
        self.rules_button.rounded_rectangle(screen, self.YELLOW, "Rules", 0, 32, 32)
        self.exit_button.rounded_rectangle(screen, self.YELLOW, "Exit", 0, 32, 32)

        if self.start_button.pressed:
            GSM.game_state = 2
            GSM.play.__init__()

        if self.rules_button.pressed:
            GSM.game_state = 1
            GSM.rules.__init__()

        if self.exit_button.pressed:
            done = True
            pygame.quit()

        # Drawing Text
        text = self.AssetLoader.large_font.render("Who wants to be a", True, (255, 255, 255))
        screen.blit(text, (290, 100))
        text_newline = self.AssetLoader.large_font.render("Millionaire?", True, (255, 255, 255))
        screen.blit(text_newline, (435, 200))

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
