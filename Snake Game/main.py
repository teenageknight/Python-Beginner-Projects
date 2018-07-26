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

# Initilazation
pygame.init()
pygame.font.init()

# Initalizes the display settings. The first is the size and the second is the title.
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')
pygame.display.update()

def drawMenu():
    # Play new game button
    user_pick = False

    startButton = pygame.draw.rect(gameDisplay, green, [250,100,300,100])
    quitButton = pygame.draw.rect(gameDisplay, green, [250,350,300,100])

    font = pygame.font.SysFont('comicsansms', 32)
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



def player_snake(xPos,yPos,numDotsEaten):
    x = xPos
    y = yPos

    playerSpeed = 0 # FIXME: Add in speed in relation to number of dots numDotsEaten
    pygame.draw.rect(gameDisplay,black, [x,y,10,10])

def game_intro():
    '''
    Can create later using the pygame.font library for plain typing.
    '''
    pass

def game_loop():
    # Globals in the def
    number_dots_eaten = 0
    speed = 10
    gameExit = False
    drawMenu()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
        gameDisplay.fill(white)

        pygame.display.update()


# Main Function Calls
game_intro()
game_loop()

# Quit Functions
pygame.quit()
quit()
