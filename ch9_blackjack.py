#Franck 14/05/2018
#Black Jack Game
# From 1 to 7 player compete against a dealer

import ch9_GamesModule, Ch9_CardModule

class BJ_Cards(Ch9_CardModule.Card):
    """A BlackJack card."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Cards.RANKS.index(self.rank) + 1
            if v >10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(Ch9_CardModule.Deck):
    """A Blackjack deck."""
    def populate(self):
        for suit in BJ_Cards.SUITS:
            for rank in BJ_Cards.RANKS:
                self.Ch9_CardModule.append(BJ_Cards(rank, suit))

class BJ_Hand(Ch9_CardModule.Hand):
    """A BlackJack Hand"""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if a card in the hand has a value of None, then total is none
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        # determine if hand contains an ACe
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Cards.ACE_VALUE:
                contains_ace = True

        # if Hand contains Ace and total is low enought, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the ace
            t +=  10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_player(BJ_Hand):
    """A BlackJAck Player"""
    def is_hitting(self):
        response = ch9_GamesModule.ask_yes_no("\n" + self.name + ", do you want a hit? (y/n): ")
        return response == "y"

    def bust(self):
        print(self.name, "bust.")
        self.lose()

    def lose(self):
        print(self.name, "lost.")

    def win(self):
        print(self.name, "win.")

    def push(self):
        print(self.name, "pushes.")

class BJ_Dealer(BJ_Hand):
    """A black jack dealer"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        return (self.name, "bust.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """ A BlackJack Game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                    player.bust()

    def play(self):
        # deal initial 2 cards to everyone
        self.deck.deal(self.players +[self.dealer], per_hand= 2)
        self.dealer.flip_first_card() # hide dealers first card
        for players in self.players:
            print(player)
        print(self.dealer)

        #deal additional card to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card() # dealer reveal first card

        if not self.still_playing:
            #since all player have busted, just the dealer's hand
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()

            else:
                #Compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        #remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tWelcome to BlackJack!\n")

    names = []
    number = ch9_GamesModule.ask_number("How many players? (1-7):", low=1, high=8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)

    print()

    game = BJ_Game(name)

    again = None
    while again != "n":
        game.play()
        again = ch9_GamesModule.ask_yes_no("\n Do you want to play again?: ")

main()
input("\n\nPress the enter key to exit.")

















