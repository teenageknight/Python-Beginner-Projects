'''
Title: Snake Game

Description: A game where a player (the snake), eats pieces of food to grow bigger.
             If the snake hits the edge or the side, it will die.

Created By: Bryce Jackson
            https://github.com/teenageknight
'''

# Imports
import pygame
import random

# Globals
score = 0
white = (255,255,255)

# Classes
class Player(object):
    """docstring for Player."""
    def __init__(self, arg):
        super(Player, self).__init__()
        self.arg = arg

    # def drawPlayer(x,y):
    #     pass

class Food(object):
    """docstring for Food."""
    def __init__(self, arg):
        super(Food, self).__init__()
        self.arg = arg

# Definitions
def redrawScreen():
    pygame.draw.rect(screen, white, [25,50,550,625])

    pygame.display.update()

# Mainloop
if __name__ == '__main__':
    # initializes pygame module
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([600,700])

    # Set the title of the window
    pygame.display.set_caption('Snake Game')

    done = False
    while not done:

        redrawScreen()

        # Defines when the function loop should stop (by clicking x)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # All key pressing movement goes here
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pass
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pass
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pass
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pass
