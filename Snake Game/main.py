#################################################################
#                                                               #
#    snake.py                                                   #
#  ----------------------------------------------------------   #
#                                                               #
#  Description: A game where the player eats dots to increase   #
#               in speed and size. Uses pygame.                 #
#                                                               #
#         Author: Bryce Jackson (bkajackson99@gmail.com)        #
#               (https://github.com/teenageknight)              #
#                                                               #
#################################################################

# Imports
import pygame

# ----------------
#     Globals
# ----------------
# Colors
black = (0,0,0)
white = (255,255,255)

# Sets snakes segments hights and widths
segment_width = 15
segment_height = 15
# Sets margins between each segment
segment margin = 3

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
