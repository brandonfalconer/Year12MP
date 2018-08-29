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
        self.button_press = False
        self.answer = False
        self.data = []

        game_button = ButtonLibrary.GameButton
        self.question_button = game_button(200, 350, 880, 80)
        self.answer_one_button = game_button(200, 450, 420, 80)
        self.answer_two_button = game_button(660, 450, 420, 80)
        self.answer_three_button = game_button(200, 550, 420, 80)
        self.answer_four_button = game_button(660, 550, 420, 80)
        self.back_button = game_button(64, 64, 128, 64)
        self.continue_button = game_button(1000, 550, 156, 96)
        ButtonLibrary.buttons.extend((self.question_button, self.answer_one_button, self.answer_two_button,
                                      self.answer_three_button, self.answer_four_button, self.back_button,
                                      self.continue_button))

    def render(self):
        from Main import GSM, stage

        def new_question():
            with open('QuestionInfo.txt', 'r') as f:
                question_data = [line.strip() for line in f]

            random_question = random.randint(0, 1) * 7

            current_question_data = [question_data[random_question], question_data[random_question + 1],
                                     question_data[random_question + 2], question_data[random_question + 3],
                                     question_data[random_question + 4], question_data[random_question + 5],
                                     question_data[random_question + 6]]

            return current_question_data

        def answer_question():
            # Draw Background
            self.screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

            # Draw Millionaire Logo
            self.screen.blit(self.AssetLoader.logo, (400, 50, 100, 300))

            # Render and update the back button
            self.back_button.rounded_rectangle(self.screen, self.BLUE, "Finish", self.WHITE, 0, 8, 8)

            if self.back_button.pressed:
                GSM.game_state = 0
                GSM.menu.__init__()

            # Create new question
            if self.question:
                self.data = new_question()
                self.question = False
            else:
                answer = self.data[5]

                # Draw and update buttons
                self.question_button.rounded_rectangle(self.screen, (0, 0, 204), ""+self.data[0], self.WHITE, 0, 16, 16)
                self.answer_one_button.rounded_rectangle(self.screen, self.BLUE, "" + self.data[1], self.WHITE, 0, 16, 16)
                self.answer_two_button.rounded_rectangle(self.screen, self.BLUE, "" + self.data[2], self.WHITE, 0, 16, 16)
                self.answer_three_button.rounded_rectangle(self.screen, self.BLUE, "" + self.data[3], self.WHITE, 0, 16, 16)
                self.answer_four_button.rounded_rectangle(self.screen, self.BLUE, "" + self.data[4], self.WHITE, 0, 16, 16)

                if self.answer_one_button.pressed:
                    self.button_press = True
                    if int(answer) == 1:
                        self.answer = True
                        return
                    else:
                        self.answer = False
                        return

                elif self.answer_two_button.pressed:
                    self.button_press = True
                    if int(answer) == 2:
                        self.button_press = True
                        self.answer = True
                        return
                    else:
                        self.answer = False
                        return

                elif self.answer_three_button.pressed:
                    self.button_press = True
                    if int(answer) == 3:
                        self.button_press = True
                        self.answer = True
                        return
                    else:
                        self.answer = False
                        return

                elif self.answer_four_button.pressed:
                    self.button_press = True
                    if int(answer) == 4:
                        self.answer = True
                        return
                    else:
                        self.answer = False
                        return

        def show_stage():
            from Main import stage

            # Draw Background
            self.screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

            # Render and update the continue button
            self.continue_button.rounded_rectangle(self.screen, self.BLUE, "Continue", self.WHITE, 0, 8, 8)

            if self.continue_button.pressed:
                self.finished = False
                self.button_press = False
                stage += 1
                print(str(stage))
                return

        if not self.finished:
            if stage > 16:
                self.finished = True
            else:
                answer_question()
                if self.button_press:
                    if self.answer:
                        show_stage()
                    else:
                        self.finished = True
        else:
            GSM.game_state = 3
            GSM.finish.__init__()

    def input(self):
        game_button = ButtonLibrary.GameButton(0, 0, 0, 0)
        game_button.update_mouse()