import pygame

# Colors
# -------------------
AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
# -------------------

pygame.init()

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode([1450, 1000])

pygame.display.set_caption("Nines")

# Loop until the user clicks the close button.
done = False

clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    screen.fill((GREEN))

    pygame.draw.rect(screen, BLACK, [100,300, 71,96],2)
    pygame.draw.rect(screen, BLACK, [190,300, 71,96],2)
    pygame.draw.rect(screen, BLACK, [280,300, 71,96],2)

    pygame.draw.rect(screen, BLACK, [100,410, 71,96],2)
    pygame.draw.rect(screen, BLACK, [190,410, 71,96],2)
    pygame.draw.rect(screen, BLACK, [280,410, 71,96],2)

    pygame.draw.rect(screen, BLACK, [100,520, 71,96],2)
    pygame.draw.rect(screen, BLACK, [190,520, 71,96],2)
    pygame.draw.rect(screen, BLACK, [280,520, 71,96],2)

    pygame.draw.rect(screen, BLACK, [635,410, 71,96],2)
    pygame.draw.rect(screen, BLACK, [744,410, 71,96],2)

    pygame.draw.rect(screen, BLACK, [1080,300, 71,96],2)
    pygame.draw.rect(screen, BLACK, [1170,300, 71,96],2)
    pygame.draw.rect(screen, BLACK, [1260,300, 71,96],2)

    pygame.draw.rect(screen, BLACK, [1080,410, 71,96],2)
    pygame.draw.rect(screen, BLACK, [1170,410, 71,96],2)
    pygame.draw.rect(screen, BLACK, [1260,410, 71,96],2)

    pygame.draw.rect(screen, BLACK, [1080,520, 71,96],2)
    pygame.draw.rect(screen, BLACK, [1170,520, 71,96],2)
    pygame.draw.rect(screen, BLACK, [1260,520, 71,96],2)



    pygame.display.flip()

    clock.tick(20)

pygame.quit()
