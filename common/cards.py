import abc

ACTIONS = {"A": "Attack",
           "C": "Change",
           "D": "Demand",
           "N": "Negate",
           "S": "Stop"}

RANKS = ("Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two")
SUITS = ("Hearts", "Diamonds", "Clubs", "Spades",)


class Card():
    def __init__(self, rank, suit):
        self.action = None
        self.is_active = False
        self.rank = rank
        self.suit = suit

    def __len__(self):
        return 1

    def __repr__(self):
        return self.rank + " of " + self.suit

    def __str__(self):
        return self.rank + " of " + self.suit

    def act(self):
        return self.action


def generate_cards():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append(Card(rank, suit))
    return deck
