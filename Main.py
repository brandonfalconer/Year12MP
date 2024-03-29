# --- Import Libraries
import GameStateManager
import pygame

# --- Define global constants
# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

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
# Objects / Variables
GSM = GameStateManager.GameStateManager(0)
stage = 0

pygame.mixer.music.load("Assets/Sound/Main Theme.mp3")
pygame.mixer.music.play(-1)

# Global Functions
def increase_stage():
    global stage
    stage += 1

def set_stage(value):
    global stage
    stage = value


while not done:
    # --- Main event loop

    # Gather user input
    for event in pygame.event.get():
        # User input from current state
        GSM.input()

        if event.type == pygame.QUIT:
            done = True

    # --- Draw/Update current state
    GSM.render()

    # --- Update the screen
    pygame.display.flip()

    # --- Set to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
