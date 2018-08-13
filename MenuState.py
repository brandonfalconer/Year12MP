import ButtonLibrary
import GameState
import pygame

#BLUE = (0, 0, 255)


class Menu(GameState):
    def __init__(self):
        super().__init__()

        self.start_button = ButtonLibrary.GameButton(100, 100, 200, 200, self.BLUE, "Start", False)
        self.ButtonLibrary.buttons.append(self.start_button)

    def render(self):
        from Main import GSM
        self.start_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    print("click")
                    for button in ButtonLibrary.buttons:
                        if (mouse_x > button.x and mouse_x < button.x + button.width) and (mouse_y > button.y and mouse_y < button.y + button.height):
                            button.pressed = True
                            print("pressed")

        if self.start_button.pressed:
            GSM.game_state = 1

    def input(self):
        pass
