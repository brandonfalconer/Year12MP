# --- Import Libraries
import pygame
import random
import Button_Library
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
new_button = Button_Library.GameButton(100, 100, 200, 200, BLUE, "Start", False)

question_info = open("QuestionInfo.txt")
line_number = 0

for line in question_info:
    words = split_line(line)
    line_number += 1

    for word in words:
        i = 0


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic

    # --- Screen-clearing
    screen.fill(WHITE)

    # --- Drawing code
    new_button.update()

    # --- Update the screen
    pygame.display.flip()

    # --- Set to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
