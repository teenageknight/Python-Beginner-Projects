import pygame
from random import randint



#Defines the colors used

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
purple = (160,32,240)
pink = (255,192,203)
black = (0,0,0)
green = (0,255,0)
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
    def createSurface(self):
        self.hangmanSurface = pygame.Surface((280,340))
        self.lettersGuessedSurface = pygame.Surface((280,200))
        self.infoSurface = pygame.Surface((140,220))

    def on_init(self):
        pygame.init()
        pygame.font.init()

        self.gameDisplay = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        pygame.display.set_caption('Hangman Game')
        pygame.display.update()

        self.createSurface()

        self.font = pygame.font.SysFont('comicsansms', 32)
        self.fontSmall = pygame.font.SysFont('comicsansms', 11)

        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    # has the music functions
    # FIXME: Consider changing mp3 to ogg
    def playMusic(self, file_name):
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play(1)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def viewHighscores(self, file_name):
        user_pick = False

        infile = open(file_name, 'r')
        scores = infile.readlines()
        print(scores)

        self.gameDisplay.fill(white)
        startGameButton = pygame.draw.rect(self.gameDisplay,blue,[500,150,250,50])
        mainMenuButton = pygame.draw.rect(self.gameDisplay,blue, [500,262.5,250,50])
        quitGameButton = pygame.draw.rect(self.gameDisplay,blue,[500,375,250,50])
        highscoresTitle = pygame.draw.rect(self.gameDisplay,white,[125,50,550,50])

        startGameButtonText = pygame.font.Font.render(self.font,'Play Game', 1, white)
        mainMenuButtonText = pygame.font.Font.render(self.font,'Main Menu', 1, white)
        quitGameButtonText = pygame.font.Font.render(self.font,'Quit', 1, white)
        highscoresTitleText = pygame.font.Font.render(self.font,'Highscores', 1, black)


        pygame.Surface.blit(self.gameDisplay, startGameButtonText, (625 - startGameButtonText.get_width() // 2, 175 - startGameButtonText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, mainMenuButtonText, (625 - mainMenuButtonText.get_width() // 2, 287.5 - mainMenuButtonText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, quitGameButtonText, (625 - quitGameButtonText.get_width() // 2, 400 - quitGameButtonText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, highscoresTitleText, (400 - highscoresTitleText.get_width() // 2, 75 - highscoresTitleText.get_height() // 2))

        pygame.display.update()

        # These varibles are a list of codinates for the boxes that hold the text
        placeBoxCor = [[25,125],[25,175],[25,225],[25,275],[25,325],[25,375],[25,425],[25,475],[25,525],[25,575]]
        nameBoxCor = [[75,125],[75,175],[75,225],[75,275],[75,325],[75,375],[75,425],[75,475],[75,525],[75,575]]

        lineNum = 1
        scoreIterations =0
        for i in range(len(placeBoxCor)):
            for ix in range(len(placeBoxCor[i])):
                if lineNum % 2 == 1:
                    box = pygame.draw.rect(self.gameDisplay,white,[placeBoxCor[i][0],placeBoxCor[i][1],25,25])
                    boxText = pygame.font.Font.render(self.fontSmall,'%s' % scores[scoreIterations].rstrip(), 1, black)
                    pygame.Surface.blit(self.gameDisplay, boxText, (placeBoxCor[i][0],placeBoxCor[i][1]))
                    pygame.display.update()
                elif lineNum % 2 == 0:
                    box = pygame.draw.rect(self.gameDisplay,white,[nameBoxCor[i][0],nameBoxCor[i][1],275,25])
                    boxText = pygame.font.Font.render(self.fontSmall,'%s' % scores[scoreIterations].rstrip(), 1, black)
                    pygame.Surface.blit(self.gameDisplay, boxText, (nameBoxCor[i][0],nameBoxCor[i][1]))
                    pygame.display.update()
                lineNum += 1
                scoreIterations += 1


        while not user_pick:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running=False
                if event.type == pygame.MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    if pygame.Rect.collidepoint(startGameButton, mouse_position):
                        startGameButton = pygame.draw.rect(self.gameDisplay,red,[500,150,250,50])
                        pygame.Surface.blit(self.gameDisplay, startGameButtonText, (625 - startGameButtonText.get_width() // 2, 175 - startGameButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, mainMenuButtonText, (625 - mainMenuButtonText.get_width() // 2, 287.5 - mainMenuButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitGameButtonText, (625 - quitGameButtonText.get_width() // 2, 400 - quitGameButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoresTitleText, (400 - highscoresTitleText.get_width() // 2, 75 - highscoresTitleText.get_height() // 2))
                        pygame.display.update()
                    elif pygame.Rect.collidepoint(mainMenuButton, mouse_position):
                        mainMenuButton = pygame.draw.rect(self.gameDisplay,red, [500,262.5,250,50])
                        pygame.Surface.blit(self.gameDisplay, startGameButtonText, (625 - startGameButtonText.get_width() // 2, 175 - startGameButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, mainMenuButtonText, (625 - mainMenuButtonText.get_width() // 2, 287.5 - mainMenuButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitGameButtonText, (625 - quitGameButtonText.get_width() // 2, 400 - quitGameButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoresTitleText, (400 - highscoresTitleText.get_width() // 2, 75 - highscoresTitleText.get_height() // 2))
                        pygame.display.update()
                    elif pygame.Rect.collidepoint(quitGameButton, mouse_position):
                        quitGameButton = pygame.draw.rect(self.gameDisplay,red,[500,375,250,50])
                        pygame.Surface.blit(self.gameDisplay, startGameButtonText, (625 - startGameButtonText.get_width() // 2, 175 - startGameButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, mainMenuButtonText, (625 - mainMenuButtonText.get_width() // 2, 287.5 - mainMenuButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitGameButtonText, (625 - quitGameButtonText.get_width() // 2, 400 - quitGameButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoresTitleText, (400 - highscoresTitleText.get_width() // 2, 75 - highscoresTitleText.get_height() // 2))
                        pygame.display.update()
                    else:
                        startGameButton = pygame.draw.rect(self.gameDisplay,blue,[500,150,250,50])
                        mainMenuButton = pygame.draw.rect(self.gameDisplay,blue, [500,262.5,250,50])
                        quitGameButton = pygame.draw.rect(self.gameDisplay,blue,[500,375,250,50])
                        highscoresTitle = pygame.draw.rect(self.gameDisplay,white,[125,50,550,50])
                        pygame.Surface.blit(self.gameDisplay, startGameButtonText, (625 - startGameButtonText.get_width() // 2, 175 - startGameButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, mainMenuButtonText, (625 - mainMenuButtonText.get_width() // 2, 287.5 - mainMenuButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitGameButtonText, (625 - quitGameButtonText.get_width() // 2, 400 - quitGameButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoresTitleText, (400 - highscoresTitleText.get_width() // 2, 75 - highscoresTitleText.get_height() // 2))
                        pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickPos = pygame.mouse.get_pos()
                    print(clickPos)
                    if pygame.Rect.collidepoint(startGameButton, clickPos):
                        print('Game Started')
                        self.playGame()
                        user_pick = True
                    elif pygame.Rect.collidepoint(mainMenuButton, clickPos):
                        print('going to main menu')
                        user_pick = True
                        self.drawMainMenu()
                    elif pygame.Rect.collidepoint(quitGameButton,clickPos):
                        print('Quit Game')
                        user_pick = True
                        pygame.quit()
                        quit()


    def drawMainMenu(self):
        user_pick = False

        self.gameDisplay.fill(black)

        # Makes Buttons for menu
        startButton = pygame.draw.rect(self.gameDisplay,green,[200,75,400,100])
        highscoreButton = pygame.draw.rect(self.gameDisplay,green,[200,225,400,100])
        quitButton = pygame.draw.rect(self.gameDisplay,green,[200,375,400,100])

        # Renders text for menu
        startButtonText = pygame.font.Font.render(self.font,'Start Hangman', 1, white)
        highscoreButtonText = pygame.font.Font.render(self.font,'View Highscores', 1, white)
        quitButtonText = pygame.font.Font.render(self.font,'Quit', 1, white)

        # Puts the text on the surface
        # FIXME: make sure to change so it renders right in the middle
        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 125 - startButtonText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 275 - highscoreButtonText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 425 - quitButtonText.get_height() // 2))
        pygame.display.update()

        while not user_pick:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running=False
                # This event makes the button change font when hovered over.
                if event.type == pygame.MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    if pygame.Rect.collidepoint(startButton, mouse_position):
                        startButton = pygame.draw.rect(self.gameDisplay,blue,[200,75,400,100])
                        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 125 - startButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 275 - highscoreButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 425 - quitButtonText.get_height() // 2))
                        pygame.display.update()
                    elif pygame.Rect.collidepoint(highscoreButton, mouse_position):
                        highscoreButton = pygame.draw.rect(self.gameDisplay,blue,[200,225,400,100])
                        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 125 - startButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 275 - highscoreButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 425 - quitButtonText.get_height() // 2))
                        pygame.display.update()
                    elif pygame.Rect.collidepoint(quitButton, mouse_position):
                        quitButton = pygame.draw.rect(self.gameDisplay,blue,[200,375,400,100])
                        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 125 - startButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 275 - highscoreButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 425 - quitButtonText.get_height() // 2))
                        pygame.display.update()
                    else:
                        startButton = pygame.draw.rect(self.gameDisplay,green,[200,75,400,100])
                        highscoreButton = pygame.draw.rect(self.gameDisplay,green,[200,225,400,100])
                        quitButton = pygame.draw.rect(self.gameDisplay,green,[200,375,400,100])
                        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 125 - startButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 275 - highscoreButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 425 - quitButtonText.get_height() // 2))
                        pygame.display.update()

                # This event is the button logic
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickPos = pygame.mouse.get_pos()
                    print(clickPos)
                    if pygame.Rect.collidepoint(startButton, clickPos):
                        print('Game Started')
                        self.playGame()
                        user_pick = True
                    elif pygame.Rect.collidepoint(highscoreButton, clickPos):
                        print('Viewing Highscores')
                        user_pick = True
                        self.viewHighscores('highscores.txt')
                    elif pygame.Rect.collidepoint(quitButton,clickPos):
                        print('Quit Game')
                        user_pick = True
                        pygame.quit()
                        quit()

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

    def drawStickMan(self, strike):
        if strike == 1:
            pygame.draw.line(self.hangmanSurface, white, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, white, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(80,80),2)

        elif strike == 2:
            pygame.draw.line(self.hangmanSurface, white, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, white, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,white,[80,100],20,2)

        elif strike == 3:
            pygame.draw.line(self.hangmanSurface, white, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, white, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,white,[80,100],20,2)

            pygame.draw.line(self.hangmanSurface,white,(80,120),(80,220),2)

        elif strike == 4:
            pygame.draw.line(self.hangmanSurface, white, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, white, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,white,[80,100],20,2)

            pygame.draw.line(self.hangmanSurface,white,(80,120),(80,220),2)

            pygame.draw.line(self.hangmanSurface,white,(20,160),(140,160),2)

        elif strike == 5:
            pygame.draw.line(self.hangmanSurface, white, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, white, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,white,[80,100],20,2)

            pygame.draw.line(self.hangmanSurface,white,(80,120),(80,220),2)

            pygame.draw.line(self.hangmanSurface,white,(20,160),(140,160),2)

            pygame.draw.line(self.hangmanSurface,white,(80,220),(20,280),2)

        elif strike == 6:
            pygame.draw.line(self.hangmanSurface, white, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, white, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, white, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,white,[80,100],20,2)

            pygame.draw.line(self.hangmanSurface,white,(80,120),(80,220),2)

            pygame.draw.line(self.hangmanSurface,white,(20,160),(140,160),2)

            pygame.draw.line(self.hangmanSurface,white,(80,220),(20,280),2)

            pygame.draw.line(self.hangmanSurface,white,(80,220),(140,280),2)

    def updateInfo(self):
        pygame.draw.rect(self.infoSurface,blue,[])

    def updateLetterGuessed(self):
        pass

    def playGame(self):
        file_name = self.getWordFile()
        chosen_word, word_len = self.chooseWord(file_name)

        strikes = 0

        user_pick = False
        while not user_pick:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running=False

            self.gameDisplay.fill(white)
            self.drawStickMan(6)
            pygame.Surface.blit(self.gameDisplay,self.hangmanSurface,(20,20))
            pygame.Surface.blit(self.gameDisplay,self.infoSurface,(320,20))
            pygame.Surface.blit(self.gameDisplay,self.lettersGuessedSurface,(480,20))


            pygame.display.update()


    def mainLoop(arg):
        pass

"""
This part is for debuging. Make real game function later
"""
game = App()
game.on_init()

game.drawMainMenu()
