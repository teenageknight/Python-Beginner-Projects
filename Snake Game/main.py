'''
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
'''

# Imports
import pygame

'''
##################
#     Globals    #
##################
'''
# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Display Width and Height
display_width = 800
display_height = 600

pygame.init()

# Initalizes the display settings. The first is the size and the second is the title.
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')
pygame.display.update()

def player_snake(xPos,yPos,numDotsEaten):
    x = xPos
    y = yPos

    playerSpeed = 0 # FIXME: Add in speed in relation to number of dots numDotsEaten
    pygame.draw.rect(gameDisplay,black, [x,y,10,10])

def game_intro(arg):
    '''
    Can create later using the pygame.font library for plain typing.
    '''
    pass

def game_loop(arg):
    # Globals in the def
    number_dots_eaten = 0
    speed = 10

    gameDisplay.Fill(white)

# Main Function Calls
game_intro()
game_loop()

# Quit Functions
pygame.quit()
quit()
