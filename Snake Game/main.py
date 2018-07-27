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
from random import *

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

# Initilazation
pygame.init()
pygame.font.init()

# Initalizes the display settings. The first is the size and the second is the title.
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')
pygame.display.update()

# Initalizes the font
font = pygame.font.SysFont('comicsansms', 32)

def drawMenu():
    # Play new game button
    user_pick = False

    startButton = pygame.draw.rect(gameDisplay, green, [250,100,300,100])
    quitButton = pygame.draw.rect(gameDisplay, green, [250,350,300,100])

    textStart = pygame.font.Font.render(font,'Start', 1, white)
    textQuit = pygame.font.Font.render(font,'Quit', 1, white)
    print(textStart,textQuit)
    pygame.Surface.blit(gameDisplay, textStart, (400 - textStart.get_width() // 2, 150 - textStart.get_height() // 2))
    pygame.Surface.blit(gameDisplay, textQuit, (400 - textQuit.get_width() // 2, 400 - textQuit.get_height() // 2))
    pygame.display.update()

    while not user_pick:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
            # This event makes the button change font when hovered over.
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                if pygame.Rect.collidepoint(startButton, mouse_position):
                    startButton = pygame.draw.rect(gameDisplay, blue, [250,100,300,100])
                    pygame.Surface.blit(gameDisplay, textStart, (400 - textStart.get_width() // 2, 150 - textStart.get_height() // 2))
                    pygame.Surface.blit(gameDisplay, textQuit, (400 - textQuit.get_width() // 2, 400 - textQuit.get_height() // 2))
                    pygame.display.update()
                elif pygame.Rect.collidepoint(quitButton, mouse_position):
                    quitButton = pygame.draw.rect(gameDisplay, blue, [250,350,300,100])
                    pygame.Surface.blit(gameDisplay, textStart, (400 - textStart.get_width() // 2, 150 - textStart.get_height() // 2))
                    pygame.Surface.blit(gameDisplay, textQuit, (400 - textQuit.get_width() // 2, 400 - textQuit.get_height() // 2))
                    pygame.display.update()
                else:
                    startButton = pygame.draw.rect(gameDisplay, green, [250,100,300,100])
                    quitButton = pygame.draw.rect(gameDisplay, green, [250,350,300,100])
                    pygame.Surface.blit(gameDisplay, textStart, (400 - textStart.get_width() // 2, 150 - textStart.get_height() // 2))
                    pygame.Surface.blit(gameDisplay, textQuit, (400 - textQuit.get_width() // 2, 400 - textQuit.get_height() // 2))
                    pygame.display.update()
            # This event is the button logic
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickPos = pygame.mouse.get_pos()
                print(clickPos)
                if pygame.Rect.collidepoint(startButton, clickPos):
                    print('Game Started')
                    user_pick = True
                elif pygame.Rect.collidepoint(quitButton,clickPos):
                    print('Quit Game')
                    user_pick = True
                    pygame.quit()
                    quit()


class Player():
    """docstring for Making the Player."""
    x = 400
    y = 300
    speed = 1

    # Movement Functions
    def moveLeft(self):
        self.x = self.x - self.speed
    def moveRight(self):
        self.x = self.x + self.speed
    def moveDown(self):
        self.y = self.y - self.speed
    def moveUp(self):
        self.y = self.y + self.speed


# def player_snake(xPos,yPos,numDotsEaten):
#     x = xPos
#     y = yPos
#
#     playerSpeed = 0 # FIXME: Add in speed in relation to number of dots numDotsEaten
#     pygame.draw.rect(gameDisplay,black, [x,y,10,10])

def game_intro():
    '''
    Can create later using the pygame.font library for plain typing.
    '''
    pass

def game_loop():
    # Globals in the def
    numberOfDots = 0
    score = 0
    gameExit = False

    # Run Menu
    drawMenu()

    gameDisplay.fill(white)

    gameBorders = pygame.draw.rect(gameDisplay, black, [50,50,700,500], 2)

    scoreRect = pygame.draw.rect(gameDisplay, white, [550,550,250,50], 1)
    scoreText = pygame.font.Font.render(font,'Score: {}'.format(score), 1, black)
    pygame.Surface.blit(gameDisplay, scoreText, (550,550))

    player = Player()

    pygame.display.update()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type == pygame.KEYDOWN:
                if event.key == K_d or event.key == K_LEFT:
                    snake.moveLeft()


# Main Function Calls
game_intro()
game_loop()

# Quit Functions
pygame.quit()
quit()
