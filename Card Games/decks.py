# Practice for OOP programing in python using a card game
# https://github.com/teenageknight/Python-Beginner-Projects

from random import *

# Defines Global variables


class player:
    """Creates a Player for the guess a number game"""
    def __init__(self, name, score = 0):
        super(player, self).__init__()
        self.name = name
