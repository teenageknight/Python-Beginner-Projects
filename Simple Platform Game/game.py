
# Imports
import pygame

walkRight = [pygame.image.load(pygame.path.join("images\sprites\charecter",'R1.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'R2.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'R3.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'R4.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'R5.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'R6.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'R7.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'R8.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'R9.png'))]
walkLeft = [pygame.image.load(pygame.path.join("images\sprites\charecter",'L1.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'L2.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'L3.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'L4.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'L5.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'L6.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'L7.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'L8.png')), pygame.image.load(pygame.path.join("images\sprites\charecter",'L9.png'))]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load(pygame.path.join("images\sprites\charecter",'standing.png')﻿)

print(walkRight[8])
# class Player(object):
#     """Class that defines how to make a player."""
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.isJump = False
#         self.jumpCount = 10
#         self.left = False
#         self.right = False
#         self.walkCount = 0
#
#     def draw(self, window):
#         if self.walkCount + 1 >= 27:
#             self.walkCount = 0
#
#         if self.left:



# # Defines game class. All of the neccesay game functions
# class Game:
#     """defines the main game functions"""
#
#     # FIXME: If you add variables, fix this function
#     def __init__(self):
#         self.screenWidth = 990
#         self.screenHeight = 540
#
#     # defines what to do on initalization
#     def on_init(self):
#         # Calles and creates menu class
#         self.menu = Menu(False)
#         self.menu.setUpMenu()
#
#         # Initalizes pygame nescesities
#         pygame.init()
#         pygame.font.init()
#
#         # Initalizes pygame window size
#         self.gameDisplay = pygame.display.set_mode((self.screenWidth, self.screenHeight))
#         pygame.display.set_caption('Jumpman')
#         pygame.display.update()
#
#     def levelSelect(self):
#         user_pick = False
#         while not user_pick:
#             pass
#
#     def main(self):
#         # Calls the initalization function to carry out first actions
#         self.on_init()
#
#         # Calls the levelSelect Function
#         self.levelSelect()
#
#
#
# if __name__ == '__main__':
#     game = Game()
#     game.main()
