
from tkinter import *
from tkinter import ttk

from win32api import GetSystemMetrics

class Menu:
    """Has the information to create a menu at the start of the game"""

    def __init__(self, done):
        self.done = done

    # FIXME: Define Logic of Functions
    def playGame(self):
        self.window.destroy()

    def readRules(self):
        pass

    def endGame(self):
        self.done = True
        self.window.destroy()

    def setUpMenu(self):
        # Collects users hight and width screen dimensions
        self.userScreenWidth = GetSystemMetrics(0)
        self.userScreenHeight = GetSystemMetrics(1)

        # Sets up window information using users screen size
        self.window = Tk()
        self.window.title("Jumpman Game | Menu")
        self.window.geometry("{0}x{1}+{2}+{3}".format(int(self.userScreenWidth/4),int(self.userScreenHeight/4),int((self.userScreenWidth/2)-(self.userScreenWidth/8)),int((self.userScreenHeight/2)-(self.userScreenHeight/8))))

        # Set up frames for information
        mainframe = ttk.Frame(self.window, padding= "3 3 12 12")
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

        self.window.mainloop()
