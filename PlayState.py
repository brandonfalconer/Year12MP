from GameState import GameState
import ButtonLibrary
import random


class Play(GameState):
    def __init__(self):
        super().__init__()

        from Main import screen
        self.screen = screen
        self.question = True
        self.finished = False
        self.data = []

        game_button = ButtonLibrary.GameButton
        self.question_button = game_button(200, 350, 880, 80)
        self.answer_one_button = game_button(200, 450, 420, 80)
        self.answer_two_button = game_button(660, 450, 420, 80)
        self.answer_three_button = game_button(200, 550, 420, 80)
        self.answer_four_button = game_button(660, 550, 420, 80)
        self.back_button = game_button(64, 64, 64, 64)
        ButtonLibrary.buttons.extend((self.question_button, self.answer_one_button, self.answer_two_button,
                                      self.answer_three_button, self.answer_four_button, self.back_button))

    def render(self):
        from Main import screen, GSM

        def new_question():
            with open('QuestionInfo.txt', 'r') as f:
                question_data = [line.strip() for line in f]

            random_question = random.randint(0, 1) * 6

            current_question_data = [question_data[random_question], question_data[random_question + 1],
                                     question_data[random_question + 2], question_data[random_question + 3],
                                     question_data[random_question + 4], question_data[random_question + 5]]

            return current_question_data

        # Draw Background
        screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

        if not self.finished:
            # Draw Millionaire Logo
            screen.blit(self.AssetLoader.logo, (400, 50, 100, 300))

            # Current State
            if self.question:
                self.data = new_question()
                self.question = False

            if self.back_button.pressed:
                GSM.game_state = 0
                GSM.menu.__init__()

            # Draw and update buttons
            self.question_button.rounded_rectangle(screen, (0, 0, 204), ""+self.data[0], self.WHITE, 0, 16, 16)
            self.answer_one_button.rounded_rectangle(screen, self.BLUE, "" + self.data[1], self.WHITE, 0, 16, 16)
            self.answer_two_button.rounded_rectangle(screen, self.BLUE, "" + self.data[2], self.WHITE, 0, 16, 16)
            self.answer_three_button.rounded_rectangle(screen, self.BLUE, "" + self.data[3], self.WHITE, 0, 16, 16)
            self.answer_four_button.rounded_rectangle(screen, self.BLUE, "" + self.data[4], self.WHITE, 0, 16, 16)

            self.back_button.circle(screen, self.BLUE, "Finish", self.WHITE, 48, 0)

        else:
            GSM.game_state = 3
            GSM.play.__init__()

    def input(self):
        game_button = ButtonLibrary.GameButton(0, 0, 0, 0)
        game_button.update_mouse()
