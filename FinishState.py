from GameState import GameState
import ButtonLibrary


class Finish(GameState):
    def __init__(self):
        super().__init__()

        game_button = ButtonLibrary.GameButton
        self.exit_button = game_button(75, 600, 128, 64)
        ButtonLibrary.buttons.append(self.exit_button)

    def render(self):
        from Main import screen, GSM, stage, set_stage

        current_stage = stage
        print(current_stage)

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)
        screen.blit(self.AssetLoader.logo, (400, 100, 100, 300))

        reward = ["0", "100", "200", "300", "400", "500", "1000", "2000", "4000", "8000", "26,000", "32,000",
                       "64,000", "125,000", "250,000", "500,000", "1,000,000"]

        if current_stage == 16:
            new_stage = current_stage
        elif current_stage < 16 and current_stage >= 11:
            new_stage = 11
        elif current_stage < 11 and current_stage >= 6:
            new_stage = 6
        else:
            new_stage = 0

        if new_stage == 0:
            text = self.AssetLoader.large_font.render("You Lost", True, self.WHITE)
        else:
            text = self.AssetLoader.large_font.render("You Won: $"+str(reward[new_stage])+"!", True, self.WHITE)
        screen.blit(text, (1280 / 2 - ((len(str(reward[new_stage])) + 9) * 25), 400))

        # Render and update the exit button
        self.exit_button.rounded_rectangle(screen, self.BLUE, "Exit", self.WHITE, 0, 8, 8)

        if self.exit_button.pressed:
            set_stage(0)
            GSM.game_state = 0
            GSM.menu.__init__()

    def input(self):
        game_button = ButtonLibrary.GameButton(0, 0, 0, 0)
        game_button.update_mouse()
