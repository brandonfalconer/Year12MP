from GameState import GameState
import ButtonLibrary


class Finish(GameState):
    def __init__(self):
        super().__init__()

        game_button = ButtonLibrary.GameButton
        self.exit_button = game_button(75, 600, 48, 48)
        ButtonLibrary.buttons.append(self.exit_button)

    def render(self):
        from Main import screen, GSM

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)
        screen.blit(self.AssetLoader.logo, (400, 100, 100, 300))

        reward = [0, 100, 200, 300, 400, 500, 1000, 2000, 4000, 8000, 26000, 32000, 64000, 125000, 250000, 500000,
                  1000000]

        text = self.AssetLoader.large_font.render("You Won: $32,000"+"!", True, self.WHITE)
        screen.blit(text, (250, 400))

        # Render and update the exit button
        self.exit_button.circle(screen, self.BLUE, "Exit", self.WHITE)

        if self.exit_button.pressed:
            GSM.game_state = 0
            GSM.menu.__init__()

    def input(self):
        game_button = ButtonLibrary.GameButton(0, 0, 0, 0)
        game_button.update_mouse()
