'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class InputOutString(object):
    """docstring for InputOutString."""

    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = str(input())
        return self.s

    def printString(self):
        return self.s.upper()
        
strObj = InputOutString()
strObj.getString()

print(strObj.printString())
