RANKS = ("Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two")
SUITS = ("Hearts", "Diamonds", "Clubs", "Spades",)


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.rank + " of " + self.suit

    def act(self, *args, **kwargs):
        return False, None


class Ace(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def act(self, **kwargs):
        action = ("demand", kwargs["suit"])
        return True, action



class King(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def act(self):
        if self.suit == SUITS[1]:
            action = ("attack", 5, "forwards")
            return True, action
        elif self.suit == SUITS[4]:
            action = ("attack", 5, "backwards")
            return True, action
        else:
            return False, None


class Queen(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Jack(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


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


class Three(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Two(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


def generate_cards():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append(Card(rank, suit))
    return deck
