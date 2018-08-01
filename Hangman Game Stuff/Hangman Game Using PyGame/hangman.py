import pygame
from random import randint
import os


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
        self.infoSurface = pygame.Surface((140,240))
        self.wordsSurface = pygame.Surface((720,180))

    def on_init(self):
        pygame.init()
        pygame.font.init()

        self.gameDisplay = pygame.display.set_mode((self.windowWidth,self.windowHeight))
        pygame.display.set_caption('Hangman Game')
        pygame.display.update()

        self.createSurface()

        self.font = pygame.font.SysFont('comicsansms', 32)
        self.fontSmall = pygame.font.SysFont('comicsansms', 14)
        self.fontMedium = pygame.font.SysFont('comicsansms', 22)


        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

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
        game_over = False
        self.hangmanSurface.fill(white)
        if strike == 1:
            pygame.draw.line(self.hangmanSurface, black, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, black, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(80,80),2)

        elif strike == 2:
            pygame.draw.line(self.hangmanSurface, black, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, black, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,black,[80,100],20,2)

        elif strike == 3:
            pygame.draw.line(self.hangmanSurface, black, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, black, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,black,[80,100],20,2)

            pygame.draw.line(self.hangmanSurface,black,(80,120),(80,220),2)

        elif strike == 4:
            pygame.draw.line(self.hangmanSurface, black, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, black, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,black,[80,100],20,2)

            pygame.draw.line(self.hangmanSurface,black,(80,120),(80,220),2)

            pygame.draw.line(self.hangmanSurface,black,(20,160),(140,160),2)

        elif strike == 5:
            pygame.draw.line(self.hangmanSurface, black, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, black, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,black,[80,100],20,2)

            pygame.draw.line(self.hangmanSurface,black,(80,120),(80,220),2)

            pygame.draw.line(self.hangmanSurface,black,(20,160),(140,160),2)

            pygame.draw.line(self.hangmanSurface,black,(80,220),(20,280),2)

        elif strike == 6:
            pygame.draw.line(self.hangmanSurface, black, (120,320),(280,320),2)
            pygame.draw.line(self.hangmanSurface, black, (200,40),(200,320),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(200,40),2)
            pygame.draw.line(self.hangmanSurface, black, (80,40),(80,80),2)

            pygame.draw.circle(self.hangmanSurface,black,[80,100],20,2)

            pygame.draw.line(self.hangmanSurface,black,(80,120),(80,220),2)

            pygame.draw.line(self.hangmanSurface,black,(20,160),(140,160),2)

            pygame.draw.line(self.hangmanSurface,black,(80,220),(20,280),2)

            pygame.draw.line(self.hangmanSurface,black,(80,220),(140,280),2)
            game_over = True
        return game_over

    def updateInfo(self,score,strike):
        self.infoSurface.fill(white)

        scoreCard = pygame.draw.rect(self.infoSurface,blue,[20,20,100,90])
        strikeCard = pygame.draw.rect(self.infoSurface,blue,[20,130,100,90])

        scoreTitleBox = pygame.draw.rect(self.infoSurface,red,[25,25,90,20])
        scoreTitleText = pygame.font.Font.render(self.fontSmall,'Score', 1, white)
        scoreBox = pygame.draw.rect(self.infoSurface,red,[25,50,90,55])
        scoreText = pygame.font.Font.render(self.font,'{0}'.format(score), 1, white)

        pygame.Surface.blit(self.infoSurface, scoreTitleText, (70 - scoreTitleText.get_width() // 2, 35 - scoreTitleText.get_height() // 2))
        pygame.Surface.blit(self.infoSurface, scoreText, (70 - scoreText.get_width() // 2, 75 - scoreText.get_height() // 2))

        strikeTitle = pygame.draw.rect(self.infoSurface,red,[25,135,90,20])
        strikeTitle = pygame.font.Font.render(self.fontSmall,'Strikes', 1, white)
        strikeBox = pygame.draw.rect(self.infoSurface,red,[25,160,90,55])
        strikeText = pygame.font.Font.render(self.font,'{0}'.format(strike), 1, white)

        pygame.Surface.blit(self.infoSurface, strikeTitle, (70 - strikeTitle.get_width() // 2, 145 - strikeTitle.get_height() // 2))
        pygame.Surface.blit(self.infoSurface, strikeText, (70 - strikeText.get_width() // 2, 187.5 - strikeText.get_height() // 2))

    def updateLetterGuessed(self,guesses):
        self.lettersGuessedSurface.fill(white)

        lettersGuessedTitle = pygame.draw.rect(self.lettersGuessedSurface,red,[80,20,120,20])
        lettersGuessedTitleText = pygame.font.Font.render(self.fontSmall,'Letters Guessed', 1, white)

        pygame.Surface.blit(self.lettersGuessedSurface, lettersGuessedTitleText, (140 - lettersGuessedTitleText.get_width() // 2, 30 - lettersGuessedTitleText.get_height() // 2))

        lettersGuessedBox = pygame.draw.rect(self.lettersGuessedSurface,red,[20,60,240,120])
        if len(guesses) == 0:
            lettersGuessed = pygame.font.Font.render(self.fontSmall,'No Letters Guessed', 1, white)
            pygame.Surface.blit(self.lettersGuessedSurface, lettersGuessed, (140 - lettersGuessed.get_width() // 2, 120 - lettersGuessed.get_height() // 2))
        elif len(guesses) > 0:
            lettersGuessed = pygame.font.Font.render(self.fontSmall,'{0}'.format(guesses), 1, white)
            pygame.Surface.blit(self.lettersGuessedSurface, lettersGuessed, (140 - lettersGuessed.get_width() // 2, 120 - lettersGuessed.get_height() // 2))

    def updateLetters(self,chosen_word,word_len, letters_list,blanks_list,user_pick,strikes):
        startPos = 10
        game_over = False
        self.wordsSurface.fill(white)
        if user_pick in letters_list:
            for i in range(len(letters_list)):
                if letters_list[i] == user_pick:
                    blanks_list[i] = user_pick
            for i in range(len(letters_list)):
                # if its a blank draw a blank
                if blanks_list[i] == '_':
                    pygame.draw.line(self.wordsSurface,black,(startPos,90),(startPos+20,90),2)
                    startPos += 30
                else:
                    pygame.draw.rect(self.wordsSurface,white,[startPos,60,20,30])
                    letter = pygame.font.Font.render(self.fontSmall,'{0}'.format(blanks_list[i]), 1, black)
                    pygame.Surface.blit(self.wordsSurface, letter, ((startPos+10) - letter.get_width() // 2, 75 - letter.get_height() // 2))
                    startPos += 30
        else:
            strikes = strikes + 1
            for i in range(len(letters_list)):
                # if its a blank draw a blank
                if blanks_list[i] == '_':
                    pygame.draw.line(self.wordsSurface,black,(startPos,90),(startPos+20,90),2)
                    startPos += 30
                else:
                    pygame.draw.rect(self.wordsSurface,white,[startPos,60,20,30])
                    letter = pygame.font.Font.render(self.fontSmall,'{0}'.format(blanks_list[i]), 1, black)
                    pygame.Surface.blit(self.wordsSurface, letter, ((startPos+10) - letter.get_width() // 2, 75 - letter.get_height() // 2))
                    startPos += 30

        if '_' not in blanks_list:
            print('No Blanks')
            game_over = True
        return strikes, game_over, blanks_list

    def checkHighscore(self,score):
        print('Checking Highscore')
        highscore = False
        infile = open('highscores.txt', 'r')
        info = infile.readlines()
        print(info)
        scores = []
        for i in range(len(info)):
            if i % 2 == 0:
                temp = info[i].rstrip()
                print(temp)
                temp = int(temp)
                print(temp)
                scores.append(temp)

        print(scores)
        for i in range(len(scores)):
            if scores[i] < score:
                highscore = True
                print('highscore')
        return highscore

    def addHighscore(self,score):
        print('add new highscore')
        name = str(input('Enter your Name:\n'))
        infile = open('highscores.txt', 'r')
        info = infile.readlines()
        print(info)
        scores = []
        names = []
        iterationScore = 0
        iterationName = 0
        for i in range(len(info)):
            if i % 2 == 0:
                temp = info[i].rstrip()
                temp = int(temp)
                scores.append(temp)
            elif i % 2 == 1:
                temp = info[i].rstrip()
                names.append(temp)
        infile.close()

        os.remove('highscores.txt')
        print('File Removed')

        print('New File Created')
        newfile = open('highscores.txt', 'w+')
        for i in range(len(scores)):
            if scores[i] < score:
                scores[i] = score
                names[i] = name
                break
            else:
                pass
        print('Printing Scores and Names')
        print(scores)
        print(names)

        for i in range(len(scores)):
            scores[i] = str(scores[i]) + '\n'
        for i in range(len(names)):
            names[i] = str(names[i]) + '\n'

        print(scores)
        print('Iterating')
        for i in range(len(info)):
            if i % 2 == 0:
                print(scores[iterationScore])
                newfile.write(scores[iterationScore])
                iterationScore += 1
            elif i % 2 == 1:
                newfile.write(names[iterationName])
                iterationName += 1
        newfile.close()
    def gameOver(self,word,score):
        self.gameDisplay.fill(white)
        gameOverTitleRect = pygame.draw.rect(self.gameDisplay,red,[225,25,350,75])
        gameOverTitleText = pygame.font.Font.render(self.font,'GAME OVER', 1, white)

        wordText = pygame.font.Font.render(self.fontMedium,'Your word was:', 1, black)
        wordText2 = pygame.font.Font.render(self.fontMedium,'{0}'.format(word), 1, black)

        pygame.Surface.blit(self.gameDisplay, gameOverTitleText, (400 - gameOverTitleText.get_width() // 2, 67 - gameOverTitleText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, wordText, (175 - wordText.get_width() // 2, 150 - wordText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, wordText2, (550 - wordText2.get_width() // 2, 150 - wordText2.get_height() // 2))

        # Makes Buttons for menu
        startButton = pygame.draw.rect(self.gameDisplay,green,[250,225,300,75])
        highscoreButton = pygame.draw.rect(self.gameDisplay,green,[250,325,300,75])
        quitButton = pygame.draw.rect(self.gameDisplay,green,[250,425,300,75])

        # Renders text for menu
        startButtonText = pygame.font.Font.render(self.font,'Start Hangman', 1, white)
        highscoreButtonText = pygame.font.Font.render(self.font,'View Highscores', 1, white)
        quitButtonText = pygame.font.Font.render(self.font,'Quit', 1, white)

        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 267 - startButtonText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 367 - highscoreButtonText.get_height() // 2))
        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 467 - quitButtonText.get_height() // 2))

        pygame.display.update()
        user_pick = False

        while not user_pick:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    if pygame.Rect.collidepoint(startButton, mouse_position):
                        startButton = pygame.draw.rect(self.gameDisplay,blue,[250,225,300,75])
                        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 267 - startButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 367 - highscoreButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 467 - quitButtonText.get_height() // 2))
                        pygame.display.update()
                    elif pygame.Rect.collidepoint(highscoreButton, mouse_position):
                        highscoreButton = pygame.draw.rect(self.gameDisplay,blue,[250,325,300,75])
                        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 267 - startButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 367 - highscoreButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 467 - quitButtonText.get_height() // 2))
                        pygame.display.update()
                    elif pygame.Rect.collidepoint(quitButton, mouse_position):
                        quitButton = pygame.draw.rect(self.gameDisplay,blue,[250,425,300,75])
                        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 267 - startButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 367 - highscoreButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 467 - quitButtonText.get_height() // 2))
                        pygame.display.update()
                    else:
                        startButton = pygame.draw.rect(self.gameDisplay,green,[250,225,300,75])
                        highscoreButton = pygame.draw.rect(self.gameDisplay,green,[250,325,300,75])
                        quitButton = pygame.draw.rect(self.gameDisplay,green,[250,425,300,75])
                        pygame.Surface.blit(self.gameDisplay, startButtonText, (400 - startButtonText.get_width() // 2, 267 - startButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, highscoreButtonText, (400 - highscoreButtonText.get_width() // 2, 367 - highscoreButtonText.get_height() // 2))
                        pygame.Surface.blit(self.gameDisplay, quitButtonText, (400 - quitButtonText.get_width() // 2, 467 - quitButtonText.get_height() // 2))
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

    def playGame(self,score = 0):
        file_name = self.getWordFile()
        chosen_word, word_len = self.chooseWord(file_name)

        letters_list = list(chosen_word)
        blanks_list = []
        for i in range(len(letters_list)):
            blanks_list.append('_')

        user_pick = False
        strikes = 0
        guesses = []
        game_over = False

        while not user_pick:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.gameDisplay.fill(white)
            user_guess = str(input('Enter A Letter\n'))
            guesses.append(user_guess)
            strikes, game_over, blanks_list = self.updateLetters(chosen_word,word_len,letters_list,blanks_list,user_guess,strikes)
            if game_over:
                if strikes == 6:
                    print('Game Over')
                    highscore = self.checkHighscore(score)
                    if highscore:
                        self.addHighscore(score)
                        self.viewHighscores('highscores.txt')
                    else:
                        self.gameOver(chosen_word,score)
                else:
                    score += 50
                    self.playGame(score)
            game_over = self.drawStickMan(strikes)
            if game_over:
                if strikes == 6:
                    print('Game Over')
                    highscore = self.checkHighscore(score)
                    if highscore:
                        self.addHighscore(score)
                        self.viewHighscores('highscores.txt')
                    else:
                        self.gameOver(chosen_word,score)
                else:
                    score += 50
                    self.playGame(score)

            self.updateInfo(score,strikes)
            self.updateLetterGuessed(guesses)
            pygame.Surface.blit(self.gameDisplay,self.wordsSurface, (40,400))
            pygame.Surface.blit(self.gameDisplay,self.hangmanSurface,(20,20))
            pygame.Surface.blit(self.gameDisplay,self.infoSurface,(320,20))
            pygame.Surface.blit(self.gameDisplay,self.lettersGuessedSurface,(480,20))
            pygame.display.update()



    def mainLoop(self):
        while self._running:
            self.on_init()
            self.drawMainMenu()

"""
This part is for debuging. Make real game function later
"""
game = App()
game.mainLoop()
