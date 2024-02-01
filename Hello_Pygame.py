"""
    Name: Hello_Pygame.py
    Author: Triumph Ogbonnia
    Created: 2/1/24
    Purpose: Pygame with python
"""
# Import pygame libraries
import pygame
# Import sys for sys.exit() to cleanly exit proram
import sys

#--------------------- INITIALIZE PYGAME ------------------------------#
# Initialize the pygame module
pygame.init()
# Create the display surface
SURFACE = pygame.display.set_mode((400, 300))
# Set the caption for window
pygame.display.set_caption("Pygame World!")

#--------------------- INITIALIZE GAME LOOP --------------------------#
while True:
    # Listen for program events
    for event in pygame.event.get():

        # Closing the program window
        # causes the quit event to be enabled
        if event.type == pygame.QUIT:
            # Exit Pygame
            pygame.quit()
            # Exit the program
            sys.exit()

    # Redraw the screen
    pygame.display.update()