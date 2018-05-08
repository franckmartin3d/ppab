#Franck 8/05/2018
#Playing Cards 2.0
# Demonstrate inheritance - class extension

class Card(object):
    """A Playing Card"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    '''A hand of playing cards'''
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep =""
            for card in self.cards:
                rep += str(card) + " "

        else:
            rep = "<empty>"

        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

#Inheriting Class

class Deck(Hand):
    """A deck of playing cards"""
    def populate(self):
        for suite in Card.SUITS:
            for rank in Card.RANKS:
                self.add(card(rank, suite))

    def shuffle(self):
        import  random
        random.shuffle(self, cards)

    def deal(selfself, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.card[0]
                    self.give(top_card, hand)
                else:
                    print ("Cant continue deal. out of cards!")
