import sys, pygame, os

pygame.init()

#Defines the colors used

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
purple = (160,32,240)
pink = (255,192,203)
black = (0,0,0)
white = (255,255,255)

class App(object):
    """docstring for App."""
    def __init__(self, arg):
        super(App, self).__init__()
        self.arg = arg
