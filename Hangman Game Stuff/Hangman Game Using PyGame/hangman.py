import pygame
from random import randint



#Defines the colors used

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
purple = (160,32,240)
pink = (255,192,203)
black = (0,0,0)
white = (255,255,255)

class App:
    """docstring for App."""

    # Global Variables
    windowWidth = 800
    windowHeight = 600

    def __init__(self):
        self._running = True

    # This function is run on intialization. It initalizes the following
    # Display, pygame, and capting
    def on_init(self):
        pygame.init()
        pygame.font.init()

        self.gameDisplay = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        pygame.display.set_caption('Hangman Game')
        pygame.display.update()

        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    # has the music functions
    # FIXME: Consider changing mp3 to ogg
    def playMusic(self, file_name):
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play(-1)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def drawMainMenu(self):
        self.playMusic('wiiSports.mp3')


        # startButton =
        # highscoreButton =
        # quitButton =

    # Gets the file that holds the words.
    def getWordFile(self):
        try:
            #Check for "wordlist.txt"
            with open("wordlist.txt", "r"): file_name = "wordlist.txt"
        except IOError:
            # If wordlist.txt cannot be found, then we ask the user to specify a text file
            found_file = False
            file_name = input('Please specify a text file containing a list of words for the Hangman game to choose from (include the full file path if the file is in a different directory than the Hangman program): ')
            while not(found_file):
                try:
                    with open(file_name, "r"): found_file= True
                except IOError:
                    file_name = input('\n{0} was not found!\n\nPlease try again, or specify a different file (include the full file path if the file is in a different directory than the Hangman program): '.format(file_name))
                    return file_name

    def chooseWord(self, file_name):
        infile = open(file_name, 'r')
        wordlist = infile.readlines()
        total_words = len(wordlist)
        random_num = randint(0, total_words - 1)

        chosen_word = wordlist[random_num].replace('\n', '')
        word_len = len(chosen_word)
        return chosen_word, word_len

"""
This part is for debuging. Make real game function later
"""
game = App()
game.on_init()

game.drawMainMenu()
