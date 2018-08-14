# --- Import Libraries
import pygame
import re
import GameStateManager

# --- Define global constants
# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


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
GSM = GameStateManager.GameStateManager(0)

question_info = open("QuestionInfo.txt")
line_number = 0

for line in question_info:
    words = split_line(line)
    line_number += 1

    for word in words:
        i = 1

while not done:
    # --- Main event loop
    # Gather user input
    for event in pygame.event.get():
        # User input from current state
        GSM.input()

        if event.type == pygame.QUIT:
            done = True

    # --- Screen-clearing
    screen.fill((255, 255, 255))

    # --- Draw/Update current state
    GSM.render()

    # --- Update the screen
    pygame.display.flip()

    # --- Set to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
