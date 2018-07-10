import sys, pygame
pygame.init()

#Defines the colors used
# FIXME: Delete the colors that are not used
blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
purple = (160,32,240)
pink = (255,192,203)
black = (0,0,0)
white = (255,255,255)

size = width, height = 960, 540
screen = pygame.display.set_mode(size)

while True:
    #####################################################################
    #  This code checks to see if the user clicked the QUIT button,
    #  e.g. the red X on Windows, or the red circle on Mac
    #  The code checks a list of "events", and if any of those is QUIT
    #  then it does two things: pygame.quit, and then sys.exit
    #####################################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    screen.fill(white)

    pygame.draw.circle(screen, black, (480,270), 100, 0)
    pygame.display.update()
# Quit Function
# done = False
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 done = True
#                 break # break out of the for loop
#         elif event.type == pygame.QUIT:
#             done = True
#             break # break out of the for loop
#     if done:
#         break # to break out of the while loop
