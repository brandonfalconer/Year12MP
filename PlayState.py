from GameState import GameState
import ButtonLibrary
import pygame
import random


class Play(GameState):
    def __init__(self):
        super().__init__()

        from Main import screen
        # Define variables
        self.screen = screen
        self.question = True
        self.finished = False
        self.button_press = False
        self.answer = False

        self.fifty = True
        self.phone = True
        self.phone_press = False
        self.audience = True
        self.del_question = True
        self.question_list = []
        self.data = []

        self.draw_one = True
        self.draw_two = True
        self.draw_three = True
        self.draw_four = True

        # Set up game buttons
        game_button = ButtonLibrary.GameButton
        self.question_button = game_button(200, 350, 880, 80)
        self.answer_one_button = game_button(200, 450, 420, 80)
        self.answer_two_button = game_button(660, 450, 420, 80)
        self.answer_three_button = game_button(200, 550, 420, 80)
        self.answer_four_button = game_button(660, 550, 420, 80)
        self.finish_button = game_button(64, 64, 156, 76)
        self.continue_button = game_button(1100, 600, 156, 96)
        self.fifty_lifeline_button = game_button(1050, 50, 150, 75)
        self.friend_lifeline_button = game_button(1050, 135, 150, 75)
        self.audience_lifeline_button = game_button(1050, 220, 150, 75)
        ButtonLibrary.buttons.extend((self.question_button, self.answer_one_button, self.answer_two_button,
                                      self.answer_three_button, self.answer_four_button, self.finish_button,
                                      self.continue_button, self.fifty_lifeline_button, self.friend_lifeline_button,
                                      self.audience_lifeline_button))

        # Open question file and load into a list
        with open('QuestionInfo.txt', 'r') as f:
            self.question_data = [line.strip() for line in f]

        # Load music
        pygame.mixer.music.load("Assets/Sound/Lets Play.mp3")
        pygame.mixer.music.play(-1)

    def render(self):
        from Main import GSM, stage, screen

        # Create a new question form a file
        def new_question():
            data = 9

            # Check to see if the question has been used before, otherwise create new question
            random_question = random.randint(0, (len(self.question_data) - data) / data) * data
            while random_question in self.question_list:
                random_question = random.randint(0, (len(self.question_data) - data) / data) * data
            else:
                self.question_list.append(random_question)

            # Insert current question into an array, then return the array
            current_question_data = []
            for i in range(9):
                current_question_data.append(self.question_data[random_question + i])

            self.question = False
            return current_question_data

        def answer_question():
            # Draw Background
            self.screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

            # Draw Millionaire Logo
            self.screen.blit(self.AssetLoader.logo, (400, 50, 100, 300))

            # Render and update the back button
            self.finish_button.rounded_rectangle(self.screen, self.BLUE, "Finish", self.WHITE, 0, 8, 8)

            # Finished button has been pressed
            if self.finish_button.pressed:
                self.question = True
                GSM.game_state = 3
                GSM.finish.__init__(True)

            # Create new question
            if self.question:
                self.data = new_question()
                self.question = False
                self.phone_press = False
                self.audience_press = False

            else:
                # Logic for 50:50 lifeline
                answer = self.data[5]

                if self.fifty:
                    # If lifeline button has been pressed
                    if self.fifty_lifeline_button.pressed:
                        self.fifty = False
                        fifty_data = str(self.data[6])
                        fifty_list = fifty_data.split(',')
                        for i in fifty_list:
                            if int(i) == 1:
                                self.draw_one = False
                            elif int(i) == 2:
                                self.draw_two = False
                            elif int(i) == 3:
                                self.draw_three = False
                            elif int(i) == 4:
                                self.draw_four = False
                    else:
                        self.fifty_lifeline_button.rounded_rectangle(self.screen, self.BLUE, "50:50", self.WHITE, 0, 16,
                                                                     16)

                # Draw and update buttons
                self.question_button.rounded_rectangle(self.screen, (0, 0, 204), self.data[0], self.WHITE, 0, 16, 16)
                if self.draw_one:
                    self.answer_one_button.rounded_rectangle(self.screen, self.BLUE, self.data[1], self.WHITE, 0, 16,
                                                             16)
                if self.draw_two:
                    self.answer_two_button.rounded_rectangle(self.screen, self.BLUE, self.data[2], self.WHITE, 0, 16,
                                                             16)
                if self.draw_three:
                    self.answer_three_button.rounded_rectangle(self.screen, self.BLUE, self.data[3], self.WHITE, 0, 16,
                                                               16)
                if self.draw_four:
                    self.answer_four_button.rounded_rectangle(self.screen, self.BLUE, self.data[4], self.WHITE, 0, 16,
                                                              16)

                # Logic for 'phone a friend' lifeline
                if self.phone:
                    # If phone lifeline has been pressed
                    if self.friend_lifeline_button.pressed:
                        self.phone = False
                        self.phone_press = True
                    else:
                        self.friend_lifeline_button.rounded_rectangle(self.screen, self.BLUE, "Phone", self.WHITE, 0,
                                                                      16, 16)
                else:
                    if self.phone_press:
                        if int(answer) == 1:
                            x = self.answer_one_button.x
                            y = self.answer_one_button.y
                        elif int(answer) == 2:
                            x = self.answer_two_button.x
                            y = self.answer_two_button.y
                        elif int(answer) == 3:
                            x = self.answer_three_button.x
                            y = self.answer_three_button.y
                        elif int(answer) == 4:
                            x = self.answer_four_button.x
                            y = self.answer_four_button.y
                        else:
                            x = 1
                            y = 1

                        screen.blit(self.AssetLoader.phone, (x + 5, y + 13, 51, 51))

                # Logic for 'as the studio audience' lifeline
                if self.audience:
                    if self.audience_lifeline_button.pressed:
                        self.audience = False
                        self.audience_press = True
                    else:
                        self.audience_lifeline_button.rounded_rectangle(self.screen, self.BLUE, "Audience", self.WHITE,
                                                                        0, 16, 16)
                else:
                    if self.audience_press:
                        audience_data = str(self.data[8])
                        audience_list = audience_data.split(',')
                        x = 1
                        for i in audience_list:
                            if x == 1:
                                text = self.AssetLoader.small_font.render("(" + i + ")", True, self.WHITE)
                                screen.blit(text, (self.answer_one_button.x + 350, self.answer_one_button.y + 25))
                            elif x == 2:
                                text = self.AssetLoader.small_font.render("(" + i + ")", True, self.WHITE)
                                screen.blit(text, (self.answer_two_button.x + 350, self.answer_two_button.y + 25))
                            elif x == 3:
                                text = self.AssetLoader.small_font.render("(" + i + ")", True, self.WHITE)
                                screen.blit(text, (self.answer_three_button.x + 350, self.answer_three_button.y + 25))
                            elif x == 4:
                                text = self.AssetLoader.small_font.render("(" + i + ")", True, self.WHITE)
                                screen.blit(text, (self.answer_four_button.x + 350, self.answer_four_button.y + 25))
                            x += 1

                # Check the answer buttons have been pressed, and if the answer is right/wrong
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
            from Main import stage, increase_stage
            self.question = False

            # Draw Background
            self.screen.blit(self.AssetLoader.background, self.AssetLoader.background_rect)

            # Draw Millionaire Logo
            self.screen.blit(self.AssetLoader.logo, (700, 100, 100, 300))

            # Draw reward table
            reward_text = ["$100", "$200", "$300", "$400", "$500", "$1000", "$2000", "$4000", "$8000", "$26,000",
                           "$32,000", "$64,000", "$125,000", "$250,000", "$500,000", "$1,000,000"]

            x = 100
            y = 650
            width = 500
            height = 30

            for i in range(len(reward_text)):
                # Highlight current score
                if int(i) == int(stage):
                    pygame.draw.rect(screen, (40, 150, 255), (x, y, width, height), 0)
                elif int(i) == 5 or int(i) == 10 or int(i) == 15:
                    pygame.draw.rect(screen, (0, 000, 255), (x, y, width, height), 0)
                else:
                    pygame.draw.rect(screen, self.BLUE, (x, y, width, height), 0)

                # Draw text
                text = self.AssetLoader.small_font.render((reward_text[i]), True, self.WHITE)
                screen.blit(text, (x + width / 2 - (len(reward_text[i]) * 5), y))

                y -= 40

            # Draw text
            if stage < 5:
                t = 5 - stage
            elif stage < 10:
                t = 10 - stage
            elif stage < 15:
                t = 15 - stage
            else:
                t = 0

            text = self.AssetLoader.medium_font.render("You are " + str(t) + " stages away", True, self.WHITE)
            screen.blit(text, (700, 400))

            text = self.AssetLoader.medium_font.render("from the next safety net.", True, self.WHITE)
            screen.blit(text, (700, 450))

            # Render and update the continue button
            self.continue_button.rounded_rectangle(self.screen, self.BLUE, "Continue", self.WHITE, 0, 8, 8)
            if self.continue_button.pressed:
                self.finished = False
                self.button_press = False
                self.del_question = True
                self.question = True
                increase_stage()
                return

        # If the user has not finished the game, continue, otherwise change to finish state
        if not self.finished:
            # If the user has reached the final stage
            if stage >= 16:
                self.finished = True
            else:
                answer_question()

                # If a question has been chosen
                if self.button_press:
                    if self.answer:
                        # Answer is correct
                        pygame.mixer.music.load("Assets/Sound/Correct Answer.mp3")
                        pygame.mixer.music.play(0)
                        self.question = True
                        show_stage()
                        self.draw_one = True
                        self.draw_two = True
                        self.draw_three = True
                        self.draw_four = True
                    else:
                        # Answer is incorrect
                        pygame.mixer.music.load("Assets/Sound/Wrong Answer.mp3")
                        pygame.mixer.music.play(0)
                        self.finished = True
        else:
            # User has lost
            self.question = True
            GSM.game_state = 3
            GSM.finish.__init__(False)

    # Handle user input
    def input(self):
        GameState.input(self)
