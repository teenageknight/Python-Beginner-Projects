#Main Variables Needed
#Number of Players leads to names of players
#Score

score = []
player_names = []
gamemode = 0   # 0 = single player, 1 = multiplayer
diff = 0
aws = 'n'

#Fixme: Delete the players that are not needed or have that option
while aws != 'y':
    num_players = int(input('How many people are playing?\n'))
    if num_players >= 2:
        print('Multiplayer Mode')
        player_names = []
        for i in range(num_players):
            x = str(input('Enter Player Name: '))
            player_names.append(x)
            score.append(0)
    elif num_players == 1:
        print('\nSingle Player Mode\n')
        diff = int(input('Press 1, 2 or 3 to select diffuculty.\n1: Easy\n2: Medium\n3: Hard\n\n'))

    #Checks to see if everyone is playing
    for i in range(len(player_names)):
        print(player_names[i])
    aws = str(input('Is this everyone? (y/n)'))
    
 
def directions():
    print('Each game, every person will get the chance to choose a word three times.\nThe people that did not choose the word can conffer to try and get the\nword. If they do not guess the word in less than six mistakes, they are\nhanged and the person that chose the word gets 100 points. If you guess the\nword before you are hanged, you split the points between the group. If at\nany time you need to access the menu, press the number 9. Have Fun!!\n')


def play_hangman(word, player):

    win = True
    word_length = len(word)
    
    #Blanks out word
    original_word_list = list(word)
    blanks_list = []
    for letter in range(word_length):
        blanks_list.append('_')
        letter += 1
    #Creates Blank String
    blanks = ' '.join(blanks_list)

    print(blanks)

    #Guesses and Stuff
    guess_left = 6
    letters_used = []
    while guess_left != 0 and '_' in blanks_list:

        decision = int(input('Press 1 to guess a letter or 2 to solve the puzzle\n'))
        if decision == 1:
            
            #Shows letters used
            x = ", ".join(letters_used)
            print('You have used the letters...\n', x)
            
            letter = str(input('\nEnter a letter.\n'))
            num_letter = 0
            letters_used.append(letter)
            for i in range(len(original_word_list)):
                if original_word_list[i] == letter:
                    blanks_list[i] = letter
                    blanks = ' '.join(blanks_list)
                    num_letter += 1
                    i += 1
                else:
                    i += 1
                    
            if num_letter > 0:
                print('There were', num_letter, letter, 'in the word')
                print(blanks)
                print('Guesses Left:', guess_left)
            else:
                print("Sorry, there were no", letter, "'s in this word")
                print(blanks)
                guess_left -= 1
                print('Guesses Left:', guess_left)
                   
                    
        elif decision == 2:
            user_guess = str(input('What do you think the word is?\n'))
            if user_guess == word:
                print('Yeah, you got it right')
                win = True
                temp_score = 100/(len(player_names)-1)
                for i in range(len(player_names)):
                    if player_names[i] == player:
                        i += 1
                    else:
                        y = score[i]
                        score[i] = y + temp_score
                        i += 1
                break
                
            else:
                print('Wrong!')
                guess_left -= 1

        if guess_left == 0:
            win = False
        elif '_' not in blanks_list:
            win = True

        return win
                

#Main Game Loop
game = 1
while game == 1:
    directions()
    #Add Menu Function

    for i in range(3):
        user_word = ''
        #Add in score card that keeps track of who is guessing
        for ix in range(len(player_names)):
            print(player_names[ix], 'enter word.')
            current_player = player_names[ix]
            user_word = str(input())
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        
            a = play_hangman(user_word, current_player)
            if a:
                print('Congratulations', current_player, 'you won!!')
            else:
                print('Sorry',current_player,'maybe next time')
            print(score)
            ix += 1
            
            

            
    #player_names[]
    break
