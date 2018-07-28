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


# class Player:
#     """docstring for Making the Player."""
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     speed = 5
#
#     # Movement Functions
#     def moveLeft(self,x):
#         self.x = self.x - self.speed
#         return self.x
#     def moveRight(self,x):
#         self.x = self.x + self.speed
#         return self.x
#     def moveDown(self,y):
#         self.y = self.y - self.speed
#         return self.y
#     def moveUp(self,y):
#         self.y = self.y + self.speed
#         return self.y

def game_intro():
    '''
    Can create later using the pygame.font library for plain typing.
    '''
    pass

def makeFood():
    food_x = randint(50,700)
    while not food_x % 5 == 0:
        food_x = randint(50,700)
    food_y = randint(50,500)
    while not food_y % 5 == 0:
        food_y = randint(50,500)
    foodLocation = (food_x,food_y)

    return food_x, food_y

def game_loop():
    # Globals in the def
    gameExit = False
    x = 400
    y = 300
    score = 0
    make_food = True

    # Run Menu
    drawMenu()

    while not gameExit:

        playerLocation = (x,y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x -= 10
                    print(playerLocation)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x += 10
                    print(playerLocation)
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    y -= 10
                    print(playerLocation)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y += 10
                    print(playerLocation)

        gameDisplay.fill(white)

        gameBorders = pygame.draw.rect(gameDisplay, black, [50,50,700,500], 2)

        scoreRect = pygame.draw.rect(gameDisplay, white, [550,550,250,50], 1)
        scoreText = pygame.font.Font.render(font,'Score: %d' % score, 1, black)
        pygame.Surface.blit(gameDisplay, scoreText, (550,550))

        if make_food:
            food_x, food_y = makeFood()
            foodRect = pygame.draw.rect(gameDisplay, red, [food_x,food_y, 10,10])
            make_food = False
            print('Made Food')

        foodRect.draw()
        playerRect = pygame.draw.rect(gameDisplay,blue,[x,y,15,15])

        if not gameBorders.contains(playerRect):
            gameExit = True
        if playerRect.contains(foodRect):
            score += 5
            print(score)
            print('winner')
            make_food = True
        pygame.display.update()

        # Clock = pygame.time.Clock()
        # Clock.tick(3)


# Main Function Calls
game_intro()
game_loop()

# Quit Functions
pygame.quit()
quit()
