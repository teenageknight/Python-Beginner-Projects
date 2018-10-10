# FIXME: add comment intro

# Imports
import menus

# Globals
menu = Menu()

# classes
class Player(object):
    """docstring for Player."""
    # def __init__(self, arg):
    #     super(Player, self).__init__()
    #     self.arg = arg

class Game(object):
    """docstring for Game."""
    # def __init__(self, arg):
    #     self.arg = arg
    def on_init():
        menu.intro()
        player = Player()
        player.selectPlayerType()

# Defenitions
def newGame():
    game = Game()
    game.on_init()


def main():
    # introduction
    # FIXME: Move to a new function

    menu.mainMenu()
    decision = input('What is your decision?\n')

    if decision == '1':
        newGame()

if __name__ == '__main__':
    main()
