
from tkinter import *
from tkinter import ttk

from win32api import GetSystemMetrics

class Menu:
    """Has the information to create a menu at the start of the game"""

    # FIXME: Define Logic of Functions
    def playGame(self):
        pass

    def readRules(self):
        pass

    def endGame(self):
        pass

    def setUpMenu(self):
        # Collects users hight and width screen dimensions
        userScreenWidth = GetSystemMetrics(0)
        userScreenHeight = GetSystemMetrics(1)

        # Sets up window information using users screen size
        window = Tk()
        window.title("Jumpman Game | Menu")
        window.geometry("{0}x{1}+{2}+{3}".format(int(userScreenWidth/4),int(userScreenHeight/4),int((userScreenWidth/2)-(userScreenWidth/8)),int((userScreenHeight/2)-(userScreenHeight/8))))

        # Set up frames for information
        mainframe = ttk.Frame(window, padding= "3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        # Set Up Buttons
        ttk.Button(mainframe,text="Play Game",command=self.playGame).grid(column=0, row=1, sticky=(W,E))
        ttk.Button(mainframe,text="Read Rules",command=self.readRules).grid(column=0, row=3, sticky=(W,E))
        ttk.Button(mainframe,text="Quit Game",command=self.endGame).grid(column=0, row=5, sticky=(W,E))


        # Sets up labels
        ttk.Label(mainframe, text="Jumpman").grid(column=0, columnspan=3, row=0, sticky= (W,E))
        ttk.Label(mainframe, text="Highscore").grid(column=2,columnspan=2, row=1, sticky= (W,E))

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        window.mainloop()

game = Menu()
game.setUpMenu()
