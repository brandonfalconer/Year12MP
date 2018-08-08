# --- Import Libraries
import pygame
import random
import ButtonLibrary
import re

# --- Define global constants
# Define some colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# --- Define classes
#class GameState:
    #def __init__(self, state):
        #self.state = state

# --- Define functions
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

# --- MAIN PROGRAM
# Initialise pygame
pygame.init()

# Initialise screen properties
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Who Wants to be a Millionaire?")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program -----------
# Variables
question_info = open("QuestionInfo.txt")
line_number = 0

buttons = []
start_button = ButtonLibrary.GameButton(100, 100, 200, 200, BLUE, "Start", False)
buttons.append(start_button)

for line in question_info:
    words = split_line(line)
    line_number += 1

    for word in words:
        i = 1

while not done:
    # --- Main event loop
    # Gather user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                for button in buttons:
                    if (mouse_x > button.x and mouse_x < button.x + button.width) and (mouse_y > button.y and mouse_y < button.y + button.height):
                        button.pressed = True

    # --- Game logic
    #if start_button.pressed:


    # --- Screen-clearing
    screen.fill(WHITE)

    # --- Drawing code
    start_button.draw()

    # --- Update the screen
    pygame.display.flip()

    # --- Set to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
