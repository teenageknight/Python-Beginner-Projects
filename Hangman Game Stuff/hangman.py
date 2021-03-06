############################################################
#                                                          #
#    hangman.py                                            #
#    -------------------------------------------------     #
#                                                          #
#    Description: A text based word guessing game where    #
#    the user attempts to guess letters to solve a word    #
#    from a list of words.                                 #
#                                                          #
#    Author: Bryce Jackson (bkajackson99@gmail.com)        #
#          (https://github.com/teenageknight)              #
#                                                          #
#    Further Ideas: Making a better graphical interphase   #
#    using PyGame or a gui like tkinter.                   #
#                                                          #
############################################################

#Import required libraries and functions
from random import randint

#getWordFile()
#
#Get a txt file with the words required for the game
def getWordFile():
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

# chooseWord()
# Chooses a word randomly from the list of words taken from the input file
def chooseWord(file_name):
    infile = open(file_name, 'r')
    wordlist = infile.readlines()
    total_words = len(wordlist)
    random_num = randint(0, total_words - 1)

    chosen_word = wordlist[random_num].replace('\n', '')
    word_len = len(chosen_word)
    return chosen_word, word_len

# Possibly move this to new art file
def drawMan(strike):
    if strike == 1:
        print("   _ _")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("==========")

    elif strike == 2:
        print("   _ _")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("==========")

    elif strike == 3:
        print("   _ _")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("==========")

    elif strike == 4:
        print("   _ _")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("==========")

    elif strike == 5:
        print("   _ _")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("==========")

    elif strike == 6:
        print("   _ _")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("      |")
        print("==========")

    elif strike == 7:
        print("   _ _")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("==========")
    else:
        print('You have no strikes')

    # Creates a function for a victory or a loss
def banners(win, word):
    if win:
        print('############################################################')
        print('#                                                          #')
        print('#       Congratulations, you have won the game!            #')
        print('#                                                          #')
        print('############################################################')
    else:
        drawMan(7)
        print('############################################################')
        print('#                                                          ')
        print('#                      You Got Hung                        ')
        print('#                       You Lose                           ')
        print('#   The word was: {0}' .format(word))
        print('#                                                          ')
        print('############################################################')





# Define Main Game loop
def main(win, file_name):
    # If there is no word list, then get one
    if not(file_name):
        file_name = getWordFile()

    # Choose a random word and store it and the length
    word, word_len = chooseWord(file_name)

    blanks = '__'
    for i in range(word_len-1):
        blanks = blanks + ' __'

    strikes = 0
    guessed_letter=[]
    game_won = False

    while strikes < 7 and game_won == False:

        drawMan(strikes)
        print(blanks)
        print(guessed_letter)

        guess = input('Enter a letter: ')

        if guess == ' ' or guess == '' or len(guess) != 1:
            print('\nPlease only guess only one letter at a time.')
            continue

        if guess in word.lower() and not(guess in guessed_letter):
            guessed_letter.append(guess)
            blanks = word
            for letter in word:
                if (not (letter.lower() in word) or not(letter.lower() in guessed_letter)) and letter != ' ':
                    blanks = blanks.replace(letter, ' __ ')

            if blanks == word:
                game_won = True
            else:
                print("Nice! {0} is in the word. Try another letter.\n".format(guess.upper()))
        elif guess in guessed_letter:
            print('\nYou already guessed the letter {0}. Try again.\n' .format(guess.upper()))
        else:
            guessed_letter.append(guess)
            strikes += 1
            print('{0} is a wrong guess! Try another letter.\n'.format(guess.upper()))

    banners(game_won, word)

main(False,False)
