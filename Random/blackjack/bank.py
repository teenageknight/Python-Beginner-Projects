'''
    Filename: bank.py

    Creater: Bryce
'''
# Imports
import os

class User(object):
    """docstring for User."""
    # def __init__(self, arg):
    #     self.arg = arg

    def getUserFile(self):
        try:
            # Check and see if the file money.txt is there (Contains user data)
            # FIXME: Consider changing to an excel file or .cvc for more writablility
            with open("money.txt", "r"): file_name = "money.txt"

        except IOError:
            # If there is no file, it will produce an error. Pick a new file in this branch
            found_file = False
            file_name = input("Please specify a text file containing user information (include the full file path if the file is in a different directory than the Hangman program):\n")

            while not(found_file):
                try:
                    with open(file_name, "r"): found_file= True
                except IOError:
                    file_name
        return file_name

    def printUsers(self, file_name):
        infile = open(file_name, 'r')
        raw_data = infile.readlines()
        # Iterates through and makes information into two lists
        # FIXME: Consider making a Type:Dictionary
        names = []
        money = []
        for i in range(len(raw_data)):
            if i % 2 == 0:
                names.append(raw_data[i].rstrip())
            elif i % 2 == 1:
                money.append(raw_data[i].rstrip())
        # Stores information in a nested list
        information = [names,money]
        # Iterates over inforamtion and prints it out
        for i in range(1):
            for ix in range(len(information[i])):
                print("{0} has ${1}.".format(information[i][ix],information[i+1][ix]))

    def createNewUser(self, file_name):
        infile = open(file_name, 'r')
        info = infile.readlines()
        # Iterates over and gathers information before it is deleted
        names = []
        money = []
        for i in range(len(info)):
            if i % 2 == 0:
                names.append(info[i])
            elif i % 2 == 1:
                money.append(info[i])
        infile.close()
        os.remove(file_name)

        # Gets a new name and new amount of money for the new user.
        newName = input("What is the new user's name:\n")
        newMoney = input("How much money does the new user have:\n")
        names.append(newName+"\n")
        money.append(newMoney+"\n")
        information = [names,money]

        # New file created
        newfile = open('money.txt', 'w+')
        for i in range(len(information[0])):
            for ix in range(len(information)):
                newfile.write(information[ix][i])
        newfile.close()

    def withdrawal(self, file_name):
        pass

    def deposit(self, file_name):
        pass

def printMainMenu():
    print('''
    ************************************************
    *                    Menu                      *
    ************************************************
    *                                              *
    *   1. New User                                *
    *   2. Print User Balance                      *
    *   3. Withdrawal/Add Money                    *
    *   4. Quit                                    *
    *                                              *
    ************************************************
    ''')

def main():
    user = User()
    file_name = user.getUserFile()

    done = False
    while not done:
        printMainMenu()
        try:
            decision = int(input("What would you like to do?\n"))
            if decision == 1:
                user.createNewUser(file_name)
            elif decision == 2:
                user.printUsers(file_name)
            elif decision == 3:
                userDescision = int(input("Press 1 to withdrawal money and 2 to add money."))
                if userDescision == 1:
                    user.withdrawal(file_name)
                elif userDescision == 2:
                    user.deposit()
            elif decision == 4:
                done == True
                break
            else:
                print("Enter a number from 1 to 4")
        except ValueError:
            print("Oops, somethings not right. Try entering a number from 1 to 4.")

if __name__ == '__main__':
    main()
