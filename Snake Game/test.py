import pygame

pygame.init()

# Initalizes the display settings. The first is the size and the second is the title.
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Test of PyGame')
pygame.display.update()

'''
Global Variables
'''
##########################
# Initalizes the colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Sets the game exit Variables
gameExit = False

##########################

while not gameExit:
    loop2 = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect.collidepoint(event.pos):
                loop2=True

        if loop2:
            gameDisplay.fill(blue)
            gameExit = True
        gameDisplay.fill(white)
        # rect(surface,color, [x location, y location, width, height])
        pygame.draw.rect(gameDisplay, black, [400,300,10,10])
        pygame.display.update()

pygame.quit()
quit()
