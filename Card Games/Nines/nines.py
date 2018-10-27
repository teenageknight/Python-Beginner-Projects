import pygame
import random

from load_images import createImageDict

# Colors
# -------------------
AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
# -------------------

class Player(object):
    """Creates a player and all of its information."""
    def __init__(self, cards):
        self.cards = cards
        self.Turn = True
        self.iteration = 0
        self.flipped = 0
        self.selectedCard = None
        self.rect = pygame.Rect(725, 520, 71, 96)

    def drawCard(self, screen, card_dict):
        pygame.draw.rect(screen,BLACK,[self.rect.left,self.rect.top,71,96],2)
        try:
            screen.blit(card_dict[self.selectedCard],[self.rect.left,self.rect.top])
        except Exception as e:
            pass

    def userTurn(self, deckList):
        # If its the first turn this code will run
        if self.iteration == 0:
            for item in self.cards:
                # Will return True if card is clicked
                if self.flipped < 2:
                    clicked = item.click_down()
                    if clicked:
                        self.flipped += 1
                    print(self.flipped)
                else:
                    pass

            if self.flipped == 2:
                self.iteration = 1
                self.Turn = False

        # Runs until all cards are flipped and once it has run once
        if self.flipped < 9 and self.iteration > 0:
            for deck in deckList:
                temp = deck.click_down()
                if type(temp) == str:
                    self.selectedCard = temp





class Deck(object):
    """
    This is a parent class that sets up the rect objects and checks their
    position.
    """
    def __init__(self, x, y):
        self.cards = []
        self.rect = pygame.Rect(x, y, 71, 96)

    def checkPos(self):
        """This checks if the cursor is on the card."""
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.rect.left and pos[0] <= self.rect.right:
            if pos[1] >= self.rect.top and pos[1] <= self.rect.bottom:
                return True
            else:
                return False
        else:
            return False


class Deck_1(Deck):
    """This is the child class representing the user has."""
    def __init__(self, x, y):
        # Call parent constructor class
        Deck.__init__(self, x, y)
        self.hidden = True
        self.firstTurn = True

    def drawCard(self, screen, card_dict):
        """Draws all of the cards in this deck onto the screen"""
        pygame.draw.rect(screen,BLACK,[self.rect.left,self.rect.top,71,96],2)
        if self.hidden:
            pygame.draw.rect(screen, TEAL, [self.rect.left,self.rect.top,71,96])
        if not self.hidden:
            for item in self.cards:
                screen.blit(card_dict[item],[self.rect.left,self.rect.top])

    def extend_list(self, cardList):
        self.cards.append(cardList[0])

    def click_down(self):
        pos = self.checkPos()
        if pos:
            self.hidden = False
            return True



class Deck_2(Deck):
    """Child class representing the cards in the middle."""
    def __init__(self, x, y):
        # Call parent constructor class
        Deck.__init__(self, x, y)
        self.x = x
        self.y = y
        self.hidden_cards = []

    def drawCard(self, screen, card_dict):
        """Draws the cards onto screen"""
        pygame.draw.rect(screen,BLACK,[self.rect.left,self.rect.top,71,96],2)
        pygame.draw.rect(screen, TEAL, [self.rect.left,self.rect.top,71,96])

    def click_down(self):
        pos = self.checkPos()
        if pos:
            # If card is clicked, the card will be returned and deleted from the list of cards
            card=self.hidden_cards[0]
            del self.hidden_cards[0]
            if card != type(None):
                return card




class Deck_3(Deck):
    """
    This is a child class for all of the cards that have been used and thrown
    out.
    """
    def __init__(self, x, y):
        Deck.__init__(self, x, y)
        self.x = x
        self.y = y


    def drawCard(self, screen, card_dict):
        """Draws the cards onto screen"""
        pygame.draw.rect(screen,BLACK,[self.rect.left,self.rect.top,71,96],2)
        if len(self.cards) == 0:
            pygame.draw.circle(screen, OLIVE, [780,458], 30, 4)
        if len(self.cards) > 0:
            screen.blit(card_dict[self.cards[-1]],[self.rect.left,self.rect.top])

    def click_down(self):
        pos = self.checkPos()
        if pos:
            if len(self.cards) == 0:
                print("No cards")


