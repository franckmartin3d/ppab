# franck 10/05/2018
# Playing cards 3.0
# Demonstrates inheritance - overriding methods


class Card(object):
    """A playing card."""
    # Attribute
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        #initializing constructor
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

# Overriding base methods
class Unprintable_Card(Card):
    '''A Card that won't reveal its rank or suit when printed.'''
    def __str__(self):
        return "<unprintable>"

#Override init
class Positionable_Card(Card):
    """A Card that can be face up or face down."""
    def __init__(self, rank, suit, face_up = True):
        #wtf is this
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


# Main
card1 = Card("A","C")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card ("A", "h")

print("Printing a card object:")
print(card1)

print("\nPrinting an Unprintable_Card object:")
print(card2)

print("\nPrinting a Positionable_Card object:")
print(card3)

print("Flipping the Positionable_Card object.")
card3.flip()

print("Printing the Positionable_Card object:")
print(card3)
input("\n\nPress the enter key to exit.")
