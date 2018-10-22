'''
Title: Snake Game

Description: A game where a player (the snake), eats pieces of food to grow bigger.
             If the snake hits the edge or the side, it will die.

Created By: Bryce Jackson
            https://github.com/teenageknight
'''

import pygame

def initPygame():
    pygame.init()

    gameDiplay = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Slither')

    pygame.display.update()

def main():
    initPygame()

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

if __name__ == '__main__':
    main()
