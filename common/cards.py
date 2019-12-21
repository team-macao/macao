import abc

ACTIONS = {"A": "Attack",
           "C": "Change",
           "D": "Demand",
           "N": "Negate",
           "S": "Stop"}

RANKS = ("Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two")
SUITS = ("Hearts", "Diamonds", "Clubs", "Spades",)



class Card(abc.ABC):
    def __init__(self, rank, suit):
        self.action = None
        self.is_active = False
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.rank + " of " + self.suit

    @abc.abstractmethod
    def act(self):
        return self.action


class Ace(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self.is_active = True


class King(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self.is_active = True

        if suit == SUITS[0] or SUITS[3]:
            self.action = ACTIONS["A"]


class Queen(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self.is_active = True

        if suit == SUITS[0] or SUITS[3]:
            self.action = ACTIONS["N"]


class Jack(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self.is_active = True
        self.action = ACTIONS["D"]


class Ten(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Nine(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Eight(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Seven(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Six(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Five(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Four(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self.is_active = True
        self.action = ACTIONS["S"]


class Three(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self.is_active = True
        self.action = ACTIONS["A"]


class Two(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self.is_active = True
        self.action = ACTIONS["A"]


def generate_cards():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append(Card(rank, suit))
    return deck
