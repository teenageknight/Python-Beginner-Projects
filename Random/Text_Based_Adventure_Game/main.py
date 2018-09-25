# FIXME: add comment intro

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
        player = Player()

# Defenitions
def newGame(arg):
    game = Game()
    game.on_init()

def main():
    # introduction
    # FIXME: Move to a new function
    print("""
    ************************************************
    *                    Menu                      *
    ************************************************
    *                                              *
    *   1. New Game                                *
    *   2. Read Rules                              *
    *   3. Contact the Creaters                    *
    *                                              *
    ************************************************
    """)

    decision = input('What is your decision?\n')

    if decision == '1':
        newGame()

if __name__ == '__main__':
    main()
