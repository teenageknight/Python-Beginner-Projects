import pygame

pygame.init()
pygame.mixer.init()

# Initalizes the display settings. The first is the size and the second is the title.
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Test of PyGame')
pygame.display.update()
gameExit = False
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
loop2 = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            loop2 = True


    gameDisplay.fill(white)

    pygame.display.update()
    pygame.mixer.music.load('wiiSports.ogg')
    pygame.mixer.music.play()
    pygame.display.update()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
