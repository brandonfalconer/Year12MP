# --- Import Libraries
import pygame
import GameStateManager

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
# Objects
GSM = GameStateManager.GameStateManager(0)

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
