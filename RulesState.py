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

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

        # Draw back button
        self.back_button.rounded_rectangle(screen, self.YELLOW, "Back", self.BLACK, 0, 32, 32)

        if self.back_button.pressed:
            GSM.game_state = 0
            GSM.menu.__init__()

        # Draw text
        text = self.AssetLoader.large_font.render("How to Play", True, self.WHITE)
        screen.blit(text, (400, 30))

        text = [" In the game 'Who Wants to be a",
                " Millionaire?' the user must answer up to",
                " fifteen general knowledge questions split",
                " into three categories (easy; medium; hard)",
                " with each correctly answered question",
                " returning a larger cash prize. This continues",
                " until the user incorrectly answers a question",
                " in which they lose all of their money, unless",
                " they have reached a safety net. These safety",
                " nets are $1000 and $32000. The user may",
                " also you one of three lifelines in a question",
                " which are; ‘Phone a Friend, ‘Ask the studio",
                " audience’ or ’50:50’."]

        y = 155
        for line in text:
            y += 30
            text = self.AssetLoader.small_font.render(line, True, self.WHITE)
            screen.blit(text, (100, y))

        # Friend Lifeline
        text = self.AssetLoader.regular_font.render("Phone a Friend", True, (255, 255, 0))
        screen.blit(text, (750, 155))

        text = ["A friend is phoned and the user",
                "is shown an answer based on",
                "the difficulty of question."]

        y = 180
        for line in text:
            y += 30
            text = self.AssetLoader.small_font.render(line, True, self.WHITE)
            screen.blit(text, (750, y))

        text = self.AssetLoader.regular_font.render("Ask the Studio Audience", True, (255, 255, 0))
        screen.blit(text, (750, 305))

        text = ["Percentages of an audience will",
                "be shown, based on the",
                "difficulty of question. "]

        y = 330
        for line in text:
            y += 30
            text = self.AssetLoader.small_font.render(line, True, self.WHITE)
            screen.blit(text, (750, y))

        text = self.AssetLoader.regular_font.render("50:50", True, (255, 255, 0))
        screen.blit(text, (750, 455))

        text = ["Two incorrect answers are",
                "removed, leaving the user with",
                "a choice of two."]

        y = 480
        for line in text:
            y += 30
            text = self.AssetLoader.small_font.render(line, True, self.WHITE)
            screen.blit(text, (750, y))

    def input(self):
        GameState.input(self)
