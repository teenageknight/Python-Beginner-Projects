'''
#################################################################
#                                                               #
#    snake.py                                                   #
#  ----------------------------------------------------------   #
#                                                               #
#  Description: A game where the player eats dots to increase   #
#               in speed and size. Uses pygame. very sloppy     #
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

def drawSnake(lead_x,lead_y,xList,yList,numBlocks,rectList):
    # playerRect = pygame.draw.rect(gameDisplay,blue,[lead_x,lead_y,20,20])

    if numBlocks != 0:
        for i in range(len(rectList)):
            if i == 0:
                xList[i] = lead_x
                yList[i] = lead_y
            elif i > 0:
                xList[i] = xList[i-1]
                yList[i] = yList[i-1]
            temp = rectList[i]
            temp.move(xList[i],yList[i])

    return xList, yList, rectList

def addMoreSnake(xList,yList,direction,lead_x,lead_y,iteration):
    rectList = []
    for i in range(len(xList)):
        temp = pygame.draw.rect(gameDisplay, blue, [xList[i],yList[i],20,20])
        rectList.append(temp)

    if iteration == 1:
        if direction == 'left':
            lead_x += 22
            xList.append(lead_x)
            yList.append(lead_y)
        elif direction == 'right':
            lead_x -= 22
            xList.append(lead_x)
            yList.append(lead_y)
        elif direction == 'up':
            lead_y += 22
            yList.append(lead_y)
            xList.append(lead_x)
        elif direction == 'down':
            lead_y -= 22
            yList.append(lead_y)
            xList.append(lead_x)
    else:
        if direction == 'left':
            tempVar = xList[iteration-2] + 22
            xList.append(tempVar)
            yList.append(yList[iteration-2])
        elif direction == 'right':
            tempVar = xList[iteration-2] - 22
            xList.append(tempVar)
            yList.append(yList[iteration-2])
        elif direction == 'up':
            tempVar = yList[iteration-2] + 22
            yList.append(tempVar)
            xList.append(xList[iteration-2])
        elif direction == 'down':
            tempVar = yList[iteration-2] - 22
            yList.append(tempVar)
            xList.append(xList[iteration-2])

    return xList, yList, rectList

def game_loop():
    # Globals in the def
    gameExit = False
    lead_x = 400
    lead_y = 300
    score = 0
    make_food = True
    food_x = 0
    food_y = 0
    direction = 'Up'
    foodEaten = 0
    snake_x = []
    snake_y = []
    rectList = []
    # Run Menu
    drawMenu()

    while not gameExit:
        playerLocation = (lead_x,lead_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True

        keys = pygame.key.get_pressed()
    # moves hero with key presses
        if keys[pygame.K_LEFT] == 1:
            direction = 'left'
        if keys[pygame.K_RIGHT] == 1:
            direction = 'right'
        if keys[pygame.K_UP] == 1:
            direction = 'up'
        if keys[pygame.K_DOWN] == 1:
            direction = 'down'

        if direction == 'left':
            lead_x -= 7
        elif direction == 'right':
            lead_x += 7
        elif direction == 'up':
            lead_y -= 7
        elif direction == 'down':
            lead_y += 7

        gameDisplay.fill(white)

        gameBorders = pygame.draw.rect(gameDisplay, black, [50,50,700,500], 2)

        scoreRect = pygame.draw.rect(gameDisplay, white, [550,550,250,50], 1)
        scoreText = pygame.font.Font.render(font,'Score: %d' % score, 1, black)
        pygame.Surface.blit(gameDisplay, scoreText, (550,550))

        if make_food:
            food_x, food_y = makeFood()
            make_food = False
            print('Made Food')

        foodRect = pygame.draw.rect(gameDisplay, red, [food_x,food_y, 10,10])
        playerRect = pygame.draw.rect(gameDisplay,blue,[lead_x,lead_y,20,20])
        snake_x, snake_y, rectList = drawSnake(lead_x,lead_y,snake_x,snake_y,foodEaten, rectList)

        if not gameBorders.contains(playerRect):
            gameExit = True
        if playerRect.contains(foodRect):
            score += 5
            foodEaten += 1
            snake_x,snake_y,rectList = addMoreSnake(snake_x,snake_y,direction,lead_x,lead_y, foodEaten)
            print(snake_x,snake_y)
            print(score)
            print('winner')
            make_food = True


        pygame.display.update()

        Clock = pygame.time.Clock()
        Clock.tick(30)


# Main Function Calls
game_intro()
game_loop()

# Quit Functions
pygame.quit()
quit()
