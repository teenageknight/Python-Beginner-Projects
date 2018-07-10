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
from art import *

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
                with open(file_name, "r": found_file= True)
            except IOError:
                file_name = input('\n{0} was not found!\n\nPlease try again, or specify a different file (include the full file path if the file is in a different directory than the Hangman program): '.format(file_name))
    return file_name