def shuffle_cards():
    """This shuffle the cards"""
    r = []
    lst = ["ace_clubs", "2_clubs", "3_clubs", "4_clubs", "5_clubs", "6_clubs",
           "7_clubs", "8_clubs", "9_clubs", "10_clubs", "jack_clubs", "queen_clubs",
           "king_clubs", "ace_spades", "2_spades", "3_spades", "4_spades",
           "5_spades", "6_spades", "7_spades", "8_spades", "9_spades", "10_spades",
           "jack_spades", "queen_spades", "king_spades", "ace_hearts", "2_hearts",
           "3_hearts", "4_hearts", "5_hearts", "6_hearts", "7_hearts", "8_hearts",
           "9_hearts", "10_hearts", "jack_hearts", "queen_hearts", "king_hearts",
           "ace_diamonds", "2_diamonds", "3_diamonds", "4_diamonds", "5_diamonds",
           "6_diamonds", "7_diamonds", "8_diamonds", "9_diamonds", "10_diamonds",
           "jack_diamonds", "queen_diamonds", "king_diamonds", "ace_clubs",
           "2_clubs", "3_clubs", "4_clubs", "5_clubs", "6_clubs","7_clubs",
           "8_clubs", "9_clubs", "10_clubs", "jack_clubs", "queen_clubs",
            "king_clubs", "ace_spades", "2_spades", "3_spades", "4_spades",
            "5_spades", "6_spades", "7_spades", "8_spades", "9_spades", "10_spades",
            "jack_spades", "queen_spades", "king_spades", "ace_hearts", "2_hearts",
            "3_hearts", "4_hearts", "5_hearts", "6_hearts", "7_hearts", "8_hearts",
            "9_hearts", "10_hearts", "jack_hearts", "queen_hearts", "king_hearts",
            "ace_diamonds", "2_diamonds", "3_diamonds", "4_diamonds", "5_diamonds",
            "6_diamonds", "7_diamonds", "8_diamonds", "9_diamonds", "10_diamonds",
            "jack_diamonds", "queen_diamonds", "king_diamonds"]

    length = len(lst)
    for i in range(length):
        if len(lst) > 1:
            c = random.choice(lst)
            r.append(c)
            lst.remove(c)
        else:
            c = lst.pop()
            r.append(c)

    return r


def main():
    pygame.init()

    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode([1450, 1000])

    pygame.display.set_caption("Nines")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------------------------------------------
    # Creates a dictanary of images objects. Code in other module
    card_dict = createImageDict()

    # This variable will hold the names of all the shuffled cards
    card_list = shuffle_cards()

    # This list will hold all of the deck objects
    deck_list = [Deck_2(635,410), Deck_1(100,300), Deck_1(190,300),
    Deck_1(280,300), Deck_1(100,410), Deck_1(190,410), Deck_1(280,410),
    Deck_1(100,520), Deck_1(190,520), Deck_1(280,520), Deck_1(1080,300),
    Deck_1(1170,300), Deck_1(1260,300), Deck_1(1080,410), Deck_1(1170,410),
    Deck_1(1260,410), Deck_1(1080,520), Deck_1(1170,520), Deck_1(1260,520),
    Deck_3(744,410)]

    # The code below distributes the cards into the two users decks
    deck_list[1].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[2].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[3].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[4].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[5].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[6].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[7].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[8].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[9].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[10].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[11].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[12].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[13].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[14].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[15].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[16].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[17].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[18].extend_list(card_list[:1])
    del card_list[:1]

    deck_list[0].hidden_cards.extend(card_list)

    # Assigns Players their decks
    player1Cards = deck_list[1:10]
    del deck_list[1:10]
    player2Cards = deck_list[1:10]
    del deck_list[1:10]

    player1 = Player(player1Cards)
    player2 = Player(player2Cards)
    players = [player1, player2]

    # Set the second players turn off so one player goes at a time.
    player2.Turn = False

    # Extra Variables
    game_over = False
    font = pygame.font.Font(None, 25)
    text = font.render("Congratulations, You Won!", True, BLACK)
    userTurn = 0

    # ------------- Main Program Loop --------------------
    while not done:
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill((GREEN))

        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONUP:
                # If not one players turn its the others
                if not player1.Turn:
                    player2.Turn = True
                if not player2.Turn:
                    player1.Turn = True

                # If one players turn, run their turn
                if player1.Turn:
                    player1.userTurn(deck_list)
                elif player2.Turn:
                    player2.userTurn(deck_list)

        # --- Game logic should go here

        # --- Drawing code should go here
        for item in deck_list:
            item.drawCard(screen, card_dict)
        for player in players:
            player.drawCard(screen, card_dict)
            for item in player.cards:
                item.drawCard(screen, card_dict)


        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 20 frames per second
        clock.tick(20)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == '__main__':
    main()
