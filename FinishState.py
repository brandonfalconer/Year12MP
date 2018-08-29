from GameState import GameState
import ButtonLibrary


class Finish(GameState):
    def __init__(self, finish):
        super().__init__()

        game_button = ButtonLibrary.GameButton
        self.exit_button = game_button(75, 600, 156, 76)
        self.again_button = game_button(1000, 600, 176, 76)
        ButtonLibrary.buttons.extend((self.exit_button, self.again_button))

        self.finish = finish

    def render(self):
        from Main import screen, GSM, stage, set_stage

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)
        screen.blit(self.AssetLoader.logo, (400, 100, 100, 300))

        reward = ["0", "100", "200", "300", "400", "500", "1000", "2000", "4000", "8000", "26,000", "32,000",
                       "64,000", "125,000", "250,000", "500,000", "1,000,000"]

        current_stage = stage

        if not self.finish:
            if current_stage == 16:
                new_stage = current_stage
            elif current_stage < 16 and current_stage >= 11:
                new_stage = 11
            elif current_stage < 11 and current_stage >= 6:
                new_stage = 6
            else:
                new_stage = 0
        else:
            new_stage = current_stage

        if new_stage == 0:
            text = self.AssetLoader.large_font.render("You Lost", True, self.WHITE)
            screen.blit(text, (450, 400))
        else:
            text = self.AssetLoader.large_font.render("You Won: $"+str(reward[new_stage])+"!", True, self.WHITE)
            screen.blit(text, (1280 / 2 - ((len(str(reward[new_stage])) + 9) * 25), 400))

        # Render and update the exit/try again button
        self.exit_button.rounded_rectangle(screen, self.BLUE, "Exit", self.WHITE, 0, 8, 8)
        self.again_button.rounded_rectangle(screen, self.BLUE, "Try Again", self.WHITE, 0, 8, 8)

        if self.exit_button.pressed:
            set_stage(0)
            GSM.game_state = 0
            GSM.menu.__init__()

        if self.again_button.pressed:
            set_stage(0)
            GSM.game_state = 2
            GSM.play.__init__()

    def input(self):
        game_button = ButtonLibrary.GameButton(0, 0, 0, 0)
        game_button.update_mouse()
